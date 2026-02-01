#!/bin/bash

# A simple decoder script that decodes a base64 encoded string passed as an argument

flag=$1

case $flag in
    --help|-h)
    echo "Humm... So you're looking for some help?"
    echo "--help or -h for calling me again"
    echo "--version or -v for seeing my version"
    echo "-d for decoding a string, followed by the type and the string itself"
    echo "-e for encoding a string, followed by the type and the string itself ( coming soon! )"
    echo "--auto for automatic decoding ( coming soon! )"
    echo " "
    echo "Example usage:"
    echo "$0 -d base64 \"SGVsbG9Xb3JsZAo=\""
    echo "Output: HelloWorld"

    echo "  "
    echo "Available types is base64, binary, hex ( or base16), url ( URL Decoding ), rot13 ( ROT13 )  and base8 ( or octal )"
    echo "Don't forgot to always use double quotes!"

    echo " "
    echo "auto decoding isin progress!"
    ;;

    --version|-v)
    echo "Version 0.1, keep going!"
    ;;

    -d)
    param=$2

    case $param in
        base64)
        string=$3
        echo "Oh, so you want me to decode a Base64 string! Here we go!"
        sleep 1
        echo " "
        echo "$3" | base64 -d
        echo " "
        echo "Bye!"
        ;;

        binary)
        string=$3
        echo "Wow, cool! So you want me to deocde a binary. Give me a second..."
        sleep 1
        echo " "
        echo "$3" | fold -w8 | while read byte; do printf "\\x$(printf '%x' $((2#$byte)))"; done; echo
        echo " "
        ;;
        octal|base8)
        string=$3
        echo "Base8? Unique! Let's decode this..." 
        sleep 1
        echo " "
        python3 octal_decode_base8.py -d "$3"
        echo " "
        ;;
        hex|base16)
        string=$3
        echo "Hexadecimal decoding coming right up!"
        sleep 1
        echo " "
        echo "$3" | xxd -r -p
        echo " "
        ;;
        url)
        string=$3
        echo "URL encoding.. UH, decoding... Please wait for a moment."
        sleep 1
        echo " "
        printf '%b' "${string//%/\\x}"
        echo " "
        ;;

        rot13)
        string=$3
        echo "ROT13, here we go!"
        sleep 1
        echo " "
        echo "$3" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
        echo " "
        ;;
        *)
        echo "NOT available or syntax error, please type $0 --help or $0 -h for help"
        ;;
    esac
    ;;
    -e)
    param=$2

    case $param in
        base64)
        string=$3
        echo "Oh, so you want me to encode a string into Base64! Here we go!"
        sleep 1
        echo " "
        echo "$3" | base64 
        echo " "
        echo "Bye!"
        ;;

        binary)
        string=$3
        echo "Wow, cool! So you want me to encode into binary. Give me a second..."
        sleep 1
        echo " "
        echo -n "$3" | xxd -b -c 1 | cut -c 10- | tr -d '\n'
        echo " "
        ;;
        octal|base8)
        string=$3
        echo "Base8? Unique! Let's encode this..." 
        sleep 1
        echo " "
        python3 octal_decode_base8.py -e "$3"
        echo " "
        ;;
        hex|base16)
        string=$3
        echo "Hexadecimal encoding coming right up!"
        sleep 1
        echo " "
        echo "$3" | xxd -p
        echo " "
        echo "Goodbye"
        ;;
        url)
        string=$3
        echo "URL encoding... Please wait for a moment."
        sleep 1
        echo " "
        python3 -c "from urllib.parse import quote; print(quote('$3'))"
        echo " "
        ;;

        rot13)
        string=$3
        echo "ROT13, here we go!"
        sleep 1
        echo " "
        echo "$3" | tr 'A-Za-z' 'N-ZA-Mn-za-m'

        echo " "
        ;;
        *)
        echo "NOT available or syntax error, please type $0 --help or $0 -h for help"
        ;;
    esac
    ;;
    --auto)
        echo "Auto decoding coming soon... Please always check for updates!"
        exit 0
        string=$2
        supported_types=("base64" "binary" "hex" "url" "rot13" "base8" "octal")
        for type in "${supported_types[@]}"; do
            echo "Trying $type..."
            # Progress!
            case $type in
                base64)
                    decoded=$(echo"$string" | base64 -d 2>/dev/null) 
                    if [[ $? -eq 0 ]]; then
                        echo "$decoded"
                        echo "Decoded as Base64"
                        exit 0
                    fi
                    ;;
                binary)
                    decoded=$(echo "$string" | fold -w8 | while read byte; do printf "\\x$(printf '%x' $((2#$byte)))"; done 2>/dev/null)
                    if [[ $? -eq 0 ]]; then
                        echo "$decoded"
                        echo "Decoded as Binary"
                        exit 0
                    fi
                    ;;
                hex)
                    decoded=$(echo "$string" | xxd -r -p 2>/dev/null)
                    if [[ $? -eq 0 ]]; then
                        echo "$decoded"
                        echo "Decoded as Hexadecimal"
                        exit 0
                    fi
                    ;;
                url)
                    decoded=$(printf '%b' "${string//%/\\x}" 2>/dev/null)
                    if [[ $? -eq 0 ]]; then
                        echo "$decoded"
                        echo "Decoded as URL"
                        exit 0
                    fi
                    ;;
                rot13)
                    decoded=$(echo "$string" | tr 'A-Za-z' 'N-ZA-Mn-za-m' 2>/dev/null)
                    if [[ $? -eq 0 ]]; then
                        echo "$decoded"
                        echo "Decoded as ROT13"
                        exit 0
                    fi
                    ;;
                base8|octal)
                    decoded=$(python3 octal_decode_base8.py "$string" 2>/dev/null)
                    if [[ $? -eq 0 ]]; then
                        echo "$decoded"
                        echo "Decoded as Base8/Octal"
                        exit 0
                    fi
                    ;;
            esac
        done
    ;;

    *)
        echo "NOT available or syntax error, please type $0 --help or $0 -h for help"
        ;;
esac