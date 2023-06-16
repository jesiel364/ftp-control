from ftplib import FTP
import sys
import time

def edit_file(title, content):
	with open(title, "w") as file:
		file.write(content)

def send_comand(cmd):
	with FTP(host="192.168.1.12", user="jesiel", passwd="senha123") as ftp:
		print(ftp.getwelcome())
		print(ftp.pwd()) #print current directory
		# ftp.mkd('my_dir') #create dir
	#	ftp.rmd('my_dir') #remove dir
	#	print(ftp.cwd('my_dir')) #change dir

		edit_file("set.txt", cmd)

		try:
			with open("set.txt", "rb") as file:
				ftp.storlines('STOR comando.txt', file)
		except:
			print("Error")
		# files = []
		# ftp.dir(files.append)
		# for f in files:
		# 	print(f)
		ftp.close()

def verify_info():
	with FTP(host="192.168.1.12", user="jesiel", passwd="senha123") as ftp:
		with open('info_local.txt', 'w', encoding='utf-8') as file:
			info = ftp.retrlines("RETR info.txt", file.write)
			# edit_file("info.txt", info)

		ftp.close()
	with open("info_local.txt", "rb") as file:
		for l in file:
			print(l)
	edit_file("info_local.txt", '')


def main():
	while True:
		user = input("Digite um comando: ")
		send_comand(user)
		if "get info" in user:
			time.sleep(2)
			verify_info()

		elif "bye" in user:
			sys.exit()



main()