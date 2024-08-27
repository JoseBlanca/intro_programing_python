import sys
from pathlib import Path

import nbformat

argv = sys.argv

if len(argv) < 2:
    print("Please provide the path to the content folder")
    sys.exit(1)

nb_dir = Path(argv[1])

if not nb_dir.exists():
    print(f"The path provided does not exist: {nb_dir}")
    sys.exit(1)

for dir_path, _, file_names in nb_dir.walk():
    for file_name in file_names:
        if file_name.endswith(".ipynb"):
            nb_path = dir_path / file_name
            print(f"Cleaning outputs for {nb_path}")
            nb = nbformat.read(nb_path, as_version=4)
            for cell in nb.cells:
                if cell.cell_type == "code":
                    cell.outputs = []
                    cell.execution_count = None
            nbformat.write(nb, nb_path)
