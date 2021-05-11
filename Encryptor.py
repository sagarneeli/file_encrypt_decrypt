import string
from collections import Counter
import csv

class Encryptor:
    def __init__(self) -> None:
        super().__init__()

    def file_encrypt(self, input_file, output_file, decoder_file):
        # Step 1 - Read the contents of the file.
        with open(input_file, 'r') as file:
            orignal_text = file.read()
        # Step 2 - Filter the text, so that we ignore numbers and punctuation
        filtered_text = self._filter_string(orignal_text)
        # Step 3 - Create a hashmap which contatins the characters, 
        #          first ordered from most to least number occurrences, 
        #          then ordered alphabetically,
        character_occurences = Counter(sorted(filtered_text)).most_common()
        # Step 4 - Process
        final_map, decoder_key_list = self._process_text(character_occurences)
        # Step 5 - Generate the final encrypted text
        final_result = self._generate_final_output(orignal_text, final_map)
        # Step 6 - Write the encrypted text to the output file
        with open (output_file, 'w') as file:
            file.write(final_result)
        # Step 7 - Write the encrypted key to the decoder file
        with open(decoder_file, 'w', newline='') as file:
            cw = csv.writer(file)
            cw.writerows(decoder_key_list)

    def file_decrypt(self, input_file, output_file, decoder_file):
        # Step 1 - Read the contents of the encrypted file.
        with open(input_file, 'r') as file:
            encrypted_text = file.read()
        # Step 2 - Read the contents of the decoder file and have it in a list
        with open(decoder_file) as f:
            decoder_key_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]
        # Step 3 - Create a mapping of the orignal character to the decrypted character
        decrypted_dict = {}
        for decoder_key in decoder_key_list:
            key, count, value = decoder_key
            decrypted_dict[value] = key
        # Step 4 - Generate the final decrypted text
        final_result = self._generate_final_output(encrypted_text, decrypted_dict)
        # Step 5 - Write the decrypted text to the output file.
        with open (output_file, 'w') as file:
            file.write(final_result)
    
    def _filter_string(self, input):
        output = ''
        for character in input:
            if character.isalpha():
                output += character
        return output

    def _process_text(self, character_occurences):
        # We will begin with the start character as 'a'. 
        # Since we are replacing the most commonly occurring character with ‘a’, 
        # the second most commonly occurring character with ‘b’, 
        # the third most commonly occurring character with ‘c’, and so forth.
        start_character_replace = 'a'
        # A list of tuples that holds the decoded keys
        decoder_key_list = []
        # A list of letters from a - z
        alpha_list = list(string.ascii_lowercase)
        index = 0
        # A hashmap that holds the mapping of characters to be replaced for the characters
        # in the orignal message
        encryption_map = {}
        while index < len(character_occurences):
            encryption_map[character_occurences[index][0]] = alpha_list[index]
            decoder_key_list.append((character_occurences[index] + (alpha_list[index], )))
            start_character_replace = chr(ord(start_character_replace) + 1)
            index += 1
        return encryption_map, decoder_key_list

    def _generate_final_output(self, orignal_text, final_map):
        final_result = ''
        for ch in orignal_text:
            if ch in final_map:
                final_result += final_map[ch]
            else:
                final_result += ch
        return final_result