import time
import replit
from colored import fore
replit.clear()
a="back"
b="Comando inesistente"
localtime = time.asctime( time.localtime(time.time()) )
print("         .--.")
print("    .-._;.--.;_.-.")
print("   (_.'_..--.._'._)")
print("    /.' . 60 . '.\"")
print("   // .      / . \\")
print("  |; .      /   . |;")
print("  ||45    ()    15||")
print("  |; .          . |;")
print("   \\ .        . //")
print("    \'._' 30 '_.'/")
print("     '-._'--'_.-'")
print("         `""` ")
print("")
print("Orologio, ora e data in tempo reale      Versione 1.1.0")
print("")
time.sleep(2)

print("Ora e data correnti :", fore.GREEN+localtime+fore.WHITE)
time.sleep(1)
x=input("Scrivi back per tornare indietro: ")

if x==a:
  replit.clear()
  print("Ritorno alle applicazioni...")
  time.sleep(1.2)
  replit.clear()
  exec(open("apps.py").read())
else:
  print(fore.RED+b+fore.WHITE)
  time.sleep(2)
  replit.clear()
  exec(open("orologio.py").read())