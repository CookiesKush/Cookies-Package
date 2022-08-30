import os, ctypes, sys, base64, random
from Crypto.Cipher import AES
from Crypto import Random
from time import sleep


'''
COMMANDS SECTION
'''

def clear():
    '''
    Clear console
    '''
    os.system('cls')


def setTitle(str:str):
    '''
    Set console title

    str     - title to set
    
    Syntax = "Hello World"
    '''
    ctypes.windll.kernel32.SetConsoleTitleW(f"{str}")


def slowPrint(str:str, speed:int):
    '''
    Print text letter by letter with a delay

    str     - text to print
    speed   - delay between letters
    
    Syntax = "Hello World, 0.04"
    '''
    for letter in str: sys.stdout.write(letter) ; sys.stdout.flush() ; sleep(speed)


def curl_download_github(file:str, github_token:str, url:str):
    '''
    Download file from github to system using curl

    file    - path to download file to
    url     - raw github url to download file from
    
    Syntax = "main.py, github_token, raw.githubusercontent.com/Callumgm/test/master/main.py"
    '''
    if "https://" in url: url = url.replace("https://", "") # Remove https:// from url if found

    os.system(f'curl -s -o {file} https://{github_token}@{url}')


def curl_download(file:str, url:str):
    '''
    Download file to system using curl

    file    - path to download file to
    url     - url to download file from
    
    Syntax = "main.py, URL"
    '''
    os.system(f'curl -s -o {file} {url}')


def obfusacate(file:str):
    '''
    Obfuscate source code file

    file    - path to file to obfuscate
    
    Syntax = "main.py"
    '''
    if file.endswith('.py'):                         # Check if file is a python file
        IV  = Random.new().read(AES.block_size)          # Generate random IV
        key = u''

        for i in range(8): key += chr(random.randint(0x4E00, 0x9FA5))  # Generate random key

        with open(f'{file}') as f:                  # Open file and fix imports
            _file = f.read()
            imports = ''
            input_file = _file.splitlines()
            for i in input_file:
                if i.startswith("import") or i.startswith("from"): imports += i+';'

        with open(f'{file}', "wb") as f:              # Write file with fixed imports & AES encrypted
            encodedBytes = base64.b64encode(_file.encode())
            obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
            f.write(f'from Crypto.Cipher import AES;{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())
    
    else: print('File is not a python file failed to obfuscate')