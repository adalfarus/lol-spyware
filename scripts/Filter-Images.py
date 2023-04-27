# Filter-Images.py - V1.1
import os
import sys
import shutil
import pytesseract
from PIL import Image

def main(folder, ffolder, keywords):
    # Set the path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'./Tesseract-OCR/tesseract.exe'

    # Set the path to your images folder
    images_folder = f'./{folder}'

    # Set the path to your filtered_images folder (create the folder if it doesn't exist)
    filtered_images_folder = f'./{ffolder}'
    os.makedirs(filtered_images_folder, exist_ok=True)

    # Iterate through the files in the folder
    for filename in os.listdir(images_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Check if the file is an image
            img_path = os.path.join(images_folder, filename)
            img = Image.open(img_path)

            # Extract text from the image using pytesseract
            extracted_text = pytesseract.image_to_string(img).lower()

            # Check if any keyword is present in the extracted text
            if any(keyword.lower() in extracted_text for keyword in keywords):
                # Move the image to the filtered_images folder
                shutil.move(img_path, os.path.join(filtered_images_folder, filename))
                print(f'Image {filename} contains one of the keywords and has been moved to the {ffolder} folder.')
            else:
                print(f'Image {filename} does not contain any keywords.')

try:
    if len(sys.argv) >= 4: # If enough arguments were passed
        folder = sys.argv[1] # Folder to scan images from
        ffolder = sys.argv[2] # Folder to move images to
        keywords = sys.argv[3].split() # Keywords to filter images with
    else:
        print("Not enough arguments provided. Please input them manually.")
        folder = input("Folder to scan images from: ")
        ffolder = input("Folder to move images to: ")
        keywords = input("Keywords to filter images with: ").split()
    main(folder, ffolder, keywords)
except Exception as e:
    print(f"Error: {e}")
finally:
    print(f"All images in {folder} scanned! And moved filtered images to {ffolder}") if len(sys.argv) >= 4 else input("Press Enter to exit...") # You can set print command to "-" * 50, for more seperation
