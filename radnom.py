import random
from re import X
from telnetlib import STATUS
import requests
import random
import string
import sys


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string

url_joxi= "http://joxi.net/"
for i in range(1,100000):
        with open('spisok.txt', 'a') as f:
            print(url_joxi+ generate_alphanum_random_string(14) ,file=f)


            
            

