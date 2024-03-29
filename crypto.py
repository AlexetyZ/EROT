from cryptography.fernet import Fernet
import os

import config


class Crypto:

    def __init__(self):
        '''
            Если ты жулик - ухади!
        '''
        self.key_path = config.key_path

    def get_cifer_key(self):
        if os.path.exists(self.key_path):
            with open(self.key_path, 'rb') as f:
                cifer_key = f.read()
            return cifer_key
        else:
            cifer_key = Fernet.generate_key()
            with open(self.key_path, 'wb') as f:
                f.write(cifer_key)
            return cifer_key

    def get_hash_password(self, hashed_p_path: str = '', password: bytes = b'1234567890', key_gen: bool = False):
        if key_gen is False:
            cifer_key = self.get_cifer_key()
        else:
            cifer_key = self.get_cifer_key()
        cifer = Fernet(cifer_key)
        hashed_pass = cifer.encrypt(password)
        return hashed_pass

    def write_hashed_password(self):
        hashed_pass = self.get_hash_password()
        with open('password.key', 'wb') as f:
            f.write(hashed_pass)
        return hashed_pass


    def unpack_password(self, hashed_pass: str or bytes):
        cifer_key = self.get_cifer_key()
        cifer = Fernet(cifer_key)
        decrypt_pass = cifer.decrypt(hashed_pass)
        return decrypt_pass.decode('utf-8')


if __name__ == '__main__':
    result = Crypto().unpack_password(config.Zaitsev_knd['password'])


    # result = Crypto().get_hash_password(password=b'pass')
    print(result)
