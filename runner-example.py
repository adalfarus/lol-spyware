# runner-example.py - V1.3.0
import subprocess

print("""Welcome to LOL-Spyware! Please use one of the following Options: 
        0 - Generates all ids, then uses them
        1 - Generates all ids, shuffels them, then uses them
        2 - Generates a new random id, each iteration
        3 - Uses ids.txt as the ids (!No spaces!)
        None - Let the Computer decide
Quick Summary -> 0, 1, 2 or 3--0 takes the longest, but is the best, 2 is the fastest, but is the worst 3 uses ids.txt as the ids""")
gen = input("Gen: ")
print("""Number - The number of times you want the main script to be executed
        E - Scrape all possible images, with the selected method
        Quick Summary -> The number of Images you want? e for all""")
ex_num = input("Execute Number of Times: ")
print("""The longer the id the newer the photos scraped will be, but also the fewer images there are, 4 has the most images, 7 is the newest, this could change with time.
Quick Summary -> the longer the URL the newer the images, max should be seven""")
length = input("Length of URL: ")

wait_all = ex_num.lower() == "e"
if wait_all: # If e is used variable is changed to -1
    ex_num = -1

if ex_num == -1 and gen == None: # Configure generator if none is chosen
    gen = 0
elif ex_num > 10000 and gen == -1:
    gen = 1
elif ex_num < 10000 and gen == -1:
    gen = 2
else:
    pass # If gen is chosen, this step get's skipped
print(f"Generator {gen}")

# Define your keywords
print("""Seperate with space
The Keywords you want filter the scraped image with
Quick Summary -> Your Keywords""")
keywords = input("Keywords: ") or "password login credentials blockchain adress ETH wallet bank CC CVV Experation @ BTC"

subprocess.run(["python", "scripts/LOL-Spyware.py", str(gen), str(ex_num), str(length), str(wait_all)]) # Run the main python script with the input variables
subprocess.run(["python", "scripts/Remove-Sample-Images.py", "image_sample.png", "image_sample_2.png", "data", "images"]) # Run the 'Remove-Sample-Images.py' python script
subprocess.run(["python", "scripts/Delete-Duplicate-Files.py", "images"]) # Run the 'Delete-Duplicate-Files.py' python script
subprocess.run(["python", "scripts/Filter-Images.py", "images", "filtered_images", keywords]) # Run the 'Filter-Images.py' python script

input("Press Enter to exit...")
