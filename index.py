import os
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def figlet():
    print(" ")
    print(bcolors.WARNING +"db    db .88b  d88. db    db d888888b "+bcolors.HEADER)
    print("88    88 88'YbdP`88 88    88 `~~88~~' "+bcolors.OKBLUE)
    print("88    88 88  88  88 88    88    88    "+bcolors.OKCYAN)
    print("88    88 88  88  88 88    88    88    "+bcolors.OKGREEN)
    print("88b  d88 88  88  88 88b  d88    88    "+bcolors.FAIL)
    print("~Y8888P' YP  YP  YP ~Y8888P'    YP    "+ bcolors.ENDC)
    print(" ")

def komutlar(var):

    if var=="xampp":
        os.system('sudo /opt/lampp/manager-linux-x64.run')
    elif var=="sil":
        os.system('clear')
        figlet()
        x = input(bcolors.WARNING +"umutcan@flysquare:~ "+bcolors.ENDC)
        komutlar(x)
    else:
        print(bcolors.FAIL+"Komut Yok!"+ bcolors.ENDC)
        x = input(bcolors.WARNING +"umutcan@flysquare:~ "+bcolors.ENDC)
        komutlar(x)

    
    
figlet()
x = input(bcolors.WARNING +"umutcan@flysquare:~ "+bcolors.ENDC)
komutlar(x)
