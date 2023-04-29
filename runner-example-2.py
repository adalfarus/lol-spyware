# runner-example-2.py - V1.1.1
import subprocess
import os
import sys

def var():
    def gen_wrapper():
        global gen
        print("0 - Generates all ids, then uses them")
        print("1 - Generates all ids, shuffels them, then uses them")
        print("2 - Generates a new random id, each iteration")
        print("3 - Uses ids.txt as the ids (!No spaces!)")
        print("Quick Summary -> 0, 1, 2 or 3--0 takes the longest, but is the best, 2 is the fastest, but is the worst 3 uses ids.txt as the ids")
        gen = input("Gen: ")
    def ex_num_wrapper():
        global ex_num
        print("Number - The number of times you want the main script to be executed")
        print("E - Scrape all possible images, with the selected method")
        print("Quick Summary -> The number of Images you want? e for all")
        ex_num = input("Execute Number of Times: ")
    def length_wrapper():
        global length
        print("The longer the id the newer the photos scraped will be, but also the fewer images there are")
        print("4 has the most images, 7 is the newest, this could change with time")
        print("Quick Summary -> the longer the URL the newer the images, max should be seven")
        length = input("Length of URL: ")
    def keywords_wrapper():
        global keywords
        print("Seperate with space")
        print("The Keywords you want filter the scraped image with")
        print("Quick Summary -> Your Keywords")
        keywords = input("Keywords: ")
    options = {
        "0": gen_wrapper,
        "1": ex_num_wrapper,
        "2": length_wrapper,
        "3": keywords_wrapper,
        "4": main
    }
    while True:
        action = input("0:Set Generator\n1:Set Ex_Num\n2:Set Length\n3:Set Keywords\n4:Back\n->")
        if action in options:
            options[action]()
            break
        else:
            print("Invalid choice. Please try again.")
    var()

def sps():
    def lol_spy_wrapper():
        if gen and ex_num and length and wait_all and keywords:
            subprocess.run(["python", "scripts/LOL-Spyware.py", str(gen), str(ex_num), str(length), str(wait_all)])
        else:
            subprocess.run(["python", "scripts/LOL-Spyware.py"])
    def rem_sam_im_wrapper():
        subprocess.run(["python", "scripts/Remove-Sample-Images.py", "image_sample.png", "image_sample_2.png", "data", "images"])
    def del_dup_wrapper():
        subprocess.run(["python", "scripts/Delete-Duplicate-Files.py", "images"])
    def fil_im_wrapper():
        if keywords:
            subprocess.run(["python", "scripts/Filter-Images.py", "images", "filtered_images", keywords])
        else:
            subprocess.run(["python", "scripts/Filter-Images.py", "images", "filtered_images"])
    def id_gen_wrapper():
        subprocess.run(["python", "scripts/id-generator.py"])
    options = {
        "0": lol_spy_wrapper,
        "1": rem_sam_im_wrapper,
        "2": del_dup_wrapper,
        "3": fil_im_wrapper,
        "4": id_gen_wrapper,
        "5": main
    }
    while True:
        action = input("0:Start LOL-Spyware Script\n1:Start Remove-Sample-Images Script\n2:Start Delete-Duplicate-Files Script\n3:Start Filter-Images Script\n4:Start id-generator script\n5:Back\n->")
        if action in options:
            options[action]()
            break
        else:
            print("Invalid choice. Please try again.")
    sps()

def li_wrapper():
    # Define the directories to list
    directories = ['images', 'filtered_images']

    # Loop through each directory
    for directory in directories:
        print(directory + '/')
        
        # Get a list of files and directories in the current directory
        items = os.listdir(directory)
        
        # Loop through each item in the directory
        for item in items:
            # Check if the item is a directory
            if os.path.isdir(os.path.join(directory, item)):
                # If it's a directory, print it and its contents indented
                print('  ' + item + '/')
                
                subitems = os.listdir(os.path.join(directory, item))
                for subitem in subitems:
                    print('    ' + subitem)
            else:
                # If it's a file, print its name indented
                print('  ' + item)
    main()
    
def settings():
    print("This is just an example, so there aren't any settings here")
    main()

def main():
    options = {
        "0": var,
        "1": sps,
        "2": li_wrapper,
        "3": settings,
        "4": sys.exit
    }
    while True:
        action = input("0:Set Variables\n1:Start Scripts\n2:List Images\n3:Settings\n4:Exit\n->")
        if action in options:
            options[action]()
            break
        else:
            print("Invalid choice. Please try again.")
    main()

if __name__ == "__main__":
##    check_database("database.db")
##    if not check():
##        try:
##            os.remove("database.db")
##        finally:
##            create_encrypted_database("database.db", get_master_password())
    print("Runner Example 2 v1.1.2 for LOL-Spyware v1.2.1\nCreated by Me :)")
    main()
