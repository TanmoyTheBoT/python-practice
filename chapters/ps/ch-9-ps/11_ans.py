# Write a python program to rename a file to “renamed_by_ python.txt.

import os

source_filename = "old.txt"
destination_filename = "renamed_by_python.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
source_filepath = os.path.join(script_dir, source_filename)
destination_filepath = os.path.join(script_dir, destination_filename)

if os.path.exists(source_filepath):
    # Read the content of the old file
    with open(source_filepath, "r") as f:
     content = f.read()

    # Write the content to the new file
    with open(destination_filepath, "w") as f:
     f.write(content)
    
    os.remove(source_filepath)
else:
    print("File not found.")