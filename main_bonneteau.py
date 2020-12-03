import random
import os
from time import sleep
import time
import pandas as pd

#todo
#integrer les sauvegardes au bons endroits.
#faire une fonction nouvelle partie

#variables
gob = 3
score = 0
choice = 0
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
	else:
		continuing()	

def result(choice, winning):
	if winning == choice:
		player_win = True
		return player_win
	elif winning != choice:
		player_win = False
		return player_win

#deroulement
title_screen()
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
	
		a = 1
		while a <= 1200:
			print('vous êtes mauvais', 1200 - a)
			time.sleep(1)
			a=a+1

		keep_playing = False
	elif player_win == True:
		score += 100
		gob += 1
		print("score = ", score)
		keep_playing = continuing()
		if keep_playing == False:
			break