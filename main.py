import replit
from colored import fore
import time
#mess.errore
a = "Invalid command"
#comandi
d = "shutdown"
e = "login"
f = "bypass"
print(fore.GREEN +"                 _      ____   _____   ____   ")
print("                | |    / __ \ / ____| |___ \  ")
print("   __ _ _ __ ___| |__ | |  | | (___     __) | ")
print("  / _` | '__/ __| '_ \| |  | |\___ \   |__ <  ")
print(" | (_| | | | (__| | | | |__| |____) |  ___) | ")
print("  \__,_|_|  \___|_| |_|\____/|_____/  |____/  " +fore.WHITE)
print("")
print("")
print("archOS 3 0.4.8")
print("© Enrico Fracasso 2022")
print("")

account = None


def login():
    global account
    replit.clear()
    user = str(input("Username: "))
    passw = str(input("Password: "))
    if user == "bachecawii":
        print("cacca [easteregg]")
    if user in replit.db.keys():
        if replit.db[user]["password"] == passw:
            print("Welcome,", user + ", please wait while i'm loading the system for you...")
            account = replit.db.get(user)
            time.sleep(5)
            replit.clear()
            exec(open("sistema.py").read())
        else:
            print(fore.RED + "Wrong password." + fore.WHITE)
            time.sleep(3)
            login()
    else:
        print(fore.RED + "This user does not exist." + fore.WHITE)
        time.sleep(3)
        login()


def signup():
    global account
    replit.clear()
    user = str(input("Username: "))
    passw = str(input("Password: "))

    if user not in replit.db.keys():
        replit.db[user] = {
            "password": passw,
        }
        print(fore.GREEN + "Your account was successfully created!" + fore.WHITE)
        time.sleep(2)
        account = replit.db.get(user)
        print("Welcome,", user + ", please wait while i'm loading the system for you...")
        time.sleep(5)
        account = replit.db.get(user)
        replit.clear()
        exec(open("sistema.py").read())
    else:
        print(fore.RED + "Cannot sign-up. Account already exists." +
              fore.WHITE)
        time.sleep(3)
        signup()


ls = input("1.Login\n2.Sign-up\n\nChoose an option: ")

if ls == "1":
    login()

elif ls == "2":
    signup()
elif ls == f:
    exec(open("orologio.py").read())
else:
    print(fore.RED + "Please choose a valid option." + fore.WHITE)
    time.sleep(3)
    replit.clear()
    exec(open("main.py").read())
