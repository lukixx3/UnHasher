import os, colorama, random, argparse, requests, re, time
from colorama import Fore

from lib.banner import banner

"""
__Author__  = Kaneki - KanekiX2
__Name__    = UnHasher
__version__ = V1.0.0 (Beta)
__Code__    = python
__Github__  = https://github.com/KanekiX2
__Date__    = 08 - 04 - 2021
__License__ = GNU General Public License V.3

"""

parser = argparse.ArgumentParser()
parser.add_argument('-c', help='Hash Combo File', dest='file')
args = parser.parse_args()

combolist = (args.file)

class unhasher():
	def __init__(self, email_user, hhash, hash_type):
		self.Hash = hhash
		self.Hash_Type = hash_type
		self.email_user = email_user

	def crack(self):
		r = requests.get(f'http://www.nitrxgen.net/md5db/{self.Hash}.json').json()

		password = r['result']['pass']
		found = r['result']['found']

		if found == True:
			print(Fore.GREEN+self.Hash+f" {self.Hash_Type} {password}{Fore.RESET} - Found")

			with open('found_hash.txt', 'a+') as f:
				f.write(self.email_user+":"+password+"\n")

		else:
			r = requests.get(f'https://md5decrypt.net/Api/api.php?hash={self.Hash}&hash_type={self.Hash_Type}&email=deanna_abshire@proxymail.eu&code=1152464b80a61728').text

			if len(r) != 0:
				print(Fore.GREEN+self.Hash+f" {self.Hash_Type} {password}{Fore.RESET} - Found")

				with open('found_hash.txt', 'a+') as f:
					f.write(self.email_user+":"+password+"\n")


			else:
				print(Fore.RED+self.Hash+f" {self.Hash_Type}{Fore.RESET} - Not Found")


try:
	os.system('cls||clear')
	os.system('title UnHasher ^| V1.0.0 (Beta)')
	print(banner.replace('$',Fore.RED+'0'+Fore.RESET).replace('[ Kaneki ]',f'[ {Fore.YELLOW}Kaneki{Fore.RESET} ]').replace('github.com/KanekiX2',Fore.YELLOW+'github.com/KanekiX2'+Fore.RESET).replace('KanekiX#9999',Fore.YELLOW+'KanekiX#9999'+Fore.RESET)+"\n\n\n")
	start_time = time.time()
	with open(combolist, 'r') as f:
		f = [line.strip('\n') for line in f]

	for combo in f:
		email_user = combo.split(':')[0]
		hhash = combo.split(":")[1]

		if len(hhash) == 32:
			hash_type = "md5"

		if len(hhash) == 40:
			hash_type = "sha1"

		if len(hhash) == 64:
			hash_type = "sha256"

		if len(hhash) == 96:
			hash_type = "sha384"

		if len(hhash) == 128:
			hash_type = "sha512"

		DeHash = unhasher(email_user, hhash, hash_type)
		DeHash.crack()

	print("\n\nHash Cracked in {}".format(time.time() - start_time))
	os.system('pause >nul')

except:
	pass