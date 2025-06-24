'''
 Searching for Digital Images with Python:

1) Prompts the user for a directory path to search

2) Verify that the path provided exists and is a directory

3) Iterate through each file in that directory and examine it using PIL.

4) Generate a PrettyTable report of your search results 
'''

import os
from PIL import Image
from prettytable import PrettyTable

def analyze_images(directory_path):
    """
    Analyzes image files in a given directory and displays metadata in a PrettyTable.
    """
    # Verify if the provided path exists and is a directory
    if not os.path.isdir(directory_path):
        print("Invalid directory. Please provide a valid directory path.")
        return

    # Create a PrettyTable for displaying results
    table = PrettyTable(["File", "Ext", "Format", "Width", "Height", "Mode"])

    # Iterate through all files in the directory
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)

        # Ensure the item is a file
        if os.path.isfile(file_path):
            try:
                # Open the image using PIL
                with Image.open(file_path) as img:
                    # Extract file metadata
                    file_ext = os.path.splitext(file_name)[1].lower()
                    file_format = img.format
                    width, height = img.size
                    mode = img.mode

                    # Add file data to the table
                    table.add_row([file_path, file_ext, file_format, width, height, mode])
            except Exception as e:
                print(f"Skipping {file_name}: {e}")

    # Print the results in tabular format
    print(table)

if __name__ == "__main__":
    # Prompt the user for a directory path
    directory = input("Enter a directory path to search: ").strip()
    
    # Call the function to analyze images
    analyze_images(directory)
