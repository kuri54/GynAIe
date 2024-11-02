import subprocess
from pathlib import Path

def run():
    viewer_path = Path(__file__).resolve().parent / 'viewer.py'
    subprocess.run(['streamlit', 'run', viewer_path])
