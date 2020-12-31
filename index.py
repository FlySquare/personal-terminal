import os


def figlet():
    print(" ")
    print("db    db .88b  d88. db    db d888888b ")
    print("88    88 88'YbdP`88 88    88 `~~88~~' ")
    print("88    88 88  88  88 88    88    88    ")
    print("88    88 88  88  88 88    88    88    ")
    print("88b  d88 88  88  88 88b  d88    88    ")
    print("~Y8888P' YP  YP  YP ~Y8888P'    YP    ")
    print(" ")

def komutlar(var):

    if var=="xampp":
       os.system('sudo /opt/lampp/manager-linux-x64.run')
    
    
figlet()
x = input("umutcan@flysquare:~ ")
komutlar(x)
