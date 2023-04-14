from PIL import Image
import os
import hashlib

image1_path = "./image_sample.png" # replace with the path to the first image
image2_path = "./image_sample_2.png" # replace with the path to the second image

data = "./data"

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

# Loop through all images in the data folder
for image_file_name in os.listdir(data):
    image_file_path = os.path.join(data, image_file_name)
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