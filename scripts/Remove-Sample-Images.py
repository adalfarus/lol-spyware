# Remove-Sample-Images.py - V1.1
from PIL import Image
import sys
import os
import hashlib

def main(image1, image2, folder, image_folder):
    image1_path = f"./{folder}/{image1}" # define the path to the first image
    image2_path = f"./{folder}/{image2}" # define the path to the second image

    images = f"./{image_folder}"

    image_hash_dict = {}

    for image_path in [image1_path, image2_path]:

        # Calculate the MD5 hash of the image data
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            image_hash = hashlib.md5(image_data).hexdigest()

        # If the hash is already in the dictionary, delete the file
        if image_hash in image_hash_dict:
            os.remove(image_path)
            print(f"{image_path} has been deleted.")
        else:
            image_hash_dict[image_hash] = image_path

    # Loop through all images in the images folder
    for image_file_name in os.listdir(images):
        image_file_path = os.path.join(images, image_file_name)
        if os.path.isfile(image_file_path) and image_file_name.endswith(".png"):

            # Calculate the MD5 hash of the image data
            with open(image_file_path, "rb") as image_file:
                image_data = image_file.read()
                image_hash = hashlib.md5(image_data).hexdigest()

            # If the hash is already in the dictionary, delete the file
            if image_hash in image_hash_dict:
                os.remove(image_file_path)
                print(f"{image_file_name} has been deleted.")
            else:
                image_hash_dict[image_hash] = image_file_path

try:
    if len(sys.argv) >= 5: # If enough arguments were passed
        image1 = sys.argv[1] # First sample image
        image2 = sys.argv[2] # Second sample image
        folder = sys.argv[3] # Folder, where these Sample Images are located
        image_folder = sys.argv[4] # Folder, where the Images are located
    else:
        print("Not enough arguments provided. Please input them manually.")
        image1 = input("First sample image: ")
        image2 = input("Second sample image: ")
        folder = input("Folder, where these Sample Images are located: ")
        image_folder = input("Folder, where the Images are located: ")
    main(image1, image2, folder, image_folder)
except Exception as e:
    print(f"Error: {e}")
finally:
    print(f"All sample images in {folder} removed!") if len(sys.argv) >= 5 else input("Press Enter to exit...") # You can set print command to "-" * 50, for more seperation
