import os
import sys

current_dir = os.path.dirname(__file__)                         # file1
project_root = os.path.dirname(os.path.dirname(current_dir))    # dir
sys.path.append(project_root)