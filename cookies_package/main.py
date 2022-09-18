
# System Modules
import os
import ctypes
import sys
import base64
import random
import platform

from time import sleep


# Downloaded Modules
from Crypto.Cipher import AES
from Crypto import Random


def clear():
    '''
        Clear console

        Syntax:
            :py:class:`clear()`
    '''
    if platform.system() == 'Windows': 
        os.system('cls')

    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    

def setTitle(title:str):
    '''
        Set console title

        Arguments:
            title   : str

        Syntax:
            :py:class:`setTitle("Hello, World")`
    '''
    ctypes.windll.kernel32.SetConsoleTitleW(f"{title}")


def slowPrint(text:str, speed:int):
    '''
        Print text letter by letter with a delay

        Arguments:
            text    : str
            speed   : int

        Syntax:
            :py:class:`slowPrint("Hello World", 0.04)`
    '''
    for letter in text: sys.stdout.write(letter) ; sys.stdout.flush() ; sleep(speed)


def curl_download_github(output:str, token:str, url:str):
    '''
        Download file from github to system using curl

        Arguments:
            output  : str   - path to download file to
            token   : str   - private github token
            url     : str   - raw github url to download file from

        Syntax:
            :py:class:`curl_download_github("main.py", TOKEN, "raw.githubusercontent.com/Callumgm/test/master/main.py")`
    '''

    if "https://" in url: url = url.replace("https://", "") # Remove https:// from url if found

    os.system(f'curl -s -o {output} https://{token}@{url}')


def curl_download(output:str, url:str):
    '''
        Download file to system using curl

        Arguments:
            output  : str   - path to download file to
            url     : str   - url to download file from

        Syntax:
            :py:class:`curl_download("main.py", url)`
    '''
    os.system(f'curl -s -o {output} {url}')


def obfusacate(file:str):
    '''
        Obfuscate source code

        Arguments:
            file    : str   - path to file to obfuscate
            speed   : int

        Syntax:
            :py:class:`obfusacate("main.py")`
    '''
    if file.endswith('.py'): 
        # Initialise variables                        
        IV  = Random.new().read(AES.block_size)
        key = u''

        # Generate random key
        for i in range(8): key += chr(random.randint(0x4E00, 0x9FA5))  

        # Open file and fix imports
        with open(f'{file}') as f:                  
            _file = f.read()
            imports = ''
            input_file = _file.splitlines()
            for i in input_file:
                if i.startswith("import") or i.startswith("from"): imports += i+';'

        # Write file with fixed imports & AES encrypted code
        with open(f'{file}', "wb") as f:              
            encodedBytes = base64.b64encode(_file.encode())
            obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
            f.write(f'from Crypto.Cipher import AES;{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())
    
    else: print('File is not a python file failed to obfuscate')