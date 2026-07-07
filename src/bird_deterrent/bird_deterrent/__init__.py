
import sys
from pathlib import Path

_repo_root = Path('/home/bird_deterrent_system/bird_deterrent_project').resolve()
if _repo_root.exists() and str(_repo_root) not in sys.path:
	sys.path.insert(0, str(_repo_root))

from bird_deterrent import BirdDeterrentSystem

__all__ = ['BirdDeterrentSystem']

