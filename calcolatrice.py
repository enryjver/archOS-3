import time
import replit
from colored import fore
replit.clear()
print("                          /\                     ")
print("     __                  / /   /\|\/\     ______ ")
print("  __|  |___   ______    / /   _)    (__  /_____/ ")
print("/__    __/  /_____/   / /    \_     _/  /_____/")
print("    |__|              / /       )    \          ")
print("                      \/        \/\|\/    ")
print("")
print(fore.YELLOW+"Calcolatrice"+fore.WHITE+"      Versione 1.0.1")
time.sleep(2)
# addizione
def add(x, y):
    return x + y

# sottrazione
def subtract(x, y):
    return x - y

# moltiplicazione
def multiply(x, y):
    return x * y

# disivisone
def divide(x, y):
    return x / y


print("Seleziona l'operazione che desideri.")
print("1.Addizione")
print("2.Sottrazione")
print("3.Moltiplicazione")
print("4.Divisione")
print("9.Informazioni")
print("0.Esci")

while True:
    # input
    choice = input("Inserisci l'opzione desiderata(1/2/3/4/9/0): ")

    # controllo opzione
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Inserisci il primo operatore: "))
        num2 = float(input("Inserisci il secondo operatore: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            if num2==0:
              print(fore.RED+"Impossibile dividere per 0."+fore.WHITE)
            else:
              print(num1, "/", num2, "=", divide(num1, num2))
    if choice in ('9', '0'):
        if choice=='9':
          print(fore.GREEN+"Calcolatrice, versione 1.0.1")
          print("© Enrico Fracasso 2022"+fore.WHITE)
          
        elif choice=='0':
          replit.clear()
          print("Ritorno alle applicazioni...")
          time.sleep(2)
          replit.clear()
          exec(open("apps.py").read())
      
    elif choice not in ('1','2','3','4','9','0'):
        print(fore.RED+"Comando inesistente"+fore.WHITE)
        time.sleep(2)