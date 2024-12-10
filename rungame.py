import os
import sys
import importlib
import inspect
from Puzzle.game import Puzzle

folder_path = r"C:\Users\Graham\Documents\ambiguopusly-named-game\puzzles"

sys.path.insert(0, folder_path)

puzzles = {}
for filename in os.listdir(folder_path):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        
        module = importlib.import_module(f"puzzles.{module_name}")
        
        for name, obj in inspect.getmembers(module):
            if name[:6] == "Puzzle":
                puzzles[name] = obj


