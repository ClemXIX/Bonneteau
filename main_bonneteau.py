import random
import os
from time import sleep
import time
import pandas as pd

#todo
#integrer les sauvegardes au bons endroits.
#faire une fonction nouvelle partie

#base de donnée
try:
	df = pd.read_csv("scores_bonneteau.csv")	  
except:
	df = pd.DataFrame(columns = [
    "player",
    "score"]).to_csv("scores_bonneteau.csv", index=False)
df = pd.read_csv("scores_bonneteau.csv")

#variables
gob = 3
score = 0
choice = 0
best_score = 0
keep_playing = True

#fonctions	
def title_screen():
	
	#listing
    os.system('clear')
    print("a Enes, Clément, Jeffrey Game")
    sleep(2)
    os.system('clear')

    #game title
    sleep(1)
    print("#==========================#")
    print("          Bonneteau")
    print("#==========================#")
    sleep(2)
    os.system('clear')
    
def continuing():
	continue_game = input("voulez vous continuer à jouer ? (oui/non) = ")
	if continue_game in ["yes", "Yes", "true", "True", "y", "Y", "Oui", "oui"]:
		keep_playing = True
		return keep_playing	
	elif continue_game in ["no", "No", "False", "false","N", "n", "non", "Non"]:
		keep_playing = False
		return keep_playing	
	elif continue_game == "easter egg":
		os.system('clear')
		a = 1
		while a < 1200:
			print("vous êtes mauvais", (1201 - a))
			sleep(1)
			a = a + 1
		continuing()
	elif continue_game in ["?", "help", "HELP", "Help"]:
		print("entrez oui ou non pour continuer ou non la partie")
		print("entrez easter egg pour une surprise")
		print("entrez save pour sauvegarder votre score actuel")
		continuing()
	elif continue_game	== "save":
		saving()
		continuing()
	else:
		continuing()	

def saving():
	new_row = pd.DataFrame(data=[{"player" : player_name,
                             "score" : score}])
	df = df.append(new_row)
	df.to_csv("scores_bonneteau.csv", index=False)

def result(choice, winning):
	if winning == choice:
		player_win = True
		return player_win
	elif winning != choice:
		player_win = False
		return player_win

#deroulement
title_screen()
os.system('clear')
player_name = input("Qui es-tu ? ")

while keep_playing:
	os.system('clear')
	winning = random.randint(1, gob)
	choice = int(input(f"choisis entre 1 et {gob} : "))
	choice_good = False
	
	while choice_good ==False:
		if 0<choice <= gob:
			player_win = result(choice, winning)
			choice_good = True
		else:
			os.system('clear')
			print(f"Votre valeur ne peut pas dépasser {gob} et doit être supérieure à 0")
			choice = int(input(f"choisis entre 1 et {gob} : "))
			result(choice, winning)
			choice_good = False

	if player_win == False:
		os.system('clear')
		print("vous avez perdu")
		print("score = ", score)
		print("le bon numéro était : ",winning)
		if best_score < score:
				best_score = score
		score = 0
		keep_playing = continuing()
	elif player_win == True:
		score += 100
		gob += 1
		print("BRAVO !")
		print("score = ", score)
		saving()
		keep_playing = continuing()
	if keep_playing == False:
		if best_score < score:
			best_score = score
		saving()
		os.system('clear')
		print("bye bye")
		print("Votre score était = ", score)
		print("Meilleur score = ",best_score)
		break