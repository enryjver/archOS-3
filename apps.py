import time
import replit
from colored import fore
#apps
a="1"
b="2"
d="3"
e="I"
f="i"
g="S"
h="s"
i="4"
c="App inesistente."
print("App disponibili:")
time.sleep(0.5)
print("1.Calcolatrice")
time.sleep(0.3)
print("2.OpenWriter")
time.sleep(0.2)
print("3.Orologio")
time.sleep(0.1)
print("4.Quack")
time.sleep(0.2)
print(fore.RED+"I.Indietro")
time.sleep(0.1)
print("S.Spegni"+fore.WHITE)
time.sleep(0.4)
x=input("Scegli quale app avviare: ")

if x==a:
  replit.clear()
  print("Avvio l'applicazione...")
  time.sleep(2)
  exec(open("calcolatrice.py").read())
elif x==b:
  replit.clear()
  print("Avvio l'applicazione...")
  time.sleep(2)
  exec(open("openwriter.py").read())
elif x==d:
  replit.clear()
  print("Avvio l'applicazione...")
  time.sleep(2)
  exec(open("orologio.py").read())
elif x==i:
  replit.clear()
  print("Avvio l'applicazione...")
  time.sleep(2)
  exec(open("quack.py").read())
elif x==e or x==f:
  replit.clear()
  print("Torno al menu di sistema...")
  time.sleep(2)
  exec(open("sistema.py").read())
elif x==g or x==h:
  replit.clear()
  print("Spegnimento...")
  time.sleep(2)
  replit.clear()
else:
  print(fore.RED+c+fore.WHITE)
  time.sleep(2.0)
  replit.clear()
  exec(open("apps.py").read())