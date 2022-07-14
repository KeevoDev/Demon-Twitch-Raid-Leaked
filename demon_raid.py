import requests, json
import multiprocessing.dummy as ThreadPool
from colorama import Fore, Back, Style
import twitch
title = f"{Fore.RED}\n____  _____ _      ____  _     \n/  _ \\/  __// \\__/|/  _ \\/ \\  /|\n| | \\||  \\  | |\\/||| / \\|| |\\ ||\n| |_/||  /_ | |  ||| \\_/|| | \\||\n\\____/\\____\\_/  \\|\\____/\\_/  \\|\n{Back.WHITE}Twitch Raid Bot{Back.RESET}\n{Fore.RESET}                               \n"
print(title)
helix = twitch.Helix('o5xk7ctiue882kqp0ij71rmtkh3go7', 'o3uzx7ii8v0yoabeye2ii22r5dnwd5')

def sub(token):
    global target_id
    headers = {'Accept':'application/json',  'Content-Type':'application/json; charset=utf-8', 
     'User-Agent':'okhttp/4.2.2', 
     'Client-ID':'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 
     'Authorization':'OAuth ' + token, 
     'X-Device-ID':'422670681a2043abbbdf8c3beddf111e'}
    data = {'operationName':'JoinRaid', 
     'variables':{'input': {'raidID': target_id}},  'extensions':{'persistedQuery': {'version':1,  'sha256Hash':'c6a332a86d1087fbbb1a8623aa01bd1313d2386e7c63be60fdb2d1901f01a4ae'}}}
    print(requests.post('https://gql.twitch.tv/gql', headers=headers, data=(json.dumps(data))).text)


toekn = input(f"[{Fore.RED}+{Fore.RESET}] Enter Token Path: ")
tokens = open((f"{toekn}"), 'r').read().split('\n')
target_id = input(f"[{Fore.RED}+{Fore.RESET}] raid id: ")
print('raidbot started.')
pool = ThreadPool(300)
results = pool.map(sub, tokens)
pool.close()
pool.join()
print('success.')
