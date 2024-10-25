import subprocess
from pathlib import Path

def run():
    exproler_path = Path(__file__).resolve().parent / 'viewer.py'
    subprocess.run(['streamlit', 'run', exproler_path])