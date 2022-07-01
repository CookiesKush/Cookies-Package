import os, ctypes, sys, shutil, base64, random
from Crypto.Cipher import AES
from util.loading_animation import *
from Crypto import Random
from time import sleep


temp = os.getenv('TEMP')


def clear():
    '''
    Clear console
    '''
    os.system('cls')


def setTitle(str, creator):
    '''
    Set console title with creator name
    
    Syntax = "Hello World, CookiesKush420"
    '''
    ctypes.windll.kernel32.SetConsoleTitleW(f"{str} | {creator}")


def slowPrint(str, speed):
    '''
    Print text letter by letter
    
    Syntax = "Hello World, 0.04"
    '''
    for letter in str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(speed)


def curl_download(file_location_with_extention, github_token, url):
    '''
    Download file from github using curl
    
    Syntax = "main.py, token, raw.githubusercontent.com/Callumgm/test/master/main.py"
    '''
    animate_loading(lambda: os.system(f'curl -s -o {file_location_with_extention} https://{github_token}@{url}'))()


def obfuscate(fileName):
    '''
    obfuscate file code before compiling from temp folder
    
    Syntax = "main.py"
    '''
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