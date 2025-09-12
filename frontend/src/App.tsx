
import ForceGraph3DComponent from './components/ForceGraph3D';
import { sampleData } from './data/sampleData';

function App() {
  return (
    <div style={{ width: '100vw', height: '100vh', background: '#222' }}>
      <ForceGraph3DComponent data={sampleData} />
    </div>
  );
}

export default App;
