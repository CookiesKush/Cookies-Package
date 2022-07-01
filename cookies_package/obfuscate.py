
import os, shutil, base64, random
from Crypto.Cipher import AES
from util.loading_animation import *
from Crypto import Random

temp = os.getenv('TEMP')

def obfuscate_code(fileName):
    IV = Random.new().read(AES.block_size)                       # Generate random IV
    key = u''
    for i in range(8):
        key = key + chr(random.randint(0x4E00, 0x9FA5))          # Generate random key

    with open(f'{temp}\\{fileName}.py') as f:                    # Open file and fix imports
        _file = f.read()
        imports = ''
        input_file = _file.splitlines()
        for i in input_file:
            if i.startswith("import") or i.startswith("from"):
                imports += i+';'

    with open(f'{temp}\\{fileName}.py', "wb") as f:              # Write file with fixed imports & AES encrypted
        encodedBytes = base64.b64encode(_file.encode())
        obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
        f.write(f'from Crypto.Cipher import AES;{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())
    
    shutil.move(f"{temp}\\{fileName}.py", f"{os.getcwd()}\\{fileName}.py")  # Move file to main folder ready for compiling