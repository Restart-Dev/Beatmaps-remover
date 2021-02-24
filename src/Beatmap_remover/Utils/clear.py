import os


def clear():
    if os.name is 'nt':
        os.system('cls')
    else:
        os.system('clear')
