# 8. Write a program to make a copy of a text file “this. txt”

##  first try

# with open("this.txt", "r") as f:
#     content = f.read()

# with open("this_copy.txt", "w") as f:
#     f.write(content)
## eorer handing way

import os

def copyFile(source_filename , destination_filename):
    try:

        # Get script directory using os
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # get source and destination file path
        source_filepath = os.path.join(script_dir, source_filename)
        destination_filepath = os.path.join(script_dir, destination_filename)

        # checks the source
        if not os.path.exists(source_filepath):
            raise FileNotFoundError(f"This file '{source_filename}' does not exist.")
        # read the content from source file
        with open(source_filepath, "r") as f:
            content = f.read()

        # write the content to destination file
        with open(destination_filepath, "w") as f:
            f.write(content)

        print(f"File '{source_filename}' successfully copied to '{destination_filename}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


copyFile("this.txt", "this_copy.txt")
