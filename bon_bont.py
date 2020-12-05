"""
Version 1.0, what a beautiful FRANGLISH clap clap
Bonneteau, si on gagne, il y a un gobelet de plus, si on perd retour à 3.
"""

import random

keep_playing = True
bank = 0 
max_cups = 3
print("Pret a tester ta chance ?? (งツ)ว \n \n ")
oui_oui_oui = ["O", "Oui", "OUI", "oui", "Y", "YES", "Yes", "y", "yes", "o", " o"]
non_non_non = ["N", "Non", "NON", "non", "n", "NO", "No", "no", " n", " non"]


#jouer au jeu
while keep_playing:
	choix = 0 #initialiser le choix du joueur
	hidden_ball = random.randrange(1, max_cups) #où la balle sera caché
	#print(hidden_ball) ## CHEATMODE


	#Tester si le joueur rentre un choix possible
	while choix <= 0 or choix > max_cups:
		choix = input(f"Combien ? entre 1 et {max_cups} \n")
		try:
			choix = int(choix)
		except ValueError:
			print(f"Un chiffre entre 1 et {max_cups}\n")
			choix = 0
			continue
		if choix <= 0:
			print("Moins que rien ...")
			continue
		if choix > max_cups:
			print(f"pas plus que : {max_cups}. \n")
			continue

	
	#Player result, did he guess right ?? 
	if choix == hidden_ball:
		print(f"Wouah tu as trouvé le bon chiffre qui était {choix}. Bravo\n")
		max_cups += 1
		bank +=  1
	elif choix != hidden_ball:
		print(f"Dommage, la balle était sous le {hidden_ball}\n")
		if bank == 0:
			print("Ahahaahahahahah  ƪ(ړײ)‎ƪ​​ \n")
		elif bank == 1:
			print("chanceux à moitié on va dire ¯\\_(ツ)_/¯\n")
		else:
			print(f"Tu as trouvé {bank} fois d'affilés. (っ▀¯▀)つ clap clap  \n")
		max_cups = 3 
		bank = 0

		#Va t'il continuer à tester sa luck, on part du principe que oui
		continuer = 0
		
		#Valid input ?? 
		while continuer not in oui_oui_oui:
			continuer = input("On recommence ? (Oui ou non) :\n")
			if continuer in oui_oui_oui:
				print(f"\n \n \n         ┬─┬⃰͡ (ᵔᵕᵔ͜ ) \n \n \n")
				break
			if continuer in non_non_non:
				print("\n \n ε=ε=ε=ε=┌(;￣▽￣)┘ \n \n ")
				keep_playing = False
				break