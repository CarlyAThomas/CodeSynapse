import React, { useEffect, useRef } from 'react';
import ForceGraph3D from 'react-force-graph-3d';

interface Node {
  id: string;
  title?: string;
  difficulty?: string;
  concepts?: string[];
  link?: string;
  type?: 'problem' | 'concept';
}

interface Link {
  source: string;
  target: string;
}


export interface GraphData {
  nodes: Node[];
  links: Link[];
}

interface Props {
  data: GraphData;
}

const ForceGraph3DComponent: React.FC<Props> = ({ data }) => {
  const fgRef = useRef<any>(null);

  useEffect(() => {
    if (fgRef.current) {
      fgRef.current.d3Force('charge').strength(-120);
    }
  }, [data]);

  return (
    <ForceGraph3D
      ref={fgRef}
      graphData={data}
      nodeAutoColorBy="type"
      nodeLabel={(node: any) => node.title || node.id}
      linkDirectionalParticles={2}
      linkDirectionalParticleSpeed={0.01}
    />
  );
};

export default ForceGraph3DComponent;
