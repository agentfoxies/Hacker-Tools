import os
import time
import requests
import random

os.system("cls")
print("Welcome to anomymous bean-time utility. VERSION 3!!!11!")
pause = input("Press enter to continue... ")
os.system("cls")
print("Choose a option:")
print("1. Attack (DDOS)")
print("2. Defend (Firewall)")
print("3. SQL Injection")
print("4. Info from IP")
print("5. Track IP")
print("6. Password Cracker")
print("7. IP from Discord")
print("8. Bashir hacker")
print("9. Exit")
option = input("Option: ")
if option == "1":
    print("Enter the IP to attack:")
    ip = input("IP: ")
    os.system(f"ping {ip} -t")
elif option == "2":
    os.system(f"firewall")
elif option == "3":
    print("Enter the IP to attack:")
    ip = input("IP: ")
    print("Enter the SQL command:")
    sql = input("SQL: ")
    print("Select a SQL method")
    print("1. SQL1")
    print("2. SQL2")
    print("3. SQL3")
    method = input("Method: ")
    if method == "1":
        print("SQL1 method selected")
        print("Attacking... Please wait")
        time.sleep(10)
        print("SQL Injection done!")
    elif method == "2":
        print("SQL2 method selected")
        print("Attacking... Please wait")
        time.sleep(10)
        print("SQL Injection done!")
    elif method == "3":
        print("SQL3 method selected")
        print("Attacking... Please wait")
        time.sleep(10)
        print("SQL Injection done!")
elif option == "4":
    print("Enter the IP:")
    ip = input("IP: ")
    result = requests.get(f"https://ipinfo.io/{ip}")
    print(result.text)
elif option == "5":
    print("Enter the IP:")
    ip = input("IP: ")
    result = requests.get(f"https://ipinfo.io/{ip}")
    print(result.text)
elif option == "6":
    print("This utility can crack up to 6 digit passwords.")
    print("Enter the password to crack:")
    password = input("Password: ")
    if password.isnumeric() == False:
        print("Password must be numeric!")
        exit()
    passwordlength = len(password)
    n = 0
    while True:
        if n == 1000000:
            print("Password not found!")
            break
        if n == int(password):
            print(f"Password found! It is {n}")
            break
        n += 1
        print(n)
elif option == "7":
    print("Enter the discord ID:")
    discordid = input("Discord ID: ")
    if not discordid.isnumeric():
        print("Discord ID must be numeric!")
        exit()

    ip = discordid[:12]
    segments = [ip[:3], ip[3:6], ip[6:9], ip[9:]]

    # Adjust each segment to be less than 255 if necessary
    for i in range(len(segments)):
        segment = int(segments[i])
        while segment > 255:
            segment //= 10  # Remove the last digit to reduce the segment
        segments[i] = str(segment)

    ip = '.'.join(segments)
    print(f"IP: {ip}")

elif option == "8":
    os.system("cls")
    print("Hacking bashir...")
    time.sleep(10)
    print("Stealing all his money...")
    time.sleep(10)
    print("Hacking his computer...")
    time.sleep(10)
    print("Hacking his phone...")
    time.sleep(10)
    print("Hacking his life...")
    time.sleep(10)
    print("Hacking his family...")
    time.sleep(10)
    print("Hacking his friends...")
    time.sleep(10)
    print("Hacking his house...")
    time.sleep(10)
    print("Hacking his car...")
    time.sleep(10)
    print("Hacking his job...")
    time.sleep(10)
    print("Hacking his school...")
    time.sleep(10)
    print("Hacking his bank account...")
    time.sleep(10)
    print("Hacking his social media...")
    time.sleep(10)
    print("Hacking his email...")
    time.sleep(10)
    print("Hacking all his devices...")
    time.sleep(10)
    print("Hacking all his accounts..")
    time.sleep(10)
    print("Hacking all his passwords...")
    time.sleep(10)
    print("Hacking his life...")
    time.sleep(10)
    print("Done.")
    exit()
elif option == "9":
    exit()
else:
    print("Invalid option!")
    exit()