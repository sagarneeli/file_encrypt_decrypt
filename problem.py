#! /usr/bin/env python3

import sys
from Encryptor import Encryptor

def main(argument_list):
    mode, input_file, output_file, decoder_file = '', '', '', ''

    try:
        # Parsing argument
        # checking each argument
        mode = argument_list[0]
        input_file = argument_list[1]
        output_file = argument_list[2]
        decoder_file = argument_list[3]
    except:
        print('Verify if all the appropriate command line arguments are provided')
        sys.exit(2)

    encryptor = Encryptor()
    if mode == 'encrypt':
        encryptor.file_encrypt(input_file, output_file, decoder_file)
    elif mode == 'decrypt':
        encryptor.file_decrypt(input_file, output_file, decoder_file)
        

if __name__ == '__main__':
    # Remove 1st argument from the
    # list of command line arguments
    argument_list = sys.argv[1:]
    # Python program to demonstrate encryption/decryption
    main(argument_list)
