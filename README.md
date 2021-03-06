Write a python script that can encrypt and decrypt the contents of a given file.

Encrypt:
To encrypt a file, replace any existing alphabetic character with another alphabetic character.  The character to replace is determined by calculating the number of occurrences of each character in the file, and replacing the most commonly occurring character with ‘a’, the second most commonly occurring character with ‘b’, the third most commonly occurring character with ‘c’, and so forth.

In the case where multiple characters occur the same number of times, use alphabetic precedence.  In other words, the earlier alphabetic character should be replaced with the next alphabetic character in ‘abc…’.

For example, a file with the contents ‘acadian asset management’ will be encrypted as ‘agahjac aeebf dacaibdbcf’.  In the original text, the characters, first ordered from most to least number occurrences, then ordered alphabetically, are [‘a’, ‘e’, ’n’, ‘m’, ‘s’, ‘t’, ‘c’, ‘d’ ‘g’, ‘i’].  The number of occurrences are [6, 3, 3, 2, 2, 2, 1, 1, 1, 1].  The replacement characters are [‘a, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’].

Assumptions:
The file is in ASCII format
The file does not contain any upper-case letters
The file may contain numbers and punctuation.  For these cases, simple leave the character as it is.

The encryption script should be called in the following format

problem.py encrypt original.txt encrypted.txt decoder.txt

original.txt contains the text to be encrypted.  encrypted.txt is the name of a file where the encrypted text should be written.  decoder.txt is the name of a file where the decoder key should be written.  In the above example, decoder.txt would contain:

a,6,a
e,3,b
n,3,c
m,2,d
s,2,e
t,2,f
c,1,g
d,1,h
g,1,i
i,1,j

Decrypt:
The process to decrypt a file is the reverse of the process to encrypt a file.  Given a file with encrypted characters, as well as a decoder file, convert the encrypted text to the original text.

The decryption script should be called in the following format:

problem.py decrypt encrypted.txt decrypted.txt decoder.txt

encrypted.txt is a file with the encrypted characters, equal to ‘agahjac aeebf dacaibdbcf’ in the earlier example.  decrypted.txt is a file with the decrypted results.  decoder.txt follows the same format and contents as the decoder.txt from the encryption process.


