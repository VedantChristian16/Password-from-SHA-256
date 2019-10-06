'''
Created by Vedant Christian
Created on 06 / 10 / 2019
'''

from urllib.request import urlopen, hashlib
import time

SHA512Hash = input("Please input the hash to crack.\n>")
HashedSHA = hashlib.sha512(bytes(SHA512Hash, 'utf-8')).hexdigest()

LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    hashedGuess = hashlib.sha512(bytes(guess, 'utf-8')).hexdigest()

    if hashedGuess == HashedSHA:
        print("The password is ", str(guess))
        time.sleep(5)

    elif hashedGuess != HashedSHA:
        print("Password guess ",str(guess)," does not match, trying next...")

print("Password not in database, we'll get them next time.")
time.sleep(5)
inp1 = input("Do you want to continue searching in a different database? (y/n)")
print("Locating Database...")
time.sleep(5)
print("Found Database...")
time.sleep(2)
print("Searching Database...")
time.sleep(1)

if inp1 == "y":
    with open("rockyou.txt", "r") as a:
        for line in a:
            line = line.rstrip("\n")
            b = hashlib.sha512((line).encode('utf-8'))
            print("\n")
            print(b.hexdigest())
            
            if (b.hexdigest()) == SHA512Hash:
                print("\nThe password is", line)
                break

            if (b.hexdigest()) != SHA512Hash:
                print("Password guess ", str(b), " does not match, trying next...")
