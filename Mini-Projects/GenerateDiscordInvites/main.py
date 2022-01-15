print('Loading')
import os
print('Loaded library "os"')

os.system('title Working...')

import requests
print('Loaded library "requests"')

print('Loaded var "word_site"')
print('Making request')
words = requests.get("http://dragonfire.7m.pl/api/wordsDB.txt").content.splitlines()
print('Splitting and printing words...')

for w in words:
	print('https://discord.gg/' + str(w).replace("'b","").replace("b'","").replace("'",""))

with open("discordInvites.txt",'w') as file:
    for w in words:
        file.write('https://discord.gg/' + str(w).replace("'b","").replace("b'","").replace("'","") + f'\n')

print()
input('Press ENTER to continue')