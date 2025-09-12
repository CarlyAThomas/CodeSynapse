# CodeSynapse

🧠 **CodeSynapse** is an interactive 3D knowledge graph of coding interview problems.  
Visualizes solved problems, their associated concepts, and how they relate, helping you map and review your Computer Science skills in an engaging, exploratory way.

## Tech Stack
- Frontend: React + Vite + TypeScript + react-force-graph-3d
- Backend: Node.js + Express
- Data: JSON initially (can expand to database later)

## Features
- Problems and concepts displayed as nodes in a 3D space  
- Nodes connected if a problem involves a concept  
- Node colors differentiate problem vs. concept  
- Easy to add new problems and concepts  
- Interactive exploration helps identify clusters and gaps in knowledge  

## Setup

### Backend

cd backend

npm install

node index.js

### Frontend

cd frontend

npm install

npm run dev

How to Add Problems

Open backend/problems.json

Add a new problem object with:

{
  
  "id": "unique-id",
  
  "title": "Problem Name",
  
  "difficulty": "Easy|Medium|Hard",
  
  "concepts": ["Concept1", "Concept2"],
  
  "link": "https://example.com/problem"

}

Visit http://localhost:5173 to see your 3D map.
