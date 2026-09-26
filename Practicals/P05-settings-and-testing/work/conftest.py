import sys
from pathlib import Path

P05_DIR = Path(__file__).resolve().parent.parent
P04_WORK = P05_DIR.parent / "P04-from-notebook-to-package" / "work"

if str(P04_WORK) not in sys.path:
    sys.path.insert(0, str(P04_WORK))
