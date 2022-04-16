import replit
from colored import fore
import time
#mess.errore
a="Comando non valido"
#comandi
d="shutdown"
e="login"
f="bypass"
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

account = None 

def login(): 
    global account
    replit.clear()
    user = str(input("Nome utente: ")) 
    passw = str(input("Password: "))
    if user=="bachecawii":
      print("cacca")
    if user in replit.db.keys():
        if replit.db[user]["password"] == passw: 
          print("Benvenuto,",user+", sto caricando il sistema...")
          account = replit.db.get(user)
          time.sleep(5)
          replit.clear()
          exec(open("sistema.py").read())
        else:
          print(fore.RED+"Password errata."+fore.WHITE)
          time.sleep(3)
          login()
    else:
      print(fore.RED+"Account inesistente."+fore.WHITE)
      time.sleep(3)
      login()

def signup():
    global account
    replit.clear()
    user = str(input("Nome utente: ")) 
    passw = str(input("Password: ")) 

    if user not in replit.db.keys(): 
        replit.db[user] = {
            "password": passw,
        }
        print(fore.GREEN+"Account creato con successo!"+fore.WHITE)
        time.sleep(2)
        account = replit.db.get(user)
        print("Benvenuto,",user+", sto caricando il sistema...")
        time.sleep(5)
        account = replit.db.get(user)
        replit.clear()
        exec(open("sistema.py").read())
    else:
        print(fore.RED+"Impossibile registrare: Account esistente."+fore.WHITE)
        time.sleep(3)
        signup()


ls = input("1.Login\n2.Registra nuovo utente\n\nScegli l'opzione desiderata: ")

if ls == "1":
  login()

elif ls=="2":
  signup()
elif ls==f:
  exec(open("quack.py").read())
else:
  print(fore.RED+"Scelta non valida."+fore.WHITE)
  time.sleep(3)
  replit.clear()
  exec(open("main.py").read())