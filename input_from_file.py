# Open the file for reading
with open('filename.txt', 'r') as file:
    # Loop over each line in the file
    for line in file:
        # Process the line
        print(line)

# Open the file for reading
with open('filename.txt', 'r') as file:
    # Read the entire contents of the file into a string
    contents = file.read()

# Process the contents of the file
print(contents)

# Redirect standard input to read from a file
import sys
sys.stdin = open('filename.txt', 'r')

# Read input from standard input
input_data = input()

# Process the input
print(input_data)
