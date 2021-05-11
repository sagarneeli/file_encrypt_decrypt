# Steps to run the code.
- Make sure `python` and `pip` are installed and configured on your system. If not follow this article to set it up - https://realpython.com/installing-python/
- Navigate to the path on your local machine where this project is imported through the terminal of your system.
- Run the following command to install all the dependencies - `pip install -r requirements.txt`
- Run the following command to make the main python script executable - `chmod 755 problem.py`
- Add the text you want to encrypt in `original.txt` file.
- To encrypt the message in `original.txt` run the following command - `./problem.py encrypt original.txt encrypted.txt decoder.txt`
- To decrypt an encrypted message run the command - `./problem.py decrypt encrypted.txt decrypted.txt decoder.txt`
- Verify the output and enjoy encrypting and decrypting messages.