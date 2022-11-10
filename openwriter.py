import time
import replit
from colored import fore
import os
import glob

a = "a"
b = "w"
c = "r"
d = "0"
e = "l"

replit.clear()
print(fore.BLUE + "   ____               __          __   _ _            ")
print("  / __ \              \ \        / /  (_) |           ")
print(" | |  | |_ __   ___ _ _\ \  /\  / / __ _| |_ ___ _ __ ")
print(" | |  | | '_ \ / _ \ '_ \ \/  \/ / '__| | __/ _ \ '__|")
print(" | |__| | |_) |  __/ | | \  /\  /| |  | | ||  __/ |   ")
print("  \____/| .__/ \___|_| |_|\/  \/ |_|  |_|\__\___|_|   ")
print("        | |                                           ")
print("        |_|                                           " + fore.WHITE)

time.sleep(2)
print("")
print("OpenWriter 1.4.7      © Enrico Fracasso 2022")
print("")
time.sleep(1.5)

print("What are we doing today?: ")
print("")

print("a.Open an existing document")
print("w.Create a new document")
print("r.Open an existing document in reading mode")
print("l.See a list of all saved documents")
print("0.Quit Openwriter")
print("")
x = input("Choose an option: ")

if x == a:
    y = input("Wich document do you want to open?: ")
    print("Opening the document...")
    time.sleep(1)
    replit.clear()
    print(
        y,
        "- Editing mode.  \nTo save and close the document, press ENTER."
    )
    print("")
    f = open(y, 'r')
    file_contents = f.read()
    print(file_contents)
    z = input()
    text_file = open(y, x)
    text_file.write("\n")
    text_file.write(z)
    text_file.close()
    time.sleep(2)
    replit.clear()
    exec(open("openwriter.py").read())

elif x == b:
    y = input("Type the name of the new document: ")
    print("Creating the document...")
    time.sleep(2)
    my_data_file = open(y, "w")
    print("Created document!")
    time.sleep(1)
    replit.clear()
    print(
        y,
        "- Editing mode.  \nTo save and close the document, press ENTER."
    )
    print("")
    z = input()
    text_file = open(y, x)
    text_file.write(z)
    text_file.close()
    time.sleep(2)
    replit.clear()
    exec(open("openwriter.py").read())
elif x == c:
    y = input("Wich document do you want to open?: ")
    print("Opening the document...")
    time.sleep(1)
    replit.clear()
    print(
        y,
        "- Reading mode. No modifications will be saved.  \nTo close the document, press ENTER."
    )
    print("")
    f = open(y, 'r')
    file_contents = f.read()
    print(file_contents)
    input()
    f.close()
    time.sleep(2)
    exec(open("openwriter.py").read())
elif x == d:
    replit.clear()
    print("Returning to applications menu...")
    time.sleep(1.2)
    replit.clear()
    exec(open("apps.py").read())
elif x == e:
    print(fore.BLUE + "Still working on it ;)..." + fore.WHITE)
    #os.chdir(r'main')
    #my_files = glob.glob('*.txt')
    #print(my_files)
    #print("\nPremi invio per tornare indietro")
    #input()
    time.sleep(2)
    replit.clear()
    exec(open("openwriter.py").read())
else:
    print(fore.RED + "Please choose a valid option." + fore.WHITE)
    time.sleep(2)
    replit.clear()
    exec(open("openwriter.py").read())
