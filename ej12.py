import os
from collections import defaultdict

root_folder = r"C:\Usuarios\debim"

file_names = defaultdict(list)

for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        file_names[filename].append(file_path)

duplicates = {name: paths for name, paths in file_names.items() if len(paths) > 1}

if duplicates:
    print("Found files with duplicate names:")
    for name, paths in duplicates.items():
        print(f"\n{name}:")
        for path in paths:
            print(f"  {path}")
else:
    print("No files with duplicate names found.")
