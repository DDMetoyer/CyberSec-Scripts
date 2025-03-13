'''
Devante Metoyer
02/08/25
Assignment #4
Assignment - File Processing Object

Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Create a class named FileProcessor
   a) The init method shall:
      i) Verify the file exists
      ii) Extract key file system metadata from the file and store them as instance attributes
          i.e. file path, file size, MAC Times, UID, permissions, etc.
   b) Create a get_file_header method which will
      i) Extract the first 20 bytes of the header and store them in an instance attribute
   c) Create a print_file_details method which will
      i) Print the metadata
      ii) Print the hex representation of the header
      
3) Demonstrate the use of the new class
   a) Prompt the user for a directory path
   b) Using the os.listdir() method to extract the filenames from the directory path
   c) Loop through each filename and instantiate an object using the FileProcessor class
   d) Using the object
      i) Invoke the get_file_header method
      ii) Invoke the print_file_details method
      
4) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  alharthiD_WK3_script.py
                 alharthiD_WK3_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''

import os
import hashlib
import sys
import time

# FileProcessor Class 
class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size = None
        self.modified_time = None
        self.created_time = None
        self.hash_results = {}

    def get_file_metadata(self):
        try:
            self.file_size = os.path.getsize(self.file_path)
            self.modified_time = time.ctime(os.path.getmtime(self.file_path))
            self.created_time = time.ctime(os.path.getctime(self.file_path))
        except Exception as e:
            print(f"Error retrieving metadata: {e}")

    def compute_hash(self, algorithm='md5'):
        try:
            with open(self.file_path, 'rb') as file:
                file_contents = file.read()
                if algorithm in hashlib.algorithms_available:
                    hash_obj = hashlib.new(algorithm)
                    hash_obj.update(file_contents)
                    self.hash_results[algorithm] = hash_obj.hexdigest()
                else:
                    print(f"Unsupported hash algorithm: {algorithm}")
        except Exception as e:
            print(f"Error computing hash: {e}")

    def display_results(self):
        print(f"File: {self.file_path}")
        print(f"Size: {self.file_size} bytes")
        print(f"Last Modified: {self.modified_time}")
        print(f"Created Time: {self.created_time}")
        for algo, hash_val in self.hash_results.items():
            print(f"{algo.upper()} Hash: {hash_val}")

# System Info Class
class SystemInfo:
    def __init__(self):
        self.python_version = sys.version_info.major
        self.os_type = sys.platform

    def print_sys_info(self):
        print(f"Python Version: {self.python_version}")
        print(f"Operating System: {self.os_type}")

# Log Analysis
def analyze_log(log_file_path):
    worm_counts = {}
    security_events = []

    try:
        with open(log_file_path, "r", encoding="utf-8", errors="ignore") as log_file:
            for line in log_file:
                if "Worm." in line:
                    worm_name = line.split("Worm.")[1].split(" FOUND")[0]
                    worm_counts[worm_name] = worm_counts.get(worm_name, 0) + 1

                if "authentication failure" in line or "requests/sec are too many" in line:
                    security_events.append(line.strip())
    except Exception as e:
        print(f"Error reading log file: {e}")

    print("=== Worm Infection Statistics ===")
    for worm, count in worm_counts.items():
        print(f"{worm}: {count} occurrences")

    print("\n=== Security Events (First 10) ===")
    for event in security_events[:10]:
        print(event)

# Main Execution
if __name__ == "__main__":
    sys_info = SystemInfo()
    sys_info.print_sys_info()

    log_file = "redhat1.txt"
    analyze_log(log_file)

    # Example usage of FileProcessor class
    file_to_hash = input("Enter file path: ")
    hasher = FileProcessor(file_to_hash)
    hasher.get_file_metadata()
    hasher.compute_hash("md5")
    hasher.compute_hash("sha256")
    hasher.compute_hash("sha512")
    hasher.display_results()
