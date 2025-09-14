

import React, { useEffect, useState } from 'react';
import ForceGraph3DComponent from './components/ForceGraph3D';
import type { GraphData } from './components/ForceGraph3D';


function App() {
  const [data, setData] = useState<GraphData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('http://localhost:3001/problems')
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch data');
        return res.json();
      })
      .then((problems) => {
        // Convert problems to GraphData format
        const nodes = problems.map((p: any) => ({ ...p, type: 'problem' as const }));
        const conceptSet = new Set<string>();
        problems.forEach((p: any) => (p.concepts || []).forEach((c: string) => conceptSet.add(c)));
        const conceptNodes = Array.from(conceptSet).map((c) => ({ id: c, type: 'concept' as const }));
        const links = problems.flatMap((p: any) => (p.concepts || []).map((c: string) => ({ source: p.id, target: c })));
        setData({ nodes: [...nodes, ...conceptNodes], links });
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div style={{ color: 'white' }}>Loading...</div>;
  if (error) return <div style={{ color: 'red' }}>Error: {error}</div>;
  if (!data) return <div style={{ color: 'red' }}>No data</div>;

  return (
    <div style={{ width: '100vw', height: '100vh', background: '#222' }}>
      <ForceGraph3DComponent data={data} />
    </div>
  );
}

export default App;
