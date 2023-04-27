import subprocess

var = input("Var (0, 1, 2 or 3--0 takes the longest, but is the best, 2 is the fastest, but is the worst 3 uses ids.txt as the ids): ")
ex_num = input("Execute Number of Times (How many Images do you want? e for all): ")
length = input("Length of URL (Max should be seven, the longer the URL the newer the images): ")

subprocess.run(["python", "LOLSpyware-v1.1.py", var, ex_num, length])
subprocess.run(["python", "Remove_Samples.py"])
subprocess.run(["python", "Extract_Key_Data.py"])
subprocess.run(["python", "Delete_Deuplicate_Files.py"])
