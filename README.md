# CodeSynapse

🧠 **CodeSynapse** is an interactive 3D knowledge graph of coding interview problems.  
Visualizes solved problems, their associated concepts, and how they relate, helping you map and review your Computer Science skills in an engaging, exploratory way.

## Tech Stack
- Frontend: React + Vite + TypeScript + react-force-graph-3d
- Backend: Node.js + Express
- Data: JSON (generated from Python problem files, can later be extended to a database)

## Features
- Problems and concepts displayed as nodes in a 3D space  
- Edges connect problems to their related concepts 
- Node colors differentiate problem types (problem vs. concept)
- Easy to add new problems by dropping in Python files with metadata
- Interactive exploration helps identify clusters and gaps in knowledge

## Setup

### Backend

Install dependencies and start the backend server:
```
cd backend
npm install
node index.js
```
The backend automatically serves problems.json, which is generated from the Python problem files in backend/problems/.

#### Adding Problems
All problems are located as Python files in the `backend/problems/` folder.  
**Do not edit `problems.json` directly**—it is generated automatically.

To add a new problem:
1. Create a new Python file in `backend/problems/` (e.g., `my_problem.py`).
2. At the top of the file, include a docstring with metadata in this format:
   ```python
   """
   Problem: Problem Name
   Difficulty: Easy|Medium|Hard
   Concepts: Concept1, Concept2
   Link: https://example.com/problem
   """
   ```

   ⚠️ Only concepts listed in `backend/concepts.json` are considered valid. If a problem uses a concept not in that file, validation will fail.

3. Run the validation script to check formatting:
   ```python
   python3 validate_problems_json.py
   ```

4. Generate the updated problems.json:
   ```python
   python3 generate_problems_json.py
   ```

⚠️ Do not edit problems.json manually. It is always auto-generated.

### Frontend

Install dependencies and start the development server:

```
cd frontend
npm install
npm run dev
```
By default, the frontend runs on http://localhost:5173.

### Notes

* ℹ️ Both frontend and backend must be served from the same domain (or proxied) to avoid CSP issues.

* A preprocessed sample dataset is available at frontend/src/data/sampleData.ts. This can be used for testing without a backend.
