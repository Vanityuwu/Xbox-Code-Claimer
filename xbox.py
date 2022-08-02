from http.client import OK
import colorama
from colorama import Fore
from colorama import init as colorama_init
import requests
import random
import os

colorama_init(autoreset=True)
colors = list(vars(colorama.Fore).values())
colored_lines = [random.choice(colors)]

def finder():
    while True:
        f = open('tokens.txt','r')
        token = f.readline().splitlines()[0]
        f.close()
        url = 'https://discord.com/api/v9/users/@me/outbound-promotions/codes?locale=en-GB'#url
        headers = {
            'authorization': token,
        }
        try:
            response = requests.get(url, headers=headers).json()
            code = response[0]['code']
            with open('codes.txt', 'a') as the_file:
                the_file.write(code + '\n')
                the_file.close()
            print(Fore.RED +"Xbox Code Found -> " + code)
            with open('tokens.txt', 'r') as fin:
                data = fin.read().splitlines(True)
            with open('tokens.txt', 'w') as fout:
                fout.writelines(data[1:])
            fout.close()
        except KeyError:
            print(Fore.RED +"No Codes Found")
            with open('tokens.txt', 'r') as fin:
                data = fin.read().splitlines(True)
            with open('tokens.txt', 'w') as fout:
                fout.writelines(data[1:])
            fout.close()
        if os.stat('tokens.txt').st_size == 0:
            print(Fore.RED +"No Tokens Left")
            os.system('pause')
            break


    
finder()