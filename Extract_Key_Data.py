import os
import shutil
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'./Tesseract-OCR/tesseract.exe'

# Define your keywords
keywords = ['password', 'login', 'credentials', 'blockchain', 'adress', 'ETH', 'wallet', 'bank', 'CC', 'CVV', 'Experation', '@', 'BTC']

# Set the path to your data folder
data_folder = './data'

# Set the path to your key_data folder (create the folder if it doesn't exist)
key_data_folder = './key_data'
os.makedirs(key_data_folder, exist_ok=True)

# Iterate through the files in the folder
for filename in os.listdir(data_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Check if the file is an image
        img_path = os.path.join(data_folder, filename)
        img = Image.open(img_path)

        # Extract text from the image using pytesseract
        extracted_text = pytesseract.image_to_string(img).lower()

        # Check if any keyword is present in the extracted text
        if any(keyword.lower() in extracted_text for keyword in keywords):
            # Move the image to the key_data folder
            shutil.move(img_path, os.path.join(key_data_folder, filename))
            print(f'Image {filename} contains one of the keywords and has been moved to the key_data folder.')
        else:
            print(f'Image {filename} does not contain any keywords.')
