import json
import os
from pathlib import Path

project = Path(__file__).resolve().parent
os.chdir(project)
os.environ['HW3P2_MODE'] = 'smoke'
os.environ.setdefault('MPLBACKEND', 'Agg')
notebook = json.loads((project / 'HW3P2_Student_Starter_Notebook_F26.ipynb').read_text())
namespace = {}
for cell in notebook['cells']:
    if cell['cell_type'] != 'code':
        continue
    name = cell['metadata'].get('id', '')
    if name == 'inference-gate':
        break
    print(f'Running: {name}', flush=True)
    exec(compile(''.join(cell['source']), f'<notebook:{name}>', 'exec'), namespace)
namespace['trainer'].cleanup()
print('Local smoke run finished. Check saved_runs/smoke_test for checkpoints.')
