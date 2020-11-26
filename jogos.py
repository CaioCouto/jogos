from os import system

import adivinhacao
import forca

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print('''
	(1) Forca 
	(2) Adivinhação
''')

jogo = int(input("Defina o jogo que deseja:  "))

system('cls')

if (jogo == 1): forca.jogar()
elif (jogo == 2): adivinhacao.jogar()