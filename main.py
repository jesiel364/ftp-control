import os
import sys
import subprocess
import time
from gtts import gTTS
from playsound import playsound
import webbrowser as browser

def cria_audio(audio, idioma,  comand):

	tts = gTTS(comand, lang = idioma, slow=False)
	tts.save(audio)
	print(comand)
	playsound(audio)
	os.remove(audio)

def edit_file(title, content, encoding="utf-8"):
	with open(title, "w") as file:
		file.write(content)

def pesquisa():
	print("O que deseja pesquisar?")
	time.sleep(5)
	edit_file("comando.txt",'')

def read_file():
	print("Esperando comando")
	with open("comando.txt", "r") as file:
		while True:
			comand = file.read()
			execute_comand(comand)
			edit_file("comando.txt",'')
			time.sleep(3)
			break

	return comand

def execute_comand(comand):
	# fechar assistente
	if 'fechar assistente' in comand or 'fechar' in comand or 'sair' in comand:
		print("Fechando assistente")
		edit_file("comando.txt",'')
		sys.exit()

	# abrir programas do computador
	elif 'abrir' in comand and 'google chrome' in comand or 'abrir chrome' in comand:
		cria_audio("comand.mp3", "pt-br", f'Abrindo Chrome')
		os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")
	elif 'abrir' in comand and 'reaper' in comand:
		cria_audio('comand.mp3', "pt-br", "Abrindo Reaper")
		edit_file('')
		os.startfile("C:/Program Files/REAPER (x64)/reaper.exe")
	elif 'abrir' in comand and 'sublime text' in comand or 'abrir sublime' in comand:
		cria_audio("comand.mp3", "pt-br", f'Abrindo Sublime Text')
		os.startfile("C:/Program Files/Sublime Text/sublime_text.exe")
	elif 'abrir' in comand and 'cmd' in comand or 'prompt de comando' in comand:
		cria_audio("comand.mp3", "pt-br", f'Abrindo Prompt de comando')
		os.system("cmd")
	elif 'abrir' in comand and 'notion' in comand:
		os.startfile("<caminho para notion na sua máquina>")

	# pesquisa no google
	elif 'pesquisa' in comand and 'google' in comand or 'como' in comand:
		print(comand)
		comand = comand.replace('pesquisar', '')
		comand = comand.replace('pesquisa', '')
		comand = comand.replace('google', '')
		comand = comand.replace('no', '')
		cria_audio("comand.mp3", "pt-br", f'Pesquisando {comand}')
		browser.open(f'https://google.com/search?q={comand}')	

	elif 'get info' in comand:
		result = subprocess.run(["ipconfig"], shell=True, capture_output=True, text=True)
		print(result.stdout)
		edit_file("info.txt", str(result.stdout))
		time.sleep(5)
		edit_file("info.txt", "")

	# desligar o computador
	elif 'desligar computador' in comand and 'uma hora' in comand:
		cria_audio("horas.mp3", "pt-br", "o computador irá desligar em uma hora")
		os.system("shutdown -s -t 3600")
	elif 'desligar computador' in comand and 'meia hora' in comand:
		cria_audio("horas.mp3", "pt-br", "o computador irá desligar em meia hora")
		os.system("shutdown -s -t 1800")
	elif 'cancelar desligamento' in comand:
		cria_audio("horas.mp3", "pt-br", "Desligamento automático do computador cancelado")
		os.system("shutdown -a")	
	elif 'desligar computador' in comand:
		cria_audio("horas.mp3", "pt-br", "desligando computador")
		os.system("shutdown /s /t 1")

def main():
	while True:
		read_file()

main()
