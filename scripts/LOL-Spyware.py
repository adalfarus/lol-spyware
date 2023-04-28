# LOL-Spyware.py - V1.2.1
import os
import re
import sys
import random
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from itertools import product, permutations

def main(gen, ex_num, length, wait_all=False):
    url_pattern = re.compile(r'(?<!:)//') # Compiling common URL pattern to regular expression object
    def no_generator_chosen():
        raise Exception("No Generator chosen")

    def del_ids():
        with open('./data/del_ids.txt', 'r') as f:
            del_ids = f.read().splitlines()
        return del_ids

    def process_ids(ids):
        nonlocal count
        for id in ids:
            if id in del_ids:
                print(f"Skipping known deleted ID {id}")
                continue # Skip this URL
            url = f"https://prnt.sc/{id}" # Attatch Id to URL
            target_element = get_element(url)
            if target_element is not None: # If a URL was found
                image_url = target_element['src']
                original_url = image_url
                image_url = url_pattern.sub('https://', image_url) # Only URLs, that were deleted need to get modified
                if original_url != image_url:
                    print(f"Skipping modified URL for ID {id}")
                    with open('./data/del_ids.txt', 'a') as f:
                        f.write(f'{id}')
                        f.write('\n')
                    continue # Skip this URL
                try:
                    response = requests.get(image_url) # Get the Image URL from the Id URL
                    if "image" not in response.headers['Content-Type']:
                        print(f"Not an image for ID {id}") # If there isn't an Image element
                        continue
                    image = Image.open(BytesIO(response.content))
                    if not os.path.exists("images"): # If there isn't an images folder, create one
                        os.makedirs("images")
                    image.save(f"images/image_{id}.png") # Save Image to the images folder
                    print(f"Image for ID {id} saved successfully!")
                    count += 1 # For how many Images you want, only those that actually get saved count
                    if count == ex_num: # If desired number of images have been saved, exit the function
                        return
                except Exception as e:
                    print("Error", e)
            elif target_element is None: # If no URL was found
                print(f"No target element found for ID {id}")
            else:
                print("Unknown Scenario")
                
    def get_element(url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
        } # To trick the website

        # Send a request to the URL and obtain the HTML content
        response = requests.get(url, headers=headers)
        html_content = response.content

        # Use BeautifulSoup to parse the HTML content and locate the img element
        soup = BeautifulSoup(html_content, "html.parser")
        target_element = soup.find("img", {"id": "screenshot-image"})

        return target_element
    
    def generate_id(length): # Generate all Ids as once
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        id_list = []
        for combination in product(characters, repeat=length):
            id_list.append(''.join(combination))
        return id_list

    def generate_id_2(length): # Generate all Ids at once and suffle them
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        id_list = []
        for combination in product(characters, repeat=length):
            id_list.append(''.join(combination))
        random.shuffle(id_list)
        return id_list

    def generate_id_3(length): # Generate one id at a time
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        id = ""
        id = ''.join(random.choices(characters, k=length))
        return id
        
    def generate_id_4(): # Use ids.txt file
        with open('./data/ids.txt', 'r') as f:
            ids = f.read().splitlines()
        return ids

    if gen == 0: # Generate Ids with selected generator
        ids = generate_id(length)
    elif gen == 1:
        ids = generate_id_2(length)
    elif gen == 2:
        pass # If statement later in code is used to generate a new id with each iteration
    elif gen == 3:
        ids = generate_id_4()
    else:
        raise Exception("No Generator chosen")
        
    count = 0
    
    del_ids = del_ids()

    if gen == 2: # Generate new ID with each iteration
        if wait_all:
            print("wait_all flag is ignored for var=2.")
        for i in range(ex_num):
            id = generate_id_3(length)
            process_ids([id])
            if count == ex_num:
                print(f"Desired number of IDs processed after {i+1} iterations.")
                break
    elif wait_all:
        process_ids(ids)
        if not ids:
            print("All IDs have been processed.")
    else:
        for i in range(ex_num):
            process_ids(ids)
            if not ids:
                print(f"All IDs have been processed after {i+1} iterations.")
                break
            elif i == ex_num-1:
                print(f"Desired number of IDs processed after {i+1} iterations.")

try:
    if len(sys.argv) >= 5: # If enough arguments were passed
        gen = int(sys.argv[1]) # Generator Type
        ex_num = int(sys.argv[2]) # Execute Number of times
        length = int(sys.argv[3]) # ID Length
        wait_all = bool(sys.argv[4]) # Wait for all available IDs to be scraped
    else:
        print("Not enough arguments provided. Please input them manually.")
        gen = int(input("Generator Type: "))
        ex_num = int(input("Execute Number of times: "))
        length = int(input("ID Length: "))
        wait_all = bool(input("Wait for all available IDs to be scraped: "))
    main(gen, ex_num, length, wait_all)
except Exception as e:
    print(f"Error: {e}")
finally:
    print(f"All available IDs scraped!") if len(sys.argv) >= 5 else input("Press Enter to exit...") # You can set print command to "-" * 50, for more seperation
