import os
import subprocess
import sys
from datetime import datetime
import glob
import pygit2

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def komutlar(var):
    now = datetime.now()
    whereami = os.getcwd()
    if var=="clear":
        os.system('cls')
        index()
    elif var == "exit":
        exit = input(now.strftime("%H:%M:%S")+" | Çıkış yapmak istediğine emin misin? (E/H): ")
        if exit == "E" or exit == "e":
            print(now.strftime("%H:%M:%S")+" | Çıkış Yapıldı!")
            sys.exit()
    elif var=="ls":
        print("\n")
        for file in os.listdir():
            if(os.path.isdir(file)):
                print(style.BLUE + file+"/"+ style.WHITE)
            else:
                print(style.GREEN + file + style.WHITE)
        print("\n")
        index()
    elif var=="whereami":
        print(whereami)
        index()
    elif var.startswith("git clone"):
        words = var.split(' ')
        os.system(words[0]+" "+words[1]+" https://gitlab.com/epazarsoft/opencart/modules/"+words[2]+"/"+words[3])
        index()
    elif var.startswith("cd "):
        change = var.split(" ")
        os.chdir(change[1])
        index()
    else:
        os.system(var)
        index()

def index():
    whereami2 = os.getcwd()
    if(os.path.isdir(whereami2+"/.git")):
        repoBranch = style.CYAN+"("+pygit2.Repository('.').head.shorthand+") "+style.WHITE
    else:
        repoBranch = ""
    now2 = datetime.now()
    x = input(" "+now2.strftime("%H:%M:%S")+" | "+style.YELLOW+whereami2+style.WHITE+" ~ " + repoBranch +": ")
    komutlar(x)

os.system('cls')
print(style.WHITE)
index()
