import os
import re
import sys
import random
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from itertools import product, permutations

def main(ex_num, var, length, wait_all=True):
    url_pattern = re.compile(r'(?<!:)//') # IDK what this is, but it looks important
    if var == 0: # Generate Ids with selected generator
        ids = generate_id(length)
    elif var == 1:
        ids = generate_id_2(length)
    elif var == 3:
        ids = generate_id_4()
    else:
        pass # If statement later in code is used to generate a new id with each iteration
    count = 0

    def process_ids(ids):
        nonlocal count
        for id in ids:
            url = f"https://prnt.sc/{id}" # Attatch Id to URL
            target_element = get_element(url)
            if target_element is not None: # If a URL was found
                image_url = target_element['src']
                original_url = image_url
                image_url = url_pattern.sub('https://', image_url) # Only URLs, that were deleted need to get modified
                if original_url != image_url:
                    print(f"Skipping modified URL for ID {id}")
                    continue # Skip this URL
                try:
                    response = requests.get(image_url) # Get the Image URL from the Id URL
                    if "image" not in response.headers['Content-Type']:
                        print(f"Not an image for ID {id}") # If there isn't an Image element
                        continue
                    image = Image.open(BytesIO(response.content))
                    if not os.path.exists("data"): # If there isn't an data folder, create one
                        os.makedirs("data")
                    image.save(f"data/image_{id}.png") # Save Image to the data folder
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

    if var == 2: # Generate new ID with each iteration
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
    with open('ids.txt', 'r') as f:
        ids = f.read().splitlines()
    return ids

try:
    if len(sys.argv) >= 4: # If enough arguments were passed
        var = int(sys.argv[1]) # Generator Type (0-3)
        if sys.argv[2] == "e": # Execute Number of times
            ex_num = -1
            wait_all = True
        else:
            ex_num = int(sys.argv[2])
            wait_all = False
        length = int(sys.argv[3]) # Length of ids
    else:
        print("Not enough arguments provided. Please input them manually.")
        var = 2 # Set Variables to avoid errors
        ex_num = 1
        length = 1
        ex_num = input("Execute Number of times (e for all)->")
        length = int(input("URL Length (The longer the fresher the image, 7 max for now)->"))
        t_var = input("VAR (Leave this if you don't know it)->")
        if t_var != '':
            var = int(t_var) 
        else:
            var = -1 # If you leave the input and let the next code decide the generator
        if ex_num == "e": # If e is used variable is changed to -1
            ex_num = -1
            wait_all = True
        else:
            ex_num = int(ex_num)
            wait_all = False
        if ex_num == -1 and var == -1: # Configure generator if none is chosen
            var = 0
        elif ex_num > 10000 and var == -1:
            var = 1
        elif ex_num < 10000 and var == -1:
            var = 2
        else:
            pass # If var is chosen, this step get's skipped
    print("var", var)
    main(ex_num, var, length, wait_all)
except Exception as e:
    print("Error", e)
finally:
    print("Done") if len(sys.argv) >= 3 else input("Press any Key to exit...") # You can set print("Done") to print("-" * 50), for seperation
    