#!/usr/bin/python3
#SHEBANG!

# Octal Decode Base8
# This script decodes a string of octal numbers (base 8) into their corresponding

# Since the user will enter a string like "o164 o141 o142 o154 o145", we need to remove the leading 'o'

import sys

import argparse

def octal_decode_base8(octal_string):
    # Split the input string into individual octal numbers
    octal_numbers = octal_string.split()
    

    # just for debugging
    print(f"Octal Numbers: {octal_string}")
    # Decode each octal number to its corresponding character
    decoded_characters = []
    for octal in octal_numbers:
        # Remove the leading 'o' if present
        if octal.startswith('o'):
            octal = octal[1:]
        # Convert octal to decimal, then to character
        decimal_value = int(octal, 8)
        decoded_characters.append(chr(decimal_value))
    
    # Join the characters to form the final decoded string
    decoded_string = ''.join(decoded_characters)
    return decoded_string

def octal_encode_base8(input_string, o_mode=False):
    # Encode each character to its corresponding octal number with optional leading 'o'
    octal_numbers = []
    for char in input_string:
        if o_mode:
            octal_value = oct(ord(char))[2:]  # Convert to octal and remove '0o' prefix
            octal_numbers.append('o' + octal_value)
        else:
            octal_value = oct(ord(char))[2:]  # Convert to octal and remove '0o' prefix
            octal_numbers.append(octal_value)

    result_string = ' '.join(octal_numbers)
    return result_string

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decode a string of octal numbers (base 8) into their corresponding characters.")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode the provided octal string.")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode a string into octal numbers (coming soon).")
    parser.add_argument("-o",  type=str, help="O mode: Add leading 'o' to octal numbers.", default=False)
    parser.add_argument("octal_string", type=str, help="A string of octal numbers separated by spaces (e.g., 'o164 o141 o142 o154 o145').")
    
    args = parser.parse_args()

    if args.encode:
        result = octal_encode_base8(args.octal_string, args.o)

        print(f"Encoded String: {result}")

    elif args.decode:
    
        
        result = octal_decode_base8(args.octal_string)
        print(f"Decoded String: {result}") 

