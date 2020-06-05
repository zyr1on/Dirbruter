#!/usr/bin/python3
#author : İnstagram , Twitter =  @semihozdmirr
#example usage: python3 Dirbrute.py http://127.0.0.1 /usr/bin/wordlists/dirb/common.txt 15

import threading
import requests
import sys
from datetime import datetime


def banner():
        print("""
	
	 /$$$$$$$  /$$           /$$$$$$$                        /$$                        
	| $$__  $$|__/          | $$__  $$                      | $$                        
	| $$  \ $$ /$$  /$$$$$$ | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$ 
	| $$  | $$| $$ /$$__  $$| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$__  $$
	| $$  | $$| $$| $$  \__/| $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$| $$  \__/
	| $$  | $$| $$| $$      | $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/| $$      
	| $$$$$$$/| $$| $$      | $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$| $$      
	|_______/ |__/|__/      |_______/ |__/       \______/    \___/   \_______/|__/      
        		Author: @semihozdmirr
			Usage: python3 Dirbrute.py <url> <wordlist> <thread>
			
        """)

if len(sys.argv) < 4:
	banner()
	exit()

target = sys.argv[1]
word_file = sys.argv[2]
threads= int(sys.argv[3])
if not "http" in target:
	print("[*] Wrong url > example url : http://www.site.com or https://www.site.com")
	exit()
wordlist = open(word_file,"r")
banner()
print(f"[*] Started  Target:{target}  Wordlist: {word_file}  Threads: {threads}  Time: {datetime.now()} \n")
print("-"*50)
def main():
	try:
		for word in wordlist:
			line = word.strip()
			full = target + "/" + line
			req = requests.get(full)
			html = str(req.content)
			#you can add something here...
			print("\u001b[37;1m " + line ,end="\r ")
			if "Not Found" in html:
				pass
			else:
				if req.status_code ==200:
					print(f"\u001b[32;1m [+] {full}  " , end="\n")
					req.close()
				else:
					pass
	except:
		print("[*] Maybe Connection Refused or Wrong Url")
		exit()

for x in range(threads):
	t = threading.Thread(target=main)
	t.start()
