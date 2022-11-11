import time
import replit
from colored import fore
#apps
a = "1"
b = "2"
d = "3"
e = "I"
f = "i"
g = "S"
h = "s"
i = "4"
c = "Please choose a valid option."
print("Available apps:")
time.sleep(0.5)
print("1.Calculator")
time.sleep(0.3)
print("2.OpenWriter")
time.sleep(0.2)
print("3.Clock")
time.sleep(0.1)
print("4.archCrypter")
time.sleep(0.2)
print(fore.RED + "I.Back")
time.sleep(0.1)
print("S.Shutdown" + fore.WHITE)
time.sleep(0.4)
x = input("Choose an option: ")

if x == a:
    replit.clear()
    print("Booting up Calculator...")
    time.sleep(2)
    exec(open("calcolatrice.py").read())
elif x == b:
    replit.clear()
    print("Booting up Openwriter...")
    time.sleep(2)
    exec(open("openwriter.py").read())
elif x == d:
    replit.clear()
    print("Booting up Clock...")
    time.sleep(2)
    exec(open("orologio.py").read())
elif x == i:
    replit.clear()
    print("Booting up archCrypter...")
    time.sleep(2)
    exec(open("archcrypter.py").read())
elif x == e or x == f:
    replit.clear()
    print("Returning to system menu...")
    time.sleep(2)
    exec(open("sistema.py").read())
elif x == g or x == h:
    replit.clear()
    print("Shutting down...")
    time.sleep(2)
    replit.clear()
else:
    print(fore.RED + c + fore.WHITE)
    time.sleep(2.0)
    replit.clear()
    exec(open("apps.py").read())
