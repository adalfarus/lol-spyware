[![Actively Maintained](https://img.shields.io/badge/Maintenance%20Level-Actively%20Maintained-green.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)
# lol_spyware V2.1
A humerous project meant to showcase the importance of good cybersecurity

## Disclaimer: 
This project is intended for humorous and educational purposes only. It is not meant to be taken seriously, and it should not be used for malicious or harmful purposes. The aim of this project is to highlight potential security vulnerabilities and demonstrate the importance of strong cybersecurity measures. Any actions taken based on the information presented in this project are solely the responsibility of the user. By using this project, you agree to use it only in a legal and ethical manner, and to refrain from using it to harm and/or harass others.

## Note: 
The existence of filtered_images and Filter-Images.py is included for educational purposes only, to demonstrate how vulnerabilities in data security can lead to scams and other malicious activities. Any use of this information for illegal or unethical purposes is strictly prohibited.

### As for how it works:

- **LOL-Spyware.py**: Main application, endpoint for data handling.
- **Remove-Samples.py**: Limited utility, filters out most removed URLs.
- **Filter-Images.py**: Scans images for keywords/parts of keywords, organizing them into a designated folder.
- **Delete-Duplicate-Files.py**: Eliminates duplicate files from a chosen folder.
- **Runner-Example.py**: Demonstrates integrating all scripts into a single application using endpoints.
- **id-generator.py**: Creates IDs for a specified range.

### File Structure:

- **images**: Folder containing unprocessed or non-keyword images.
- **filtered_images**: Folder with images containing keyword(s).
- **data**: Folder containing data utilized by the scripts.
  - *image_sample.png*: First sample of a deleted URL image.
  - *image_sample_2.png*: Second sample of a deleted URL image.
  - *ids.txt*: Contains generated/special IDs.
  - *del_ids.txt*: Lists known deleted IDs.
- **Tesseract-OCR**: Contains a copy of Tesseract, version 5.0.0, feel free to update
