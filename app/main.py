from app.decrypt import Decryptor
from app.encrypt import Encryptor


class FileAdapter:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, "rb") as file:
            data = file.read()
        return data


if __name__ == '__main__':
    file_input = FileAdapter('../data/frame.png')
    decrypted_file = '../data/decrypted.png'
    plaintext_key = 'abacadabra'

    encryption_key = Encryptor(plaintext_key)
    decryption_key = Decryptor(plaintext_key)

    encrypted_data = encryption_key.encrypt(file_input)
    decrypted_data = decryption_key.decrypt(encrypted_data)

    with open(decrypted_file, "wb") as f:
        f.write(decrypted_data)
