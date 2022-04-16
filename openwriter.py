import time
import replit
from colored import fore
import glob

a="a"
b="w"
c="r"
d="0"
e="l"

replit.clear()

print(fore.BLUE+"   ____               __          __   _ _            ")
print("  / __ \              \ \        / /  (_) |           ")
print(" | |  | |_ __   ___ _ _\ \  /\  / / __ _| |_ ___ _ __ ")
print(" | |  | | '_ \ / _ \ '_ \ \/  \/ / '__| | __/ _ \ '__|")
print(" | |__| | |_) |  __/ | | \  /\  /| |  | | ||  __/ |   ")
print("  \____/| .__/ \___|_| |_|\/  \/ |_|  |_|\__\___|_|   ")
print("        | |                                           ")
print("        |_|                                           "+fore.WHITE)

time.sleep(2)
print("")
print("OpenWriter 1.4.7      © Enrico Fracasso 2022")
print("")
time.sleep(1.5)

print("Che cosa desideri fare?: ")
print("")

print("a.Aprire un documento esistente")
print("w.Crerare un nuovo documento")
print("r.Aprire un documento esistente in modalità sola lettura")
print("l.vedere una lista di documenti salvati")
print("0.Esci da OpenWriter")
print("")
x=input("Inserisci un comando: ")

if x==a:
  y=input("Quale documento desideri aprire?: ")
  print("Apro il documento...")
  time.sleep(1)
  replit.clear()
  print(y,"- Modalità scrittura.  \nPer salvare e chiudere il documento, premi invio.")
  print("")
  f = open(y, 'r')
  file_contents = f.read()
  print (file_contents)
  z = input()
  text_file = open(y, x)
  text_file.write("\n")
  text_file.write(z)
  text_file.close()
  time.sleep(2)
  replit.clear()
  exec(open("openwriter.py").read())
  
elif x==b:
  y=input("Inserisci il nome del tuo nuovo documento: ")
  print("Creo il documento...")
  time.sleep(2)
  my_data_file = open(y, "w")
  print("Documento creato!")
  time.sleep(1)
  replit.clear()
  print(y,"- Modalità scrittura.  \nPer salvare e chiudere il documento, premi invio.")
  print("")
  z = input()
  text_file = open(y, x)
  text_file.write(z)
  text_file.close()
  time.sleep(2)
  replit.clear()
  exec(open("openwriter.py").read())
elif x==c:
  y=input("Quale documento desideri aprire?: ")
  print("Apro il documento...")
  time.sleep(1)
  replit.clear()
  print(y,"- Modalità lettura.  \nPer salvare e chiudere il documento, premi invio.")
  print("")
  f = open(y, 'r')
  file_contents = f.read()
  print (file_contents)
  input()
  f.close()
  time.sleep(2)
  exec(open("openwriter.py").read())
elif x==d:
  replit.clear()
  print("Ritorno alle applicazioni...")
  time.sleep(1.2)
  replit.clear()
  exec(open("apps.py").read())
elif x==e:
  print(fore.BLUE+"Ci sto ancora lavorando..."+fore.WHITE)
  #mylist = [f for f in glob.glob("*.txt")]
  #print("\nPremi invio per tornare indietro")
  #input()
  time.sleep(2)
  replit.clear()
  exec(open("openwriter.py").read())
else:
  print(fore.RED+"Comando inesistente"+fore.WHITE)
  time.sleep(2)
  replit.clear()
  exec(open("openwriter.py").read())