# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the same row
    for col in range(size):
        print("*", end="")
    # Print a newline character after each row
    print()
    row += 1
