from cryptography.fernet import Fernet


class DataEncryptorDecryptor:

    encrypt_file='encrypted_texts.txt'
    decrypt_file='decrypted_texts.txt'
    key_file='encryption_key.key'

    def __init__(self,input_file,data):
        self.input_file=input_file
        with open(input_file,'a') as file:
            file.write(data)

    def genereate_key(self):
        return Fernet.generate_key()

    def save_key(self,key,key_file):
        with open(key_file,"wb") as file:
            file.write(key)

    def load_key(self,key_file):
        with open(key_file,"rb") as file:
            return file.read()

    def encrypted_file(self,input_file,output_file,key):
        with open(input_file,'rb') as file:
            data=file.read()

        fernet=Fernet(key)
        encrypted_data=fernet.encrypt(data)

        with open(output_file,'wb') as file:
            file.write(encrypted_data)
        print(f'{data_encrypter_decrypter.input_file} is encrypted in to {data_encrypter_decrypter.encrypt_file}')

    def decrypted_file(self,input_file,output_file,key):
        with open(input_file,'rb') as file:
            encrypted_data=file.read()

        fernet=Fernet(key)
        decrypted_data=fernet.decrypt(encrypted_data)

        with open(output_file,'wb') as file:
            file.write(decrypted_data)
        print(f'{data_encrypter_decrypter.encrypt_file} is decrypted in to {data_encrypter_decrypter.decrypt_file}')


if __name__=="__main__":

    data_encrypter_decrypter=DataEncryptorDecryptor("plain.txt","<enter your message>")
    key=data_encrypter_decrypter.genereate_key()
    data_encrypter_decrypter.save_key(key,data_encrypter_decrypter.key_file)


    data_encrypter_decrypter.encrypted_file(data_encrypter_decrypter.input_file,data_encrypter_decrypter.encrypt_file,key)

    data_encrypter_decrypter.decrypted_file(data_encrypter_decrypter.encrypt_file,data_encrypter_decrypter.decrypt_file, key)
