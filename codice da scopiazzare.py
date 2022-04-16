import os
from colorama import Fore,Back,Style
import time, os, random, sys
from time import sleep
import requests

try:
  from googlesearch import search
except:
  os.system("pip install googlesearch-python")
  from googlesearch import search



# Variables
# Space variables *(Thanks @JBloves27 XD)
space = "                          "
space2 = "                     "
space3 = "                "
space4 = "              "
space5 = "            "
megaspace = "                                      "

abouts = f"""{space} {Fore.BLUE}A{Fore.RED}B{Fore.LIGHTYELLOW_EX}O{Fore.BLUE}U{Fore.LIGHTGREEN_EX}T"""

#logos
logo = f"{space}"+f"{Fore.BLUE}N{Fore.RED}O{Fore.LIGHTYELLOW_EX}T-{Fore.BLUE}G{Fore.RED}o{Fore.LIGHTYELLOW_EX}o{Fore.BLUE}g{Fore.LIGHTGREEN_EX}l{Fore.RED}e"

wikilogo = f"{space}"+f"🌐 Wikipedia"

udlogo = f"{space}"+f"📚 Urban Dictionary"

sugglogo = f"{space4}"+f"📧 Suggestion or Feedback"


# Functions
def clear():
  os.system("cls||clear")

def sp(str): # Thanks JBlove27 xD
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)
  print()

