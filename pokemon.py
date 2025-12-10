import random 
import time
from math import * 
#variables de tout le programme : 
monnaie = 50
duree_1 = 1
XP = 0
hp_poke_joueur = 60 
hppokefightinitial = 50 
#Variable PP des Pokémons : 
#Variable PP Poussifeu
nbr_Flammèche = 15
nbr_LanceFlammes = 20
nbr_Rebondifeu = 10
#Variable PP Gobou
nbr_Pistolet_à_O = 15
nbr_Siphon = 20
nbr_Hydrocanon = 10
#Variable PP Arcko
nbr_Désherbaffe = 15
nbr_FouetsLiannes = 20
nbr_LammeFeuille = 10
#Variable Pokéballs
nbr_pokeball = 0
nbr_superball = 0
nbr_hyperball = 0
#Variable Potions
nbr_superpotion = 0
nbr_hyperpotion = 0
#variable fossile 
fossile1 = 0
fossile2 = 0
#variable_amitié
amitié = 0
# Dictionnaire des chemins : clé = choix, valeur = (nom, fonction) 
chemins = {
    "1": ("Ville Donjon", ville_donjon),
    "2": ("La forêt Pangorn", forêt_pangorn),
    "3": ("Les arênes Pokémon", arènes_pokémons),
    "4": ("Le Volcan instable de l'île", grotte_boss)
}
#Fonction combat
def boucle_combat(hp_ennemi, nom_poke_ennemi, hp_starter, starter, XP):
    while hp_ennemi > 0 and hp_starter > 0 and not fuir:
        # Appel du menu de combat correspondant au Pokémon actif
        print(f"\n À Vous de Jouer ! \n")
        if starter == 1:
            hp_ennemi = menu_combat_arcko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
        elif starter == 2:
            hp_ennemi = menu_combat_poussifeu (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
        elif starter == 3:
            hp_ennemi = menu_combat_gobou (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
        # Attaque du Pokémon ennemi
        print(f"le pokemon ennemie a {hp_ennemi} pv ")
        print("Au tour du pokémon adverse de jouer ! ")
        if hp_ennemi > 10:
                attaque_ennemi = random.randint(1,4)
                if attaque_ennemi == 1:
                        hp_starter -= 20
                        print(f"{nom_poke_ennemi} vous a infligé 20 dégats. Vous avez {hp_starter} points de vie.")
                elif attaque_ennemi == 2:
                        hp_starter -= 15
                        print(f"{nom_poke_ennemi} vous a infligé 15 dégats. Vous avez {hp_starter} points de vie.")
                else:
                        hp_starter -= 10
                        print(f"{nom_poke_ennemi} vous a infligé 10 dégats. Vous avez {hp_starter} points de vie.")
        else:
                attaque_ou_soin = random.randint(1,4)
                if attaque_ou_soin == 1:
                        hp_ennemi += 15
                        print(f"{nom_poke_ennemi} s'est soigné et a {hp_ennemi} points de vie.")
                else:
                        attaque_ennemi_2 = random.randint(1,4)
                        if attaque_ennemi_2 == 1:
                                hp_starter -= 20
                                print(f"{nom_poke_ennemi} vous a infligé 20 dégats. Vous avez {hp_starter} points de vie.")
                        elif attaque_ennemi_2 == 2:
                                hp_starter -= 15
                                print(f"{nom_poke_ennemi} vous a infligé 15 dégats. Vous avez {hp_starter} points de vie.")
                        else:
                                hp_starter -= 10
                                print(f"{nom_poke_ennemi} vous a infligé 10 dégats. Vous avez {hp_starter} points de vie.")
        if hp_ennemi <= 0:
                XP_gagne=random.randint(100,200)
                XP += XP_gagne
                if XP >= 500:
                        XP = 0
                        print(f"Félicitation, vous avez gagné(e) votre combat {nom_poke_ennemi}, Vous avez gagné(e) {XP_gagne} XPs !\n Que ce passe-t-il ?\n\n\n Le Pokémon évolue !")
                        if starter == 1:
                                print(f"Arcko devient Massko ! ")
                        elif starter == 2:
                                print(f"Poussifeu devient Galifeu ! ")
                        elif starter == 3:
                                print(f"Gobou devient Flobio ! ")
                        elif starter == 4:
                                print(f"Massko devient Jungko ! ")
                        elif starter == 5:
                                print(f"Galifeu devient Braségali! ")
                        elif starter == 6:
                                print(f"Flobio devient Laggron ! ")
                        elif starter == 7:
                                print(f"Jungko devient Méga-Jungko ! ")
                        elif starter == 8:
                                print(f"Braségali devient Méga-Braségali !")
                        elif starter == 9:
                                print(f"Laggron devient Méga-Laggron !")
                        starter += 3
                else:
                        print(f"Félicitation, vous avez gagné(e) votre combat {nom_poke_ennemi}, Vous avez gagné(e) {XP_gagne} XPs !")

def menu_combat_gobou (nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, hp_ennemi, hp_starter, nbr_superpotion, nbr_hyperpotion, nbr_pokeball, nbr_superball, nbr_hyperball):
	fuir = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-15 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-10 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-20 hp) {nbr_Hydrocanon}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-15 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-10 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-20 hp) {nbr_Hydrocanon}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Pistolet_à_O > 0:
				hp_ennemi -= 15 
				nbr_Pistolet_à_O -= 1
				return hp_ennemi
			else:
				print("Vous n'avez plus de Pistolet à O, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_Siphon > 0:
				hp_ennemi -= 10 
				nbr_Siphon -= 1
				return hp_ennemi
			else:
				print("Vous n'avez plus de Siphon, faites attention la prochaine fois ")
		elif quelle_attaque == 3: 
			if nbr_Hydrocanon > 0:
				hp_ennemi -= 20 
				nbr_Hydrocanon -= 1
				return hp_ennemi
			else:
				print("Vous n'avez plus de Hydrocanon, faites attention la prochaine fois ")
	elif choix == 2: 
		print("Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print("Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superpotion > 0 :
				hp_poke_joueur += 20
				nbr_superpotion -= 1
			else:
				print(f"Vous n'avez plus de super potion...")
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0:
				hp_poke_joueur = 60 
				nbr_hyperpotion -= 1
			else:
				print(f"Vous n'avez plus d'hyper potion...")
		elif choixsoin == 3:
                    print(f"Sur quelle attaque : \n1)Pistolet à O  (-15 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-10 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-20 hp) {nbr_Hydrocanon}/10 ")
                    reponse_pp=int(input(f"Quel attaque choisissez vous ?"))
                    while not response_pp in (1,2,3):
                        print(f"Veuillez saisir un nombre correct")
                        print(f"Sur quelle attaque : \n1)Pistolet à O  (-15 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-10 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-20 hp) {nbr_Hydrocanon}/10 ")
                        reponse_pp=int(input(f"Quel attaque choisissez vous ?"))
                    if reponse_pp == 1:
                        nbr_Pistolet_à_O = 15
                    elif reponse_pp == 2:
                        nbr_Siphon = 20
                    else:
                        nbr_Hydrocanon = 10
	elif choix == 3: 
            print(f"Quel Pokeball veux-tu utiliser ?\n1) Pokéball ({nbr_pokeball})\n2) Superball ({nbr_superball})\n3) Hyperball ({nbr_hyperball})")
            choix_pokeball = int(input("Choisis le bon numéro (1,2,3)"))
            while not choix_pokeball in (1,2,3):
                print(f"Veuillez saisir un nombre correct")
                print(f"Quel Pokeball veux-tu utiliser ?\n1) Pokéball ({nbr_pokeball})\n2) Superball ({nbr_superball})\n3) Hyperball ({nbr_hyperball})")
                choix_pokeball = int(input("Choisis le bon numéro (1,2,3)"))
            if choix_pokeball == 1:
                if nbr_pokeball > 0: 
                    nbr_pokeball -= 1
                    print("Vous lancez une Pokéball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,5+i)
                        if proba_poké_pop == 5:
                            print(f"La Pokéball a pop à la secousse numéro {i+1}!")
                            break
                        else :
                            print(f"La Pokéball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur += 1
                    if poké_pop_compteur % 2 != 0:
                        print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print("Vous lancez une Superball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,6+i)
                        if proba_poké_pop == 5:
                            print(f"La Superball a pop à la secousse numéro {i+1}!")
                            break
                        else:
                            print(f"La Superball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur += 1
                        if poké_pop_compteur % 2 != 0:
                            print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print("Vous lancez une Hyperball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,7+i)
                        if proba_poké_pop == 5:
                            print(f"La Hyperball a pop à la secousse numéro {i+1}!")
                            break
                        else:
                            print(f"La Hyperball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur += 1
                        if poké_pop_compteur % 2 != 0:
                            print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print("Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return hp_ennemi
	
def menu_combat_poussifeu (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-15 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-10 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-20 hp) {nbr_Rebondifeu}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-15 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-10 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-20 hp) {nbr_Rebondifeu}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Flammèche > 0:
				hp_ennemi -= 15 
				nbr_Flammèche -= 1
				return hp_ennemi
			else:
				print("Vous n'avez plus de Flammèche, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_LanceFlammes > 0:
				hp_ennemi -= 10 
				nbr_LanceFlammes -= 1
				return hp_ennemi
			else:
				print("Vous n'avez plus de Lance Flammes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_Rebondifeu > 0:
				hp_ennemi -= 20 
				nbr_Rebondifeu -= 1
				return hp_ennemi
			else:
				print("Vous n'avez plus de Rebondifeu, veuillez en chosir une autre ")
	elif choix == 2: 
		print("Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print("Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superption > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
			if nbr_superpotion == 0 :
				print(f"Vous n'avez plus de super potion...")
				
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0 :
				hp_starter = 60 
				nbr_hyperpotion -= 1
			if nbr_hyperpotion == 0 :
				print(f"vous n'avez plus d'hyper potion...")
				
		elif choixsoin == 3: 
			print("Sur quelle attaque : \n1)Flammèche (-15 hp) {nbr_Flammèche}/15 \n 2)Lance-Flammes (-10 hp) {nbr_Lance-Flammes}/20 \n 3)Rebondifeu (-20 hp) {nbr_Rebondifeu}/10 ")
			reponse_pp=int(input(f"Quelle attaque choisissez vous ?"))
			if reponse_pp == 1:
			    nbr_Flammèche = 15
			elif reponse_pp == 2: 
			    nbr_LanceFlammes == 20
			else:
				nbr_Rebondifeu = 10
	elif choix == 3: 
            print(f"Quel Pokeball veux-tu utiliser ?\n1) Pokéball ({nbr_pokeball})\n2) Superball ({nbr_superball})\n3) Hyperball ({nbr_hyperball})")
            choix_pokeball = int(input("Choisis le bon numéro (1,2,3)"))
            while not choix_pokeball in (1,2,3):
                print(f"Veuillez saisir un nombre correct")
                print(f"Quel Pokeball veux-tu utiliser ?\n1) Pokéball ({nbr_pokeball})\n2) Superball ({nbr_superball})\n3) Hyperball ({nbr_hyperball})")
                choix_pokeball = int(input("Choisis le bon numéro (1,2,3)"))
            if choix_pokeball == 1:
                if nbr_pokeball > 0: 
                    nbr_pokeball -= 1
                    print("Vous lancez une Pokéball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,5+i)
                        if proba_poké_pop == 5:
                            print(f"La Pokéball a pop à la secousse numéro {i+1}!")
                            break
                        else :
                            print(f"La Pokéball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur += 1
                    if poké_pop_compteur % 2 != 0:
                        print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print("Vous lancez une Superball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,6+i)
                        if proba_poké_pop == 5:
                            print(f"La Superball a pop à la secousse numéro {i+1}!")
                            break
                        else:
                            print(f"La Superball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur += 1
                        if poké_pop_compteur % 2 != 0:
                            print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print("Vous lancez une Hyperball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,7+i)
                        if proba_poké_pop == 5:
                            print(f"La Hyperball a pop à la secousse numéro {i+1}!")
                            break
                        else:
                            print(f"La Hyperball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur += 1
                        if poké_pop_compteur % 2 != 0:
                            print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print("Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return hp_ennemi 
	
def menu_combat_arcko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_poke_joueur,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-15 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-10 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-20 hp) {nbr_Rebondifeu}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-15 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-10 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-20 hp) {nbr_Rebondifeu}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Désherbaffe > 0:
				hp_ennemi -= 15 
				nbr_Désherbaffe -= 1
				return hp_ennemi
			else:
				print("Vous n'avez plus de Désherbaffe, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_FouetsLiannes > 0:
				hp_ennemi -= 10 
				nbr_FouetsLiannes -= 1
				return hp_ennemi
			else:
				print("Vous n'avez plus de Fouets-Liannes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_LammeFeuille > 0:
				hp_ennemi -= 20 
				nbr_LammeFeuille -= 1
				return hp_ennemi
			else:
				print("Vous n'avez plus de Lamme-Feuille, veuillez en chosir une autre ")
	elif choix == 2: 
		print("Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print("Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superption > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
			if nbr_superpotion == 0 :
				print(f"Vous n'avez plus de super potion...")
				
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0 :
				hp_starter = 60 
				nbr_hyperpotion -= 1
			if nbr_hyperpotion == 0 :
				print(f"vous n'avez plus d'hyper potion...")
				
		elif choixsoin == 3: 
			print("Sur quelle attaque : \n1)Flammèche (-15 hp) {nbr_Flammèche}/15 \n 2)Lance-Flammes (-10 hp) {nbr_Lance-Flammes}/20 \n 3)Rebondifeu (-20 hp) {nbr_Rebondifeu}/10 ")
			reponse_pp=int(input(f"Quelle attaque choisissez vous ?"))
			if reponse_pp == 1:
			    nbr_Désherbaffe = 15
			elif reponse_pp == 2: 
			    nbr_FouetsLiannes == 20
			else:
				nbr_LammeFeuille = 10
	elif choix == 3: 
            print(f"Quel Pokeball veux-tu utiliser ?\n1) Pokéball ({nbr_pokeball})\n2) Superball ({nbr_superball})\n3) Hyperball ({nbr_hyperball})")
            choix_pokeball = int(input("Choisis le bon numéro (1,2,3)"))
            while not choix_pokeball in (1,2,3):
                print(f"Veuillez saisir un nombre correct")
                print(f"Quel Pokeball veux-tu utiliser ?\n1) Pokéball ({nbr_pokeball})\n2) Superball ({nbr_superball})\n3) Hyperball ({nbr_hyperball})")
                choix_pokeball = int(input("Choisis le bon numéro (1,2,3)"))
            if choix_pokeball == 1:
                if nbr_pokeball > 0: 
                    nbr_pokeball -= 1
                    print("Vous lancez une Pokéball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,5+i)
                        if proba_poké_pop == 5:
                            print(f"La Pokéball a pop à la secousse numéro {i+1}!")
                            break
                        else :
                            print(f"La Pokéball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur += 1
                    if poké_pop_compteur % 2 != 0:
                        print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print("Vous lancez une Superball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,6+i)
                        if proba_poké_pop == 5:
                            print(f"La Superball a pop à la secousse numéro {i+1}!")
                            break
                        else:
                            print(f"La Superball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur += 1
                        if poké_pop_compteur % 2 != 0:
                            print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print("Vous lancez une Hyperball !")
                    for i in range (3):
                        poké_pop_compteur = 0
                        proba_poké_pop=random.randint(1,7+i)
                        if proba_poké_pop == 5:
                            print(f"La Hyperball a pop à la secousse numéro {i+1}!")
                            break
                        else:
                            print(f"La Hyperball n'a pas pop à la secousse numéro {i+1}!")
                            poké_pop_compteur += 1
                        if poké_pop_compteur % 2 != 0:
                            print("le pokémon a été capturé. Bravo !")
                else:
                    print("Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print("Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return hp_ennemi			
#fonction boutique
def boutique (monnaie,nbr_pokeball,nbr_superball,nbr_hyperball,nbr_superpotion,nbr_hyperpotion):
	print(f" accueil : Bienvenue à la boutique que souhaitez vous acheter ?")
	print(f"\n1)acheter des Pokéballs\n2)acheter des potions")
	achat_boutique = int(input("\nQue choisissez vous ? (sélectionnez le bon numéro) : ")) 
	while not achat_boutique in (1,2):
		print(f"Veuillez saisir un nombre correct")
		print(f"\n1)acheter des Pokéballs\n2)acheter des potions")
	achat_boutique = int(input("\nQue choisissez vous ? (sélectionnez le bon numéro) : ")) 
	if achat_boutique == 1:
		print(f"Quelle type de pokéball voulez-vous acheter ?")
		print(f"\n1)Pokéball\n2)Superball\n3)Hyperball")
		achat_poke = int(input("que choisissez vous ? (sélectionnez le numéro) : ")) 
		while not achat_poke in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"\n1)Pokéball\n2)Superball\n3)Hyperball")
			achat_poke = int(input("que choisissez vous ? (sélectionnez le numéro) : ")) 
		if achat_poke == 1:
			if monnaie >= 5:
				monnaie -= 5
				print(f"Vous venez d'acheter une pokéball !")
				nbr_pokeball += 1
			else :
				print(f"T'as plus de thunes sale sdf, sors de ma boutique !")

		elif achat_poke == 2:
			if monnaie >= 10 :
				print(f"Vous venez d'acheter une superball !")
				monnaie -= 10
				nbr_superball += 1
			else :
				print(f"T'as plus de thunes sale sdf, sors de ma boutique !")

		else :
			if monnaie >= 15 :
				print(f"Vous venez d'acheter une hyperball !")
				monnaie -= 15
				nbr_hyperball += 1
			else :
				print(f"T'as plus de thunes sale sdf, sors de ma boutique")
				
	else :
		print(f"Quelle potion voulez-vous acheter ?")
		print(f"\n1)super potion\n2)hyper potion")
		achat_potion = int(input("Que choisissez vous ? (sélectionnez le numéro) : ")) 
		while not achat_potion in (1,2):
			print(f"Veuillez saisir un nombre correct")
			print(f"\n1)super potion\n2)hyper potion")
			achat_potion = int(input("Que choisissez vous ? (sélectionnez le numéro) : ")) 
		if achat_potion == 1 :
			if monnaie >= 10 :
				print(f"Vous venez d'acheter une super potion !")
				monnaie -= 10
				nbr_superpotion += 1
			else :
				print(f"T'as plus de thunes sale sdf, sors de ma boutique")

		else :
			if monnaie >= 15 :
				print(f"Vous venez d'acheter une hyper potion !")
				monnaie -= 15
				nbr_hyperpotion += 1
			else :
				print(f"T'as plus de thunes sale sdf, sors de ma boutique")


# --- Définition des fonctions associées à chaque chemin --- #

def ville_donjon (): 
	print(f"Tu as choisis de te diriger vers la ville donjon du nom de Versailles")
	print(f"Après quelques heures de marche tu te retrouves face au château de Versailles")
	print(f"{prenom_1} : Ce château me donne des frissons dans le dos mais je suis sûr de trouver des super pokémons et récompenses !")
	print(f"Tu rentres dans le château et tu t'enfonces dans une salle obscure...")
	print(f"Tu observes deux objets scintillants à quelques mètres de toi")
	print(f"Les lumières de la salle s'allument et tu te retrouves face à un ténéfix !")
	print(f"Que le combat commence")
	#combat ténéfix
	boucle_combat(65, "Ténéfix", 80, starter, XP)
	print(f"Après ce rude combat, tu t'orientes vers le fond de la salle")
	print(f"2 portes s'offrent à toi...")
	print("Que voulez vous faire :")
	print("1)porte de gauche \n2)porte de droite")
	choix_porte = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	while not choix_porte in (1,2):
		print(f"Veuillez saisir un nombre correct")
		print("1)porte de gauche \n2)porte de droite")
		choix_porte = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	if choix_porte = 1 :
		print(f"Vous vous dirigez vers la porte de gauche")
		print(f"Vous entendez un rugissement venant de derrière la porte...")
		print(f"Vous décidez quand même d'entrer car vous savez porter vos balls")
		print(f"Vous vous tenez devant absol, le combat risque d'être compliqué !")
		print(f"Que le combat commence !")
		#combat absol
		boucle_combat(60, "Absol", 80, starter, XP)
		
	else :
		print(f"Vous vous dirigez vers la porte de droite")
		print(f"Vous entendez un cri effrayant venant de derrière la porte...")
		print(f"Vous décidez quand même d'entrer car vous savez porter vos balls")
		print(f"Vous vous tenez devant spectrum, le combat risque d'être compliqué !")
		print(f"Que le combat commence !")
		#combat spectrum
		boucle_combat(75, "Spectrum", 80, starter, XP)
		print("Après ce rude combat vous vous dirigez vers le la porte au fond de la salle, et, juste avant de la franchir vous êtes intrigués par une trappe dans un coinde la salle")
		print("Que voulez vous faire :")
		print("1)porte\n2)trappe")
		choix_trappe = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		while not choix_porte in (1,2):
			print(f"Veuillez saisir un nombre correct")
			print("1)porte\n2)trappe")
			choix_trappe = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		if choix_trappe = 1:
			print("Vous vous retrouvez dans un long couloir comme ceux qui mènent au boss dans les jeux")
			print("En poussant la grande porte au bout du couloir vous tombez face à un trioxhydre, bonne chance...")
		else:
			print("Vous passez la trappe et vous êtes arrivés dans une salle avec plusieurs portes")
			labyrinthe = {
				"A": {
					"gauche": "B",
					"droite": "C",
				},
				"B": {
					"gauche": "I",
					"face": "J",
				},
				"C": {
					"gauche": "F",
					"face": "E",
					"droite": "D",
				},
				"D": { 
					"face": "Q",
					"gauche": "R",
				},
				"E": {
					"face": "O",
					"droite": "H"
				},
				"F": { 
					"face": "N",
					"gauche": "M",
				},
				"H": {
					"gauche": "S",
					"droite": "T",
				},
				"I": {
					None,
				},
				"J": {
					"droite": "K",
					"gauche": "L",
				},
				"K": { 
					None,
				},
				"L": {
					None,
				},
				"M": { 
					None,
				},
				"N": { 
					None,
				},
				"O": { 
					None,
				},
				"P": { 
					None,
				},
				"Q": { 
					None,
				},
				"R": { 
					None,
				},
				"S":{
					"sortie",
				},
				"T": { 
					None,
				}
			}
		position = "A"

		while True:
			print(f"Vous êtes à : {position}")

   	 	chemins = labyrinthe[position]

    #sortie
			if position == "sortie":
				print("\n Bravo ! Vous avez trouvé la sortie du labyrinthe !")
				print("Vous êtes arrivés dans la salle au trésor caché et un objet mystérieux est placé au centre de la pièce...")
				print("Vous vous rapprochez et prenez l'objet. C'est une partie d'un fossile mâchoire !")
				fossile2 += 1
				print("une porte se tient au fond de la pièce pour sortir, vous la prenez et vous tombez directement dans la salle du boss !") 
				print("Un trioxhydre fait son appirition, bonne chance...")
		
		
	#chemins
			if all(direction is None for direction in chemins.values()):
				print("Cul-de-sac ! Retour à l'entrée...\n")
    			position = "A"
		
			print("Options disponibles :")
			for direction, destination in chemins.items():
				if destination is not None:
        			print(f"  - {direction} -> {destination}")
			
			choix = input("Direction (gauche, face, droite) : ")
		
			if choix not in chemins:
        	print("Direction invalide.\n")
		
			position = chemins[choix]
			print()		
	
def grotte_boss (): 
	print(f"vous decidez de prendre la direction du Volcan de l'ile qui se trouve être de plus en plus instable récemment")
	print(f"En te rapprochant du volcan tu te retrouves face à une grotte")
	print("Que voulez vous faire :")
	print("1)rentrer dans la grotte\n2)faire demi-tour")
	response_17 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	while not response_17 in (1,2):
		print(f"Veuillez saisir un nombre correct")
		print("1)rentrer dans la grotte\n2)faire demi-tour")
		response_17 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	if response_17 == 1 :
		print(f"Vous avez décidé de rentrer dans la grotte, vous marchez pendant de longues minutes jusqu'à vous retrouver dans une salle souterraine")
		print(f"Un pokémon que vous n'avez encore jamais croisé fait son apparition")
		#combat pokémon mystérieux
		boucle_combat(200, "Mewtoo", 100, starter, XP)
		
	else :
		
def arènes_pokémons ():
		print(f"Vous arrivez à présent aux arènes pokémons espérant gagner de nombreuses récompenses et faire évoluer vos pokémons")
		print(f"quelqu'un à l'entrée de l'arène vous attend pour vous expliquer les règles de l'arène pokémon")
		print(f"organisateur : Bonjour jeune homme, vous êtes arrivé à l'arène pokémon, ici de nombreux dresseurs s'affrontent en espérant atteindre la finale du tournoi pour gagner un pokémon rarissime !")
		print(f"organisateur : Le fonctionnement est très simple, vous démarrez quand 32 dresseurs pokémons arrivent dans l'arène et dès que vous perdez vous devez attendre le prochain tournoi, par contre à chaque fois que vous gagnez vous passez à l'étape supérieure et vous affrontez de noueaux dresseurs. Vous avez le droit d'utliser des potions de soins sur vos pokémons seulement entre chaque combat; Bonne chance !")
		print(f"Organisateur : Alors ça te tente ?")
		print("Que voulez vous faire :")
		print("1)S'inscrire au tournoi\n2)partir de l'arène pokémon")
		response_8 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		while not response_8 in (1,2):
		print(f"Veuillez saisir un nombre correct")
		print("1)S'inscrire au tournoi\n2)partir de l'arène pokémon")
		response_8 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		if response_8 == 1:
			print(f"votre premier combat commence !")
		else:
			print(f"Vous sortez des arènes pokémons, la queue entre les jambes (#tapette)")
			print("À la sortie des arenes Pokémon vous rencontrés votre mère qui a honte de vous. Elle vous ramène alors jusqu'à chez vous et vous finissez votre vie à jouer à LOL comme un gros puant #pasdemeufscommemathurin")
			quit()

def forêt_pangorn ():
	print(f"Après quelques dizaines de minutes de marche, vous arrivez à l'entrée de la forêt Pangorn")
	print(f"{prenom_1} : j'entends de l'eau qui coule vers l'ouest. J'aprçois une lueur pas loin devant moi. J'entends aussi la terre qui tremble à quelques centaines de mètres à ma droite")
	print("Que voulez vous faire :")
	print("1)Se diriger vers les bruits de l'eau\n2)S'approcher de la lueur\n3)Se rendre aux lieux des tremblements de terre")
	response_9 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	while not response_9 in (1,2,3):
		print(f"Veuillez saisir un nombre correct")
		print("1)Se diriger vers les bruits de l'eau\n2)S'approcher de la lueur\n3)Se rendre aux lieux des tremblements de terre")
		response_9 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	if response_9 == 1 :
		print(f"Vous êtes émerveillé par une magnifique cascade cependant vous ne vous rendez même pas compte qu'un Crocodil vous observe")
		print(f"Le Crocodil vous saute dessus seulement vous le voyez au dernier moment et vus avez le choix entre esquiver en vous baissant ou en sautant vers la rivière")
		print("que voulez vous faire ?")
		print("1)esquiver en se baissant\n2)esquiver en sautant vers la rivière")
		response_10 : int(input("que choisissez vous ? (sélectionnez le numéro) : "))
		while not response_10 in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print("1)esquiver en se baissant\n2)esquiver en sautant vers la rivière")
			response_10 : int(input("que choisissez vous ? (sélectionnez le numéro) : "))
		if response_10 == 1 :
			Croco_griffe = random.randint(1,2)
			if Croco_griffe == 1:
				print(f"Le crocodil vous érafle le dos mais vous êtes légèrment blessé, il va falloir soigner cela avant que ça ne s'infecte")
				print(f"Le Crocodil se dresse devant vous, préparez vous au combat !")
			
			else:
				print(f"vous avez esquivé de justesse, préparez vous au combat !")
		
		if response_10 == 2 :
		print(f"Vous vous retrouvez au bord de la rivière et un léviator surgit et vous mange tout cru !")
		print(f"Game over")
		quit()
	
	if response_9 == 2 :
		print("Au fur et à mesure que vous vous approchez de la lumière vous sentez une odeur de brûlé")
		print("Vous avez trop avancé et vous êtes maintenant encerclés par des flammes. Vite il faut s'échapper !")
		print("En vous retournant vous vous retrouvez face à un ouisticram qui vous bloque le passage. Préparez-vous au combat !")
			#combat
		
				
	if response_9 == 3 :
		print("Vous vous rapprochez des tremblements de terre, et vous apercevez un onix mais il n'a pas l'air dans son état normal, il se tape contre une falaise...")
		print("cependant à cause des secousses vous trébuchez et vous vous retrouvez par terre")
		print("à cause des coups donnés par onix sur la falaise des rochers tombent droit sur vous !")
		print("Que voulez vous faire ?")
		print("1)se cacher derrière un arbre\n 2)plonger en avant")
		response_13 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
		while not response_13 in (1,2):
			print(f"Veuillez saisir un nombre correct")
			print("1)se cacher derrière un arbre\n 2)plonger en avant")
			response_13 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
		if response_13 == 1:
			arbre = random.randint(1,4)
			if arbre == 1 :
				print("Un rocher vous à éraflé dans sa chute, vous êtes plutôt sérieusement blessé, il va falloir se rendre chez un médecin")
			else :
				print("Vous avez réussi à esquiver la chute de rochers, mais pourquoi le Onix est-il aussi intrigué par cette falaise ?")
				onix_secret()
		else :
			print("vous vous êtes foulé la cheville mais vous avez esquivé la chute de rochers, cependant il va falloir se rendre chez un médecin")
			onix_secret()
def onix_secret ():
	print("Il va falloir combattre pour savoir ce qui intrigue ce onix !")
	#combat onix
	print(" {prenom_1} : Pfiou, ce combat n'était pas facile mais que cache cette falaise ? Je n'ai d'autre choix que d'escalader mais c'est risqué !")
	print("Que voulez-vous faire ?")
	print("1) Grimper la falaise\n2)Rebrousser chemin")
	response_14 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
	while not response_14 in (1,2):
			print(f"Veuillez saisir un nombre correct")
			print("1) Grimper la falaise\n2)Rebrousser chemin")
		response_14 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
	if response_14 == 1 :
		print(f"{prenom_1} : c'est parti pour une petite séance d'escalade !")
			chutes = 0
			bonnes_prises = 0
			while chutes != 5 and bonnes_prises != 5:
				reponse_15 = int(input("Que voulez vous faire ? : \n1)Monter la main gauche ?\n2)Monter la main droite ? (sélectionnez le numéro) : "))
				while not response_15 in (1,2):
					print(f"Veuillez saisir un nombre correct")
					reponse_15 = int(input("Que voulez vous faire ? : \n1)Monter la main gauche ?\n2)Monter la main droite ? (sélectionnez le numéro) : "))
				if reponse_15 == 1:
					print("La prise ne tient pas, vous êtes tombé(e)")
					chutes += 1
					bonnes_prises = 0
					print(f"Vous avez {chutes} chute(s) et les bonnes prises ont été remise à {bonnes_prises}. \n	⚠️ Attention à ne pas trop chuter ! ⚠️")
				else :
					print("La prise tient, reste plus qu'à continuer comme ça !")
					bonnes_prises += 1
					print(f"Vous avez {chutes} chute(s) et {bonnes_prises} bonnes prises. \n	⚠️ Attention à ne pas trop chuter ! ⚠️")
			if bonnes_prises == 5 :
				print("{prenom_1} : Pas simple cette ascension mais je suis enfin arrivé dans cette grotte qui intrguait le Onix")
				print("Vous avancez jusqu'au fond de la grotte et un caillou avec une forme étrange se trouve au centre de la grotte")
				print("Vous venez de trouver un fossile mâchoire ! Ce fossile, si les conditions sont réunies, va se transformer en un ptyranidur !") 
				print("{prenom_1} : Quel incroyable trésor ! Il est peut-être temps de partir maitenant")
				fossile1 += 1
			else :
				print("vous êtes tombés trop de fois, vous êtes morts de chute")
				print("Game Over")
				quit()
#Introduction
print(f"Homme mystérieux : Bonjour jeune homme! Tu es perdu ? Tu ne devrais pas te promener seul dans la forêt si tard le soir ! Il y a des rumeurs comme quoi cette forêt abrite les Pokemons les plus dangereux.")
input("↓")
print(f"Homme mystérieux : Comment t'appelles tu ? ") 
input("↓")
prenom_1 = input("Indiquez votre nom : ")
print(f"Homme mystérieux : Viens {prenom_1}, je vais te ramener chez tes parents, c'est dangereux ici !")
input("↓")
print(f"10 jours plus tard, alors que vous vous promenez dans Perdium, vous croisez une foule entourant l'homme que vous aviez croisé dans la forêt.") 
input("↓")

#Premier choix 
print("Que voulez vous faire :")
print("1)Aller voir la foule de plus près\n2)Partir dans le sens opposé") 
response_1 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
while not response_1 in (1,2):
	print(f"Veullez saisir un nombre correct"):
	print("1)Aller voir la foule de plus près\n2)Partir dans le sens opposé") 
	response_1 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
#Branche 1 (direct foule) 
if int(response_1) == 1:
	print(f"Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
	input("↓")
	print(f"Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
	input("↓")
	print(f"{prenom_1} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
	input("↓")
	print(f"Homme mystérieux : Je viens visiter mon village natal, tu ne me connais pas ? ")
	input("↓")
	print(f"{prenom_1} : Non! Qui êtes-vous ?")
	input("↓")
	print(f"Homme mystérieux : Je suis le tout nouveau maitre Pokémon. Je viens de gagner le combat final de la ligue Pokémon")
	input("↓")
	print(f"{prenom_1} : La ligue Pokémon ? C'est quoi ? ")	
	input("↓")
	print(f"Homme mystérieux : Tu ne connais pas la ligue Pokémon ?")
	input("↓")
	print(f"{prenom_1} : Non, c'est quoi ?")
	input("↓")
	print(f"Homme mystérieux : C'est une ligue connue à l'internationale où tout les combattants pokémon s'affrontent pour savoir qui est le meilleur dresseur, ça t'intéresse ?")
	input("↓")
	print(f"Que voulez vous faire :")
	print("1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
	response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	while not response_2 in (1,2):
		print(f"Veuillez saisir un nombre correct")
		print("1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
		response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	#branche 1-1 (il accepte le défi de devenir dresseur) 
	if int(response_2) == 1:
		print(f"{prenom_1} : Oui je veux entrer dans le monde Pokémon !")
		input("↓")
		print(f"Homme mystérieux : Très bien alors il est temps de choisir ton premier pokémon !")
	#Branche 1-2 (il renonce au défi fin du jeu) 
	elif int(response_2) == 2:
		print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
		quit()
#Branche 2 (il va dans l'autre sens et rencontre son meilleur pote) 
elif int(response_1) == 2: 
	print(f"Quelqu'un vous tape à l'épaule et vous vous retournez")
	input("↓")
	print(f"jeune garçon : Salut comment tu t'appelles ? Tu es nouveau ici ?")
	input("↓")
	print(f"Que voulez vous faire :")
	print(f"1)Faire connaissance\n2)L'ignorer") 
	response_3 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	while not response_3 in (1,2):
		print(f"Veuillez saisir un nombre correct")
		print(f"1)Faire connaissance\n2)L'ignorer") 
		response_3 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	if int(response_3)== 1:
		print(f"{prenom_1} : Je m'appelle {prenom_1}, je suis de retour ici, et toi comment tu t'appelles?")
		input("↓")
		print(f"jeune garçon : Je m'appelle Victor, ça te dit qu'on devienne potes?")
		input("↓")
		print(f"Que voulez vous faire :")
		print(f"1)devenir amis\n2)Le repousser")
		response_4 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		while not response_4 in (1,2):
			print(f"Veuillez saisir un nombre correct")
			print(f"1)devenir amis\n2)Le repousser")
			response_4 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		if int(response_4)== 1:
			print(f"{prenom_1} : Oui bien sûr, ça te dit qu'on se rapproche de la foule ?")
			input("↓")
			print(f"Vous vous rapprochez de la foule")
			input("↓")
			print(f"Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
			input("↓")
			print(f"Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
			input("↓")
			print(f"{prenom_1} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
			input("↓")
			print(f"Homme mystérieux : Je viens visiter mon village natal, tu ne me connais pas ? ")
			input("↓")
			print(f"{prenom_1} : Non! Qui êtes-vous ?")
			input("↓")
			print(f"Homme mystérieux : Je suis le tout nouveau maitre Pokémon. Je viens de gagner le combat final de la ligue Pokémon")
			input("↓")
			print(f"{prenom_1} : La ligue Pokémon ? C'est quoi ? ")	
			input("↓")
			print(f"Homme mystérieux : Tu ne connais pas la ligue Pokémon ?")
			input("↓")
			print(f"{prenom_1} : Non, c'est quoi ?")
			input("↓")
			print(f"Homme mystérieux : C'est une ligue connue à l'internationale où tout les combattants pokémon s'affrontent pour savoir qui est le meilleur dresseur, ça t'intéresse ?")
			print(f"Que voulez vous faire :")
			print("1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
			response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
			while not response_2 in (1,2):
				print(f"Veuillez saisir un nombre correct")
				print("1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
				response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
			#branche 1-1 (il accepte le défi de devenir dresseur) 
			if int(response_2) == 1:
				print(f"{prenom_1} : Oui je veux entrer dans le monde Pokémon !")
				print(f"Homme mystérieux : Très bien alors il est temps de choisir ton premier pokémon !")
		#Branche 1-2 (il renonce au défi fin du jeu) 
			elif int(response_2) == 2:
				print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
				quit()
		elif int(response_4)== 2:
				print(f"{prenom_1} : Non désolé je suis trop occupé, à la prochaine")
				print(f"Vous regretterez sans doute ce choix...")
				amitié += 1
				print(f"Attiré par les bruits de la foule, vous vous rapprochez")
				print(f"Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
				print(f"Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
				print(f"{prenom_1} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
				print(f"Homme mystérieux : Je viens visiter mon village natal, tu ne me connais pas ? ")
				print(f"{prenom_1} : Non! Qui êtes-vous ?")
				print(f"Homme mystérieux : Je suis le tout nouveau maitre Pokémon. Je viens de gagner le combat final de la ligue Pokémon")
				print(f"{prenom_1} : La ligue Pokémon ? C'est quoi ? ")	
				print(f"Homme mystérieux : Tu ne connais pas la ligue Pokémon ?")
				print(f"{prenom_1} : Non, c'est quoi ?")
				print(f"Homme mystérieux : C'est une ligue connue à l'internationale où tout les combattants pokémon s'affrontent pour savoir qui est le meilleur dresseur, ça t'intéresse ?")
				print(f"Que voulez vous faire :")
				print("1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
				response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
				if int(response_2) == 1:
					print(f"{prenom_1} : Oui je veux entrer dans le monde Pokémon !")
					print(f"Homme mystérieux : Très bien alors il est temps de choisir ton premier pokémon !")
				elif int(response_2) == 2:
					print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
					quit()
	elif int(response_3)== 2:
		print(f"{prenom_1} : Non désolé je suis trop occupé, à la prochaine")
		print(f"Vous regretterez sans doute ce choix...") 
		amitié += 1
		print(f"Attiré par les bruits de la foule, vous vous rapprochez")
		print(f"Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
		print(f"Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
		print(f"{prenom_1} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
		print(f"Homme mystérieux : Je viens visiter mon village natal, tu ne me connais pas ? ")
		print(f"{prenom_1} : Non! Qui êtes-vous ?")
		print(f"Homme mystérieux : Je suis le tout nouveau maitre Pokémon. Je viens de gagner le combat final de la ligue Pokémon")
		print(f"{prenom_1} : La ligue Pokémon ? C'est quoi ? ")	
		print(f"Homme mystérieux : Tu ne connais pas la ligue Pokémon ?")
		print(f"{prenom_1} : Non, c'est quoi ?")
		print(f"Homme mystérieux : C'est une ligue connue à l'internationale où tout les combattants pokémon s'affrontent pour savoir qui est le meilleur dresseur, ça t'intéresse ?")
		print(f"Que voulez vous faire :")
		print("1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
		response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		if int(response_2) == 1:
			print(f"{prenom_1} : Oui je veux entrer dans le monde Pokémon !")
			print(f"Homme mystérieux : Très bien alors il est temps de choisir ton premier pokémon !")
		elif int(response_2) == 2:
			print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
			quit()
#le jouer fait son premier combat tutoriel 
print(f"oe entraine toi pour voir si tu merites un de mes pokemon")
while hppokefightinitial > 0:
	print(f"le pokemon adverse a {hppokefightinitial} points de vie, quel voulez vous faire ? n\1) Attaquer n\2) Se soigner n\3) Changer de pokémon")
	choix=int(input("choisissez le bon numéro "))
	while not choix in (1,2,3):
		print(f"Veuillez saisir un nombre correct")
		print(f"le pokemon adverse a {hppokefightinitial} points de vie, quel voulez vous faire ? n\1) Attaquer n\2) Se soigner n\3) Changer de pokémon")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? n/1)Nom attaque 1 (-15 hp) {nbrattaque1}/15 n/2)Nom attaque 2 (-10 hp) {nbrattaque2}/20 n/1)Nom attaque 3 (-20 hp) {nbrattaque3}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbrattaque1 > 0:
				hppokefightinitial = hppokefightinitial - 15 
				nbrattaque1 = nbrattaque1 - 1
			else:
				print("Vous n'avez plus d'attaque 1 veuillez en chosir une autre ")
		elif quelle_attaque == 2: 
			if nbrattaque2 > 0:
				hppokefightinitial = hppokefightinitial - 10 
				nbrattaque2 = nbrattaque2 - 1
			else:
				print("Vous n'avez plus d'attaque 2 veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbrattaque3 > 0:
				hppokefightinitial = hppokefightinitial - 20 
				nbrattaque3 = nbrattaque3 - 1
			else:
				print("Vous n'avez plus d'attaque 3 veuillez en chosir une autre ")
	elif choix == 2: 
		print("Quelle objet pour se soigner ? n\1)super potion n\2)hyper potion ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2):
			print(f"Veuillez saisir un nombre correct")
			print("Quelle objet pour se soigner ? n\1)super potion n\2)hyper potion ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			hp_poke_joueur = hp_poke_joueur + 20
			nbr_superpotion -= 1
		elif choixsoin == 2: 
			hp_poke_joueur = 60 
			nbr_hyperpotion -= 1
	else: 
		print("tu n'as pas le droit")
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
print("Bravo ! Tu as gagné ton premier combat (tu ne pouvais pas perdre donc prend pas trop la confiance sale merde")
print("homme mystérieux : Tu es maintenant un dresseur pokémon ! Différents choix s'offrent à toi. Tu peux par exemple partir pour les arènes pokémons pour essayer de gagner des récompenses et faire évoluer ton pokémon")
print("homme mystérieux : tu peux aussi partir pour la forêt pangorn à proximité pour obtenir de nouveaux pokémons mais fais attention à prendre des pokéballs avec toi")
print("homme mystérieux : il existe de nombreuses villes à proximité si l'envie t'ne prends de faire du tourisme")
print("homme mystérieux : Tu peux même si tu le souhaites explorer les environs")
print(f"mais d'abord choisis un de mes pokémons : ")
print("Homme mystérieux : Alors, quel Pokémon t'acompagneras dans ton aventure vers la ligue Pokémon ?\n1) Arcko (Type Plante)\n2) Poussifeu (Type Feu)\n3)Gobou (Type Eau)")
starter = int(input("Quel Pokémon choisissez vous ? (sélectionnez le numéro correspondant) : "))
while not Poké_dep_choix in {1,2,3} : 
    print("Vous vous êtes trompés de numéro")
    print("Homme mystérieux : Alors, quel Pokémon t'acompagneras dans ton aventure vers la ligue Pokémon ?\n1) Arcko (Type Plante)\n2) Poussifeu (Type Feu)\n3)Gobou (Type Eau)")
	starter = int(input("Quel Pokémon choisissez vous ? (sélectionnez le numéro correspondant) : "))
if starter == 1:
    print("Arcko a été ajouté à ton Pokédex !")
    print("Arcko est un pokémon de type Plante, cela veut dire qu'il sera très éfficace face aux Pokémons de type Eau, Roche et Sol !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
elif starter == 2:
    print("Poussifeu a été ajouté à ton Pokédex !")
    print("Poussifeu est un pokémon de type Feu, cela veut dire qu'il sera très éfficace face aux Pokémons de type Plante et Glace !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
elif starter == 3:
    print("Gobou a été ajouté à ton Pokédex !")
    print("Gobou est un pokémon de type Eau, cela veut dire qu'il sera très éfficace face aux Pokémons de type Feu, Roche et Sol !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
print(f"très bon choix ! Maintenant tu es prêt à visiter l'île, profite de ton aventure.")
while chemins:
    print("\nChemins disponibles :")
    for numero, (nom, _) in chemins.items():
        print(f"{numero} - {nom}")

    choix = input("Choisis un chemin : ") 

    if choix in chemins:
        nom, fonction = chemins[choix]
        print(f"\nTu as choisi : {nom}\n")
        fonction()  #  Lance la fonction liée
        del chemins[choix]  #  Supprime le chemin
    else:
        print("Choix invalide, fais un effort !")

print("\n Game Over ! ")
