import os
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

# Create a dictionary to store the hashes of the image files
hashes = {}

# Iterate over all image files in the key_data folder
for file_name in os.listdir('key_data'):
    if file_name.endswith('.png'):
        file_path = os.path.join('key_data', file_name)
        file_hash = compute_hash(file_path)
        if file_hash in hashes:
            # Delete the duplicate file
            os.remove(file_path)
            print(f"Deleted duplicate file: {file_path}")
        else:
            hashes[file_hash] = file_name

print("Duplicate files deleted successfully!")
