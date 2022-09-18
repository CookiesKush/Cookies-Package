<h1 align="center">Welcome to cookies package 👋</h1>

<p align="center">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=Callumgm_Cookies_Package&metric=ncloc">
  <img src="https://img.shields.io/badge/version-1.5.1-blue.svg?cacheSeconds=2592000" >
  <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" >
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" >
  <img src="https://img.shields.io/github/last-commit/Callumgm/Cookies_Package">
  <a href="https://twitter.com/Flashouttt" target="_blank">
    <img src="https://img.shields.io/twitter/follow/Flashouttt.svg?style=social">
  </a>
</p>

> Python package for easier use of certin functions that I personally use alot

## 🚀 〢 Usage

```sh-session
pip install cookies_package
```

## 📃 〢 Documentation

```sh
Clear console

Syntax:
    clear()
```

```sh
Set console title

Arguments:
    title   : str

Syntax:
    setTitle("Hello, World")
```

```sh
Print text letter by letter with a delay

Arguments:
    text    : str
    speed   : int

Syntax:
    slowPrint("Hello World", 0.04)
```

```sh
Download file from github to system using curl

Arguments:
    output  : str   - path to download file to
    token   : str   - private github token
    url     : str   - raw github url to download file from

Syntax:
    curl_download_github("main.py", "TOKEN", "raw.githubusercontent.com/Callumgm/test/master/main.py")
```

```sh
Download file to system using curl

Arguments:
    output  : str   - path to download file to
    url     : str   - url to download file from

Syntax:
    curl_download("main.py", url)
```

```sh
Obfuscate src code

Arguments:
    file    : str   - path to file to obfuscate
    speed   : int

Syntax:
    obfusacate("main.py")
```

## 💭 〢 ChangeLog
```diff
v1.5.1 ⋮ 2022-09-18
+ more cleaning of code for easier reading/usage

v1.5.0 ⋮ 2022-08-30
+ cleaned up code and documentation
- removed creator section from set title
- removed backdoor script since it was broken

v1.4.7 ⋮ 2022-07-30
+ added simple backdoor script

v1.4.6 ⋮ 2022-07-16
+ added minor change

v1.3.3 ⋮ 2022-07-16
+ added normal curl download function
+ changed curl download via github name function
- removed obfusacate function to find file only from temp folder

v1.2.3 ⋮ 2022-07-01
+ fixed loading animation printing breaking

v1.2.2 ⋮ 2022-07-01
+ fixed shitty import errors
+ created sections
- removed seperate files and place all code into main.py

v1.2.1 ⋮ 2022-07-01
+ small hotfix

v1.1.3 ⋮ 2022-07-01
+ added loading antimation to obfusacate and curl commands
+ cleaned code
- removed obfuscate code from main into utils

v1.0.3 ⋮ 2022-07-01
+ added obfuscate code with random key
+ added download github code via curl
+ added loading animation

v0.0.1 ⋮ 2022-05-23
+ initial release
```

## 👤 〢 Author

 👤 **CookiesKush420**  
- Website: http://cookiesservices.xyz/  
- Twitter: [@Flashouttt](https://twitter.com/Flashouttt)  
- GitHub: [@Callumgm](https://github.com/Callumgm)    


## 🤝 〢 Contributing
Contributions, issues and feature requests are welcome!<br />Feel free to check
[issues page](https://github.com/Callumgm/Cookies_Package/issues).  


## 🌟 〢 Show your support
Give a ⭐️ if this project helped you! 


## 📝 〢 License
 Copyright © 2022
[CookiesKush420](https://github.com/Callumgm).<br />  This project is [MIT](https://github.com/Callumgm/Cookies_Package/blob/master/LICENCE) licensed. 
