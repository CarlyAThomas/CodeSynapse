import os
import re
import json

PROBLEMS_DIR = os.path.join(os.path.dirname(__file__), 'problems')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'problems.json')

def extract_metadata_from_docstring(docstring):
    metadata = {}
    # Patterns for each field
    patterns = {
        'title': r'Problem:\s*(.*)',
        'difficulty': r'Difficulty:\s*(.*)',
        'concepts': r'Concepts:\s*(.*)',
        'link': r'Link:\s*(.*)'
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, docstring)
        if match:
            value = match.group(1).strip()
            if key == 'concepts':
                metadata[key] = [c.strip() for c in value.split(',')]
            else:
                metadata[key] = value
    return metadata


def main():
    problems = []
    py_files = [f for f in os.listdir(PROBLEMS_DIR) if f.endswith('.py')]
    py_files.sort()  # Ensure consistent order
    for idx, filename in enumerate(py_files, 1):
        file_path = os.path.join(PROBLEMS_DIR, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        docstring_match = re.match(r'"""(.*?)"""', content, re.DOTALL)
        if docstring_match:
            docstring = docstring_match.group(1)
            meta = extract_metadata_from_docstring(docstring)
            if meta:
                meta_out = {
                    "id": f"{idx:012d}",
                    "title": meta.get("title", ""),
                    "difficulty": meta.get("difficulty", ""),
                    "concepts": meta.get("concepts", []),
                    "link": meta.get("link", "")
                }
                problems.append(meta_out)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        json.dump(problems, out, indent=2)
    print(f"Wrote {len(problems)} problems to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
