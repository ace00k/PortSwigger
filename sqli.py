#!/usr/bin/python3

import pdb, sys, string, requests, 
from pwn import *


def def_handler():
    print("\nSaliendo.....")
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)

main_url = ""
characters = string.ascii_lovercase + string.digits 


def make_SQLi():



if __name__ == '__main__': 
    make_SQLi()
