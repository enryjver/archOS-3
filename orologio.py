from datetime import datetime
import replit
from colored import fore
import calendar

replit.clear()
a = "back"
b = "Please choose a valid option."
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
print("         `" "` ")
print("")
print("Clock: real date and time       Version 1.2.0")
print("")
time.sleep(2)
x = datetime.now()
month = datetime.now().month
year = datetime.now().year
print(fore.BLUE+calendar.month(year, month)+fore.WHITE)
print("Current date and time :", fore.GREEN , x , fore.WHITE)
time.sleep(1)
xx = input("Type back to return to applications menu: ")

if xx == a:
    replit.clear()
    print("Returning to applications menu...")
    time.sleep(1.2)
    replit.clear()
    exec(open("apps.py").read())
else:
    print(fore.RED + b + fore.WHITE)
    time.sleep(2)
    replit.clear()
    exec(open("orologio.py").read())
