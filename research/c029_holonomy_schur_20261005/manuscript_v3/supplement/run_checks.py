"""Run the complete exact computational suite in dependency order.

Copy the input packet before executing: programs create outputs beside their sources.
Requires Python 3 and SymPy 1.14.0. NumPy is optional, for labeled illustrations only.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent / 'certificates'
COMMANDS = [
    'analytic/verify_r2_certificate.py',
    'audit/replay_direct_graph_seed.py',
    'audit/replay_local_from_direct_graph.py',
    'new_conjecture/verify_antiperiodic_counterexample.py',
    'audit/replay_antiperiodic.py',
    'strengthening/verify_uniform_cap.py',
    'strengthening/audit/replay_stronger_cap.py',
    'r4_pilot/verify_r4_pilot.py',
    'r4_pilot/audit/replay_r4_phase.py',
    'unequal_cells/verify_unequal_cells.py',
    'unequal_cells/audit/independent_assembly.py',
    'r6_completion/verify_r6_completion.py',
    'r6_completion/audit/replay_r6.py',
]

if __name__ == '__main__':
    for relative in COMMANDS:
        print('\nRunning ' + relative, flush=True)
        subprocess.run([sys.executable, str(ROOT / relative)], cwd=ROOT, check=True)
