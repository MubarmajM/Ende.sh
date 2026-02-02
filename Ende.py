#!/usr/bin/bash

# A based on Python and more user-friendly wrapper script for the Ende.sh Bash Script.
# This script provides an easy-to-use interface for encoding and decoding various formats.

from UFO import print_color, print_alert, print_banner, input_color
import subprocess
import sys

def main():
    print_color("Welcome to Ende.py - A User-Friendly Wrapper for Ende.sh", "green")
    print_color("Please choose an option:", "yellow")
    print_color("1. Encode", "cyan")
    print_color("2. Decode", "cyan")
    choice = input_color("Enter your choice (1/2): ", "yellow")

    if choice == '1':
        print_color("You chose to Encode.", "green")
        print("\n\n")
        print_color("Which encoding type do you want to use?", "blue")
        print_color("1. Base64", "cyan")
        print_color("2. URL Encode", "cyan")
        print_color("3. Hex Encode", "cyan")
        print_color("4. ROT13 Encode", "cyan")
        print_color("5. binary Encode", "cyan")
        print_color("6. base 8 encode ( octal )", "cyan")
        encoding_choice = input_color("Enter your choice (1-6): ", "yellow")
        if encoding_choice not in ['1', '2', '3', '4', '5', '6']:
            print_color("Invalid encoding choice. Please run the script again.", "red")
            sys.exit(1)
        elif encoding_choice == '1':
            encoding_type = 'base64'
        elif encoding_choice == '2':
            encoding_type = 'url'
        elif encoding_choice == '3':
            encoding_type = 'hex'
        elif encoding_choice == '4':
            encoding_type = 'rot13'
        elif encoding_choice == '5':
            encoding_type = 'binary'
        elif encoding_choice == '6':
            encoding_type = 'octal'
        data = input_color("Enter the data to encode: ", "yellow")
        output=subprocess.run(['./Ende.sh', '-e',encoding_type, data])
        print_color(output.stdout, "green")
        print_color(f"Encoded data: {data}", "green") 
    elif choice == '2':
        print_color("You chose to Decode.", "green")
        print("\n\n")
        print_color("Which decoding type do you want to use?", "blue")
        print_color("1. Base64", "cyan")
        print_color("2. URL Decode", "cyan")
        print_color("3. Hex Decode", "cyan")
        print_color("4. ROT13 Decode", "cyan")
        print_color("5. binary Decode", "cyan")
        print_color("6. base 8 decode ( octal )", "cyan")
        decoding_choice = input_color("Enter your choice (1-6): ","yellow")
        if decoding_choice not in ['1', '2', '3', '4', '5', '6']:
            print_color("Invalid decoding choice. Please run the script again.", "red")
            sys.exit(1)
        elif decoding_choice == '1':
            decoding_type = 'base64'
        elif decoding_choice == '2':
            decoding_type = 'url'
        elif decoding_choice == '3':
            decoding_type = 'hex'
        elif decoding_choice == '4':
            decoding_type = 'rot13'
        elif decoding_choice == '5':
            decoding_type = 'binary'
        elif decoding_choice == '6':
            decoding_type = 'octal' 
        data = input_color("Enter the data to decode: ", "yellow")
        output=subprocess.run(['./Ende.sh', '-d',decoding_type, data])
        print_color(output.stdout, "green")
        print_color(f"Decoded data: {data}", "green")  
    else:
        print_color("Invalid choice. Please run the script again.", "red")



if __name__ == "__main__":
    main()