import itertools

# Define the characters to use
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

fr = int(input("From->"))
to = int(input("To->"))+1

print("Everything is going well, just wait. You can check the size of the generated file to be sure(combination.txt).")

# Open a file for writing
with open('combinations.txt', 'w') as f:
    # Generate all possible combinations with lengths up to variable to
    for i in range(fr, to):
        combinations = itertools.product(characters, repeat=i)
        for combination in combinations:
            # Write each combination to the file without whitespaces
            f.write(''.join(combination))
            f.write('\n')
input("Done, press any key to exit...")