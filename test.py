import random 
from math import * 
#variables de tout le programme :
monnaie = 50
XP = 0
hp_poke_joueur = 60 
hppokefightinitial = 50 
nbr_Flammèche = 15
nbr_LanceFlammes = 20
nbr_Rebondifeu = 10
nbr_Pistolet_à_O = 15
nbr_Siphon = 20
nbr_Hydrocanon = 10
nbr_pokeball = 5
nbr_superball = 0
nbr_hyperball = 0
def menu_combat_poussifeu ():
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
	choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-15 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-10 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-20 hp) {nbr_Rebondifeu}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Flammèche > 0:
				hppokefightinitial = hppokefightinitial - 15 
				nbr_Flammèche = nbr_Flammèche - 1
			else:
				print("Vous n'avez plus de Flammèche, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_LanceFlammes > 0:
				hppokefightinitial = hppokefightinitial - 10 
				nbr_LanceFlammes = nbr_LanceFlammes - 1
			else:
				print("Vous n'avez plus de Lance-Flammes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_Rebondifeu > 0:
				hppokefightinitial = hppokefightinitial - 20 
				nbr_Rebondifeu = nbr_Rebondifeu - 1
			else:
				print("Vous n'avez plus de Rebondifeu, veuillez en chosir une autre ")
	elif choix == 2: 
		print("Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			hp_poke_joueur = hp_poke_joueur + 20
		elif choixsoin == 2: 
			hp_poke_joueur = 60 
		elif choixsoin == 3: 
			print("Sur quelle attaque : \n1)Flammèche (-15 hp) {nbr_Flammèche}/15 \n 2)Lance-Flammes (-10 hp) {nbr_Lance-Flammes}/20 \n 3)Rebondifeu (-20 hp) {nbr_Rebondifeu}/10 ")
			reponse_pp=int(input(f"Quelle attaque choisissez vous ?"))
			if reponse_pp == 1:
			    nbr_Flammèche = nbr_Flammèche - nbr_Flammèche + 15
			elif reponse_pp == 2: 
			    nbr_LanceFlammes = nbr_LanceFlammes - nbr_LanceFlammes + 20
			else:
                nbr_Rebondifeu = nbr_Rebondifeu - nbr_Rebondifeu + 10
	elif choix == 3:
            fuir = False
            print("Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	elif choix == 4: 
            print(f"Quel Pokeball veux-tu utiliser ?\n1) Pokéball ({nbr_pokeball})\n2) Superball ({nbr_superball})\n3) Hyperball ({nbr_hyperball})")
            choix_pokeball = int(input("Choisis le bon numéro (1,2,3)"))
            if choix_pokeball == 1:
                if nbr_pokeball > 0: 
                    nbr_pokeball = nbr_pokeball - 1
                    print("Vous lancez une Pokéball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,5+i)
	                    if proba_poké_pop == 5:
                        	print(f"La Pokéball a pop à la secousse numéro {i+1}!")
                        	break
                    	else :
                        	print(f"La Pokéball n'a pas pop à la secousse numéro {i+1}!")
                        	poké_pop_compteur = poké_pop_compteur + 1
                    if poké_pop_compteur % 2 != 0:
                        print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball = nbr_superball - 1
                    print("Vous lancez une Superball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,6+i)
                        if proba_poké_pop == 5:
                            print(f"La Superball a pop à la secousse numéro {i+1}!")
                            break
                        else:
                            print(f"La Superball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur = poké_pop_compteur + 1
                        if poké_pop_compteur % 2 != 0:
                            print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball = nbr_hyperball - 1
                    print("Vous lancez une Hyperball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,7+i)
                        if proba_poké_pop == 5:
                            print(f"La Hyperball a pop à la secousse numéro {i+1}!")
                            break
                        else:
                            print(f"La Hyperball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur = poké_pop_compteur + 1
                        if poké_pop_compteur % 2 != 0:
                            print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            else:
                print("tu n'as pas le droit on a pas encore coder cette partie et on le fera probablement jamais")


while hppokefightinitial > 0 or not fuir: 
	menu_combat_poussifeu ()
	if hppokefightinitial < 10:
		proba_soin=random.randint(1,3)
		if proba_soin == 1:
			print("le pokemon adverse se soigne ! Il regénère 10 hp")
			hppokefightinitial = hppokefightinitial + 1 
		else: 
			proba_attaque=random.randint(1,2)
			if proba_attaque == 1:
				print("il utilise l'attaque 1")
				hp_poke_joueur = hp_poke_joueur - 1 
			elif proba_attaque == 2:
				print("il utilise l'attaque 2")
				hp_poke_joueur = hp_poke_joueur - 1
			elif proba_attaque == 3:
				print("il utilise l'attaque 3")
				hp_poke_joueur = hp_poke_joueur - 5

	else: 
			proba_attaque=random.randint(1,2)
			if proba_attaque == 1:
				print("il utilise l'attaque 1")
				hp_poke_joueur = hp_poke_joueur - 1 
			elif proba_attaque == 2:
				print("il utilise l'attaque 2")
				hp_poke_joueur = hp_poke_joueur - 1
			elif proba_attaque == 3:
				print("il utilise l'attaque 3")
				hp_poke_joueur = hp_poke_joueur - 5


chemins = {
	1:("Aller visiter la Forêt Pangorn", forêt_pangorn),
	2:("Aller visiter le Donjon", ville_donjon),
	3:("Aller relever le défi des Arènes", arènes_pokémons),
	4:("Aller visiter une mysterieuse grotte", grotte_boss), 
}
