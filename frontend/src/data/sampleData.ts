import type { GraphData } from '../components/ForceGraph3D';

export const sampleData: GraphData = {
  nodes: [
    { id: 'example-1', title: 'Two Sum', difficulty: 'Easy', concepts: ['Hash Table', 'Array'], type: 'problem' as const },
    { id: 'Hash Table', type: 'concept' as const },
    { id: 'Array', type: 'concept' as const }
  ],
  links: [
    { source: 'example-1', target: 'Hash Table' },
    { source: 'example-1', target: 'Array' }
  ]
};
