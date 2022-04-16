import replit
import time
from colored import fore
#comandi
a="apps"
c="help"
d="shutdown"
b="Comando inesistente."
#code
replit.clear()
print(fore.GREEN+"                                 _ _  ____   _____   ____  ")
print("                                | (_)/ __ \ / ____| |___ \ ")
print("   __ _ _ __ _ __ ___   __ _  __| |_| |  | | (___     __) |")
print("  / _` | '__| '_ ` _ \ / _` |/ _` | | |  | |\___ \   |__ < ")
print(" | (_| | |  | | | | | | (_| | (_| | | |__| |____) |  ___) |")
print("  \__,_|_|  |_| |_| |_|\__,_|\__,_|_|\____/|_____/  |____/ "+fore.WHITE)
print("")
print("")
print("armadiOS 3 0.4.1")
print("© Enrico Fracasso 2022")
print("")
x=input(fore.WHITE+"Inserisci un comando: ")

if x==a:
  print("Sto caricando le applicazioni...")
  time.sleep(1.2)
  replit.clear()
  exec(open("apps.py").read())
elif x==c:
  print(fore.BLUE+"Comandi disponibili:",a,",",c,",",d,"."+fore.WHITE)
  time.sleep(3)
  exec(open("sistema.py").read())
elif x==d:
  replit.clear()
  print("Spegnimento...")
  time.sleep(2)
  replit.clear()
else:
  print(fore.RED+b+fore.WHITE)
  time.sleep(2)
  replit.clear()
  exec(open("sistema.py").read())