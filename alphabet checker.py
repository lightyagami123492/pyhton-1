# Program to check if a given character is an alphabet using ASCII values

# Get input from the user
char = input("Enter a character: ")

# Check if it's a single character
if len(char) != 1:
    print("Please enter only a single character.")
else:
    # Get the ASCII value of the character
    ascii_value = ord(char)

    # Check if the ASCII value is in the range of uppercase or lowercase letters
    if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")