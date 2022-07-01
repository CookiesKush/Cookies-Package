import os, ctypes, sys
from util.loading_animation import *
from util.obfuscate import *
from time import sleep

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


def obfusacate(fileName):
    '''
    obfuscate file code before compiling from temp folder
    
    Syntax = "main.py"
    '''
    animate_loading(lambda: obfuscate_code(fileName))()
    