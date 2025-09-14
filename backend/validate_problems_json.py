import subprocess
import json
import os

PROBLEMS_JSON = os.path.join(os.path.dirname(__file__), 'problems.json')
GEN_SCRIPT = os.path.join(os.path.dirname(__file__), 'generate_problems_json.py')


def load_valid_concepts():
    concepts_path = os.path.join(os.path.dirname(__file__), 'concepts.json')
    if not os.path.exists(concepts_path):
        print("concepts.json was not found.")
        return set()
    with open(concepts_path, 'r', encoding='utf-8') as f:
        concepts_data = json.load(f)
    valid_concepts = set()
    for group in concepts_data.values():
        valid_concepts.update(group)
    return valid_concepts

def validate_problems_json():
    # Run the generation script
    try:
        subprocess.run(['python3', GEN_SCRIPT], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running generate_problems_json.py: {e}")
        return False

    # Check if problems.json exists
    if not os.path.exists(PROBLEMS_JSON):
        print("problems.json was not created.")
        return False

    # Validate JSON structure and concepts
    try:
        with open(PROBLEMS_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        assert isinstance(data, list), "problems.json should be a list"
        valid_concepts = load_valid_concepts()
        all_valid = True
        for problem in data:
            assert 'id' in problem, "Missing 'id' in a problem entry"
            assert 'title' in problem, "Missing 'title' in a problem entry"
            assert 'difficulty' in problem, "Missing 'difficulty' in a problem entry"
            assert 'concepts' in problem, "Missing 'concepts' in a problem entry"
            assert 'link' in problem, "Missing 'link' in a problem entry"
            # Check concepts
            invalid = [c for c in problem['concepts'] if c not in valid_concepts]
            if invalid:
                print(f"Problem '{problem['title']}' (id: {problem['id']}) has invalid concepts: {invalid}")
                all_valid = False
        if all_valid:
            print("problems.json is valid and contains", len(data), "problems.")
        else:
            print("problems.json has problems with invalid concepts.")
        return all_valid
    except Exception as e:
        print(f"Validation failed: {e}")
        return False

if __name__ == '__main__':
    valid = validate_problems_json()
    exit(0 if valid else 1)
