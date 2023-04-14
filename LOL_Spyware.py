import os
import re
import sys
import random
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from itertools import product, permutations

def main(ex_num, var, length):
    url_pattern = re.compile(r'(?<!:)//')
    if var == 0:
        ids = generate_id(length)
    elif var == 1:
        ids = generate_id_2(length)
    elif var == 2:
        pass
    else:
        ids = generate_id_4()
    count = 0
    while count < ex_num:
        id = ids.pop(0) if var == 0 or var == 1 or var == 3 and ids != [] else generate_id_3(length)
        #id = random.choice(ids) if var == 0 or var == 1 or var == 3 else generate_id_3(length)
        #ids.remove(id) if var == 0 or var == 1 or var == 3 else print("Nothing to remove")
        url = f"https://prnt.sc/{id}"
        target_element = get_element(url)
        if target_element is not None:
            image_url = target_element['src']
            original_url = image_url
            image_url = url_pattern.sub('https://', image_url)
            if original_url != image_url:
                #print("URL was modified:", original_url, "->", image_url)
                print(f"Skipping modified URL for ID {id}")
                continue
            try:
                response = requests.get(image_url)
                if "image" not in response.headers['Content-Type']:
                    print(f"Not an image for ID {id}")
                    continue
                image = Image.open(BytesIO(response.content))
                if not os.path.exists("data"):
                    os.makedirs("data")
                image.save(f"data/image_{id}.png")
                print(f"Image for ID {id} saved successfully!")
                count += 1
            except Exception as e:
                print("Error", e)
        elif target_element is None:
            print(f"No target element found for ID {id}")
        else:
            print("Unknown Scenario")
        
def get_element(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
    }

    # Send a request to the URL and obtain the HTML content
    response = requests.get(url, headers=headers)
    html_content = response.content

    # Use BeautifulSoup to parse the HTML content and locate the img element
    soup = BeautifulSoup(html_content, "html.parser")
    target_element = soup.find("img", {"id": "screenshot-image"})

    return target_element
    
def generate_id(length):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    id_list = []
    for combination in product(characters, repeat=length):
        id_list.append(''.join(combination))
    return id_list

def generate_id_2(length):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    id_list = []
    for combination in product(characters, repeat=length):
        id_list.append(''.join(combination))
    random.shuffle(id_list)
    return id_list

def generate_id_3(length):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    id = ""
    id = ''.join(random.choices(characters, k=length))
    return id
    
def generate_id_4():
    with open('ids.txt', 'r') as f:
        ids = f.read().splitlines()
    return ids
    
try:
    param1 = int(sys.argv[1])
    param2 = sys.argv[2]
    param3 = int(sys.argv[3])
    if param1 == '' and param2 == '' and param3 == '':
        var = -1
        ex_num = int(input("ex_num (e for all)->"))
        length = int(input("URL Length (Max of 7 last)->"))
        t_var = input("VAR (Leave this if you don't know it)->")
        var = int(t_var) if t_var != '' else print("var pass")
        if ex_num == "e" and var == -1:
            ex_num = -1
            var = 0
        elif ex_num > 10000 and var == -1:
            var= 0
        elif ex_num < 10000 and var == -1:
            var =1
        else:
            pass
    else:
        var = param1
        ex_num = int(param2) if param2 != "e" else -1
        length = param3
    main(ex_num, var, length)
except Exception as e:
    print("Error", e)
finally:
    print("Press any Key to exit...")
