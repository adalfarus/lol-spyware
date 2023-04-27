# Delete-Duplicate-Files.py - V1.1
import os
import sys
import hashlib

# Define a function to compute the hash of a file
def compute_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.digest()

def main(folder):
    # Create a dictionary to store the hashes of the image files
    hashes = {}

    # Iterate over all image files in the specified folder
    for file_name in os.listdir(folder):
        if file_name.endswith('.png'):
            file_path = os.path.join(folder, file_name)
            file_hash = compute_hash(file_path)
            if file_hash in hashes:
                # Delete the duplicate file
                os.remove(file_path)
                print(f"Deleted duplicate file: {file_path}")
            else:
                hashes[file_hash] = file_name

try:
    if len(sys.argv) >= 2: # If enough arguments were passed
        folder = sys.argv[1] # Folder to delete duplicate files from
    else:
        print("Not enough arguments provided. Please input them manually.")
        folder = input("Folder to delete duplicate files from: ")
    main(folder)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Duplicate files deleted successfully!") if len(sys.argv) >= 2 else input("Press Enter to exit...") # You can set print command to "-" * 50, for more seperation
