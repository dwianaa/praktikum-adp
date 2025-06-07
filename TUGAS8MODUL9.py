import os
import time
from termcolor import cprint, colored

def loading_screen():
    os.system('cls')  

    cprint("|=========================|", 'yellow')
    cprint("|    PUBG  M O B I L E    |", 'yellow', attrs=['bold'])
    cprint("|   >> BATTLEGROUND <<    |", 'yellow')
    cprint("|=========================|", 'yellow')
    print(colored("\nDeploying to battleground...", 'cyan'))

    panjang = 30
    for i in range(panjang + 1):
        isi = colored('-' * i, 'white', 'on_green')
        kosong = ' ' * (panjang - i)
        bar = isi + kosong
        persen = int((i / panjang) * 100)
        print(f"[{bar}] {persen}%", end='\r')
        time.sleep(0.08)

    print()
    time.sleep(1)
    cprint("✔ Welcome, Warrior! Prepare for battle!\n", 'red', attrs=['bold', 'underline'])

loading_screen()
