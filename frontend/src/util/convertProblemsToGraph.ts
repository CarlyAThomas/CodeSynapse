import type { GraphData } from '../components/ForceGraph3D';

export interface Problem {
  id: string;
  title: string;
  difficulty: string;
  concepts: string[];
  link: string;
}

export function convertProblemsToGraph(problems: Problem[]): GraphData {
  const nodes: GraphData['nodes'] = [];
  const links: GraphData['links'] = [];
  const conceptSet = new Set<string>();

  for (const problem of problems) {
    nodes.push({
      id: problem.id,
      title: problem.title,
      difficulty: problem.difficulty,
      concepts: problem.concepts,
      link: problem.link,
      type: 'problem',
    });
    for (const concept of problem.concepts) {
      conceptSet.add(concept);
      links.push({ source: problem.id, target: concept });
    }
  }

  for (const concept of conceptSet) {
    nodes.push({ id: concept, type: 'concept' });
  }

  return { nodes, links };
}