def home_page():
  clear()

  print(logo)

  print(space3+f"{Fore.WHITE}Type {Fore.RED}!about {Fore.WHITE}to know more.")
  print(space3+f"{Fore.WHITE}Type {Fore.RED}!wikipedia {Fore.WHITE}to go to Wikipedia.")
  print(space3+f"{Fore.WHITE}Type {Fore.RED}!ud {Fore.WHITE}to go to Urban Dictionary.")
  print(space3+f"{Fore.WHITE}Type {Fore.RED}!sugg {Fore.WHITE}to give a suggestion.")

  print(space4+f"🔍 Search:")

  searchq = input(f"{space3}{Fore.BLUE}>{Fore.LIGHTYELLOW_EX}>{Fore.RED}>{Fore.WHITE} ")

  clear()
  try:
    if searchq == '!about':
      about()
    elif searchq == "!wikipedia":
      wiki()
    elif searchq == "!sugg":
      sugg()
    elif searchq == "!ud":
      ud()
    else:
      try:
        search_bar = f"{Fore.WHITE}{space2}({searchq}{space4}|🔍)"
        print(logo)
        print(search_bar)
        s = searchq.replace(" ", "+")
        for res in search(s, lang='en', num_results=50):
          print(f"{Fore.YELLOW}> {Fore.LIGHTBLUE_EX}{res}\n")
        conf = input(f"{space3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
        if conf == 'y':
          home_page()
        elif conf == "n":
          home_page()
        else:
          return
      except:
        print(logo)
        print(search_bar)
        print(f"{Fore.RED} 404 ERROR")
        sleep(3)
        home_page()
  except:
    pass

def about():
  clear()
  print(abouts)

  sp(f"{Fore.WHITE}Made by {Fore.CYAN}iFreaku{Fore.WHITE}\nThis Project is inspired by {Fore.CYAN}@JBloves27{Fore.WHITE}'s {Fore.RED}Replol Project{Fore.WHITE}")

  sp(f"His Project URL: {Fore.LIGHTBLUE_EX}https://replit.com/@JBloves27/Replol{Fore.WHITE}")

  print(f"{space}{Fore.BLUE}F{Fore.RED}E{Fore.LIGHTYELLOW_EX}A{Fore.BLUE}T{Fore.LIGHTGREEN_EX}U{Fore.RED}R{Fore.BLUE}E{Fore.LIGHTYELLOW_EX}S{Fore.WHITE}")

  sp(f"{Fore.RED}● {Fore.WHITE}Google Search\n{Fore.RED}● {Fore.WHITE}Wikipedia\n{Fore.RED}● {Fore.WHITE}Urban Dictionary Search\n{Fore.RED}● {Fore.WHITE}Sugestion And Feedback")

  conf = input(f"{space3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE})")
  if conf == 'y':
    home_page()
  else:
    return

# Searching Commands 
def search_f():
  clear()
  try:
    if searchq == '!about':
      about()
    elif searchq == "!wikipedia":
      wiki()
    elif searchq == "!sugg":
      sugg()
    elif searchq == "!ud":
      ud()
    else:
      try:
        search_bar = f"{Fore.WHITE}{space2}({searchq}{space4}|🔍)"
        print(logo)
        print(search_bar)
        s = searchq.replace(" ", "+")
        for res in search(s, lang='en', num_results=50):
          print(f"{Fore.YELLOW}> {Fore.LIGHTBLUE_EX}{res}\n")
        conf = input(f"{space3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
        if conf == 'y':
          home_page()
        elif conf == "n":
          home_page()
        else:
          return
      except:
        print(logo)
        print(search_bar)
        print(f"{Fore.RED} 404 ERROR")
        sleep(3)
        home_page()
  except:
    pass

def wiki():
  clear()
  print(wikilogo)
  print(space4+f"🔎 Search:")
  
  wikisearchq = input(f"{space3}{Fore.BLUE}>{Fore.LIGHTYELLOW_EX}>{Fore.RED}>{Fore.WHITE} ")
  
  wikis = wikisearchq.replace(" ", "+")
  try:
    wikires = requests.get(f"https://allin1-api.glique.repl.co/wikipedia?word={wikis}&length=5").json()
    
    sum = wikires["result"]
    
    wiki_search_bar = f"{Fore.WHITE}{space2}({wikisearchq}{space4}|🌐)"
    
    clear()
    print(wikilogo)
    print(wiki_search_bar)
    sp(f"{sum}\n")
    print(f"URL: {Fore.LIGHTBLUE_EX}https://en.wikipedia.org/wiki/{wikis}")
    conf = input(f"{space3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
    if conf == 'y':
      home_page()
    elif conf == "n":
      wiki()
    else:
      return
  except:
    wiki_search_bar = f"{Fore.WHITE}{space2}({wikisearchq}{space4}|🌐)"
    clear()
    print(wikilogo)
    print(wiki_search_bar)
    print(f"{Fore.RED} Not Found")
    conf = input(f"{space3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
    if conf == 'y':
      home_page()
    elif conf == "n":
      wiki()
    else:
      return

def ud():
  clear()
  print(udlogo)
  print(space4+f"🔎 Search:")
  
  udsearchq = input(f"{space3}{Fore.BLUE}>{Fore.LIGHTYELLOW_EX}>{Fore.RED}>{Fore.WHITE} ")
  ud_search_bar = f"{Fore.WHITE}{space2}({udsearchq}{space4}|📚)"
  uds = udsearchq.replace(" ", "%20")
  try:
    res = requests.get(f"https://udict-api.glique.repl.co/{uds}").json()
    auth = res["author"]
    defi = res["definition"]
    example = res["example"]
    url = res["permalink"]

    data = f"{Fore.RED}AUTHOR:\n{Fore.WHITE}{auth}\n\n{Fore.RED}DEFINITION:\n{Fore.WHITE}{defi}\n\n{Fore.RED}EXAMPLE:\n{Fore.WHITE}{example}\n\n{Fore.RED}URL: {Fore.LIGHTBLUE_EX}{url}"
    clear()
    print(udlogo)
    print(ud_search_bar)
    sp(data)

    conf = input(f"{space3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
    if conf == 'y':
      home_page()
    elif conf == "n":
      ud()
    else:
      return
  except:
    ud_search_bar = f"{Fore.WHITE}{space2}({udsearchq}{space4}|📚)"
    clear()
    print(udlogo)
    print(ud_search_bar)
    print(f"{Fore.RED} Not Found or The API is offline :(")
    conf = input(f"{space3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
    if conf == 'y':
      home_page()
    else:
      return

def sugg():
  clear()
  print(sugglogo)
  name = input("Discord Username or Any social media username\n>>> ")
  title = input("Title of the suggestion or feedback\n>>> ")
  desc = input("Your Suggestion or Feedback\n>>> ")
  weburl = os.getenv("weburl")
  
  data = {
    "username": "NOT-GOOGLE CLIENT",
    "content": "@everyone",
    "embeds": [{
      "author": {
        "name": name
      },
      "title": title,
      "description": desc
    }]
  }

  res = requests.post(weburl, json=data)

  print(f"Response Code: {res.status_code}\nRedirecting to Home Page In 3 Seconds")
  sleep(1)
  print("3")
  sleep(1)
  print("2")
  sleep(1)
  print("1")
  sleep(1)
  home_page()

  
# Base Code
clear()
print(logo)
print(space3+f"{Fore.WHITE}Type {Fore.RED}!about {Fore.WHITE}to know more.")
print(space3+f"{Fore.WHITE}Type {Fore.RED}!wikipedia {Fore.WHITE}to go to Wikipedia.")
print(space3+f"{Fore.WHITE}Type {Fore.RED}!ud {Fore.WHITE}to go to Urban Dictionary.")
print(space3+f"{Fore.WHITE}Type {Fore.RED}!sugg {Fore.WHITE}to give a suggestion.")
print(space4+f"🔎 Search:")
searchq = input(f"{space3}{Fore.BLUE}>{Fore.LIGHTYELLOW_EX}>{Fore.RED}>{Fore.WHITE} ")
search_f()