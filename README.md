# lol_spyware
A humerous project meant to showcase the importance of good cybersecurity

Disclaimer: This project is intended for humorous and educational purposes only. It is not meant to be taken seriously, and it should not be used for malicious or harmful purposes. The aim of this project is to highlight potential security vulnerabilities and demonstrate the importance of strong cybersecurity measures. Any actions taken based on the information presented in this project are solely the responsibility of the user. By using this project, you agree to use it only in a legal and ethical manner, and to refrain from using it to harm and/or harass others.

Note: The existence of key_data and extract_key_data.py is included for educational purposes only, to demonstrate how vulnerabilities in data security can lead to scams and other malicious activities. Any use of this information for illegal or unethical purposes is strictly prohibited.

As for how it functions: 
LOL-Spyware.py -> The main application, it has an endpoint for data
Remove_Samples.py -> Mostly useless, as most removed URL's get filtered out
Extract-Key-Data.py -> Extracts all images containing keywords or parts of them into key_data
Delete-Duplicate-Files.py -> Deletes duplicate files from key_data
Runner-Example.py -> Showcases, how to combine all individual files into one application, using endpoints
id-generator.py -> Generates all ID's for a specific range of length

image_sample.png -> First sample of deleted URL image
image_sample_2.png -> Second sample of deleted URL image
ids.txt -> Contains the generated/special ID's
data -> Folder containing unprocessed images or ones without keyword(s)
key_data -> Folder containing images containing keyword(s)
Tesseract-OCR -> Contains a copy of Tesseract, version 5.0.0, feel free to update
