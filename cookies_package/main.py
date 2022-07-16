import os, ctypes, sys, base64, random
from Crypto.Cipher import AES
from Crypto import Random
from time import sleep


'''
MODULES SECTION
'''

def obfuscate_code(fileName):
    if fileName.endswith('.py'):
        IV = Random.new().read(AES.block_size)                       # Generate random IV
        key = u''
        for i in range(8):
            key = key + chr(random.randint(0x4E00, 0x9FA5))          # Generate random key

        with open(f'{fileName}.py') as f:                    # Open file and fix imports
            _file = f.read()
            imports = ''
            input_file = _file.splitlines()
            for i in input_file:
                if i.startswith("import") or i.startswith("from"):
                    imports += i+';'

        with open(f'{fileName}.py', "wb") as f:              # Write file with fixed imports & AES encrypted
            encodedBytes = base64.b64encode(_file.encode())
            obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
            f.write(f'from Crypto.Cipher import AES;{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())
    else:
        print('File is not a python file failed to obfuscate')



'''
COMMANDS SECTION
'''

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


def curl_download_github(file_location_with_extention, github_token, url):
    '''
    Download file from github using curl
    
    Syntax = "main.py, github_token, raw.githubusercontent.com/Callumgm/test/master/main.py"
    '''
    os.system(f'curl -s -o {file_location_with_extention} https://{github_token}@{url}')


def curl_download(file_location_with_extention, url):
    '''
    Download file using curl
    
    Syntax = "main.py, URL"
    '''
    os.system(f'curl -s -o {file_location_with_extention} {url}')


def obfusacate(fileName):
    '''
    obfuscate file code before compiling
    
    Syntax = "C:\Users\Dick\Desktop\main.py"
    '''
    obfuscate_code(fileName)

