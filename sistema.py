import replit
import time
from colored import fore, style
import random
#comandi
a = "apps"
c = "help"
d = "shutdown"
b = "Please choose a valid option."
#code
replit.clear()
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
#msg = [
#    'conti sfigato', 'hello daddy, uwu', 'mommy? sorry.', 'FESTAAAA?',
#    'perchè dire parole tante quando parole poche fare lavoro?',
#    'hello ur computerk has virus', 'borsellone', 'jamal'
#]

#print(fore.YELLOW + "Daily quote:" + fore.WHITE,"'"+ random.choice(msg)+"'")

x = input(fore.WHITE + "\nChoose an option (Type 'help' for help): ")

if x == a:
    print("Loading applications menu...")
    time.sleep(1.2)
    replit.clear()
    exec(open("apps.py").read())
elif x == c:
    print(fore.BLUE + "Available options:", a, ",", c, ",", d,
          "." + fore.WHITE)
    time.sleep(3)
    exec(open("sistema.py").read())
elif x == d:
    replit.clear()
    print("Shutting down...")
    time.sleep(2)
    replit.clear()
else:
    print(fore.RED + b + fore.WHITE)
    time.sleep(2)
    replit.clear()
    exec(open("sistema.py").read())
