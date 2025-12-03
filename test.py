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
#fonction boutique
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
            else:
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
			changer_pokemon()
			
def menu_combat_arcko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_poke_joueur,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs \n5) Fuir")
	choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-15 hp) {nbr_Désherbaffe}/15 \n 2)Fouets Liannes (-10 hp) {nbr_FouetsLiannes}/20 \n 3)Lame Feuille (-20 hp) {nbr_LammeFeuille}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Désherbaffe > 0:
				hp_ennemi -= 15 
				nbr_Désherbaffe - = 1
			else:
				print("Vous n'avez plus de Pistolet à O, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_FouetsLiannes > 0:
				hp_ennemi -= 10 
				nbr_FouetsLiannes -= 1
			else:
				print("Vous n'avez plus de Siphon, faites attention la prochaine fois ")
		elif quelle_attaque == 3: 
			if nbr_LammeFeuille > 0:
				hp_ennemi -= 20 
				nbr_LammeFeuille -= 1
			else:
				print("Vous n'avez plus de Hydrocanon, faites attention la prochaine fois ")
	elif choix == 2: 
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
			if reponse_pp == 1: 
				nbr_Désherbaffe = 15
			elif reponse_pp == 2: 
				nbr_FouetsLiannes = 20
			else: 
				nbr_LammeFeuille = 10
	elif choix == 3:
            fuir = False
            print("Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	elif choix == 4: 
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
		changer_pokemon()
		
def menu_combat_gobou (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_poke_joueur,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
	choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-15 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-10 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-20 hp) {nbr_Hydrocanon}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Pistolet_à_O > 0:
				hp_ennemi -= 15 
				nbr_Pistolet_à_O - = 1
			else:
				print("Vous n'avez plus de Pistolet à O, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_Siphon > 0:
				hp_ennemi -= 10 
				nbr_Siphon -= 1
			else:
				print("Vous n'avez plus de Siphon, faites attention la prochaine fois ")
		elif quelle_attaque == 3: 
			if nbr_Hydrocanon > 0:
				hp_ennemi -= 20 
				nbr_Hydrocanon -= 1
			else:
				print("Vous n'avez plus de Hydrocanon, faites attention la prochaine fois ")
	elif choix == 2: 
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
			if reponse_pp == 1: 
				nbr_Pistolet_à_O = 15
			elif reponse_pp == 2: 
				nbr_Siphon = 20
			else: 
				nbr_Hydrocanon = 10
	elif choix == 3:
            fuir = False
            print("Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	elif choix == 4: 
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
		changer_pokemon()

def capture_pokemon(nom_pokemon, pv_max_pokemon, menu_combat_pokemon):
    # PV
    if nom_pokemon not in pv_max:
        pv_max[nom_pokemon] = pv_max_pokemon
        pv_team[nom_pokemon] = pv_max_pokemon
        print(f"{nom_pokemon} ajouté aux PV !")
    else:
        print(f"{nom_pokemon} est déjà dans vos PV.")

    # Pokédex
    if nom_pokemon not in pokedex:
        pokedex[nom_pokemon] = menu_combat_pokemon
        print(f"{nom_pokemon} ajouté au Pokédex !")
    else:
        print(f"{nom_pokemon} est déjà dans votre Pokédex.")

    # Équipe
    if nom_pokemon in team:
        print(f"{nom_pokemon} est déjà dans votre équipe.")
    elif len(team) < 6:
        team.append(nom_pokemon)
        print(f"{nom_pokemon} ajouté à votre équipe !")
    else:
        print(f"Ton équipe est pleine, {nom_pokemon} a été ajouté au Pokédex mais pas à l'équipe.")

pokedex = {}
pv_team = {}
pv_max = {}
team = []

def boucle_combat(hp_ennemi, nom_poke_ennemi):
    # Copie temporaire de l'équipe pour ce combat
    team_combat = team.copy()
	
    while hp_ennemi > 0 and Fuir = False and poké_pop_compteur % 2 == 0 and any(pv_team[poke] > 0 for poke in team_combat):
        actif = team_combat[0]   # Pokémon actif

        # Appel du menu de combat correspondant au Pokémon actif
        pokedex[actif](nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, hp_ennemi, pv_team[actif], nbr_superpotion, nbr_hyperpotion, nbr_pokeball, nbr_superball, nbr_hyperball)

        # Attaque du Pokémon ennemi
		print("Au tour du pokémon adverse de jouer ! ")
		if hp_ennemi > 10: 
			attaque_ennemi = random.randint(1,4)
			if attaque_ennemi == 1:
				pv_team[actif] -= 20
				print(f"{nom_poke_ennemi} vous a infligé 20 dégats. Vous avez {pv_team[actif]} points de vie.")
			elif attaque_ennemi == 2:
				pv_team[actif] -= 15
				print(f"{nom_poke_ennemi} vous a infligé 15 dégats. Vous avez {pv_team[actif]} points de vie.")
			else:
				pv_team[actif] -= 10
				print(f"{nom_poke_ennemi} vous a infligé 10 dégats. Vous avez {pv_team[actif]} points de vie.")
		else: 
			attaque_ou_soin = random.randint(1,4)
			if attaque_ou_soin == 1:
				hp_ennemi += 15
				print(f"{nom_poke_ennemi} s'est soigné et a {hp_ennemi} points de vie.")
			else: 
				attaque_ennemi_2 = random.randint(1,4)
				if attaque_ennemi_2 == 1:
					pv_team[actif] -= 20
					print(f"{nom_poke_ennemi} vous a infligé 20 dégats. Vous avez {pv_team[actif]} points de vie.")
				elif attaque_ennemi_2 == 2:
					pv_team[actif] -= 15
					print(f"{nom_poke_ennemi} vous a infligé 15 dégats. Vous avez {pv_team[actif]} points de vie.")
				else:
					pv_team[actif] -= 10
					print(f"{nom_poke_ennemi} vous a infligé 10 dégats. Vous avez {pv_team[actif]} points de vie.")
		
		# Vérifier si le Pokémon actif est K.O.
        if pv_team[actif] <= 0:
            print(f"{actif} est K.O. !")
            team_combat.pop(0)  # On retire le Pokémon actif du combat temporaire
            if not team_combat:
                print("Tous vos Pokémon sont K.O. !")
                break

    # Remise full HP après combat
    for poke in team:
        pv_team[poke] = pv_max[poke]
    	print("Tous vos Pokémon ont été remis à full PV !")

def changer_pokemon():
    if len(team) <= 1:
        print("Vous n'avez qu'un seul Pokémon dans votre équipe, impossible de changer.")
        return

    print("Choisissez le Pokémon actif :")
    for i, poke in enumerate(team):
        print(f"{i + 1}) {poke} (PV: {pv_team[poke]}/{pv_max[poke]})")

    while True:
        choix = int(input("Entrez le numéro du Pokémon que vous voulez mettre actif : ")) - 1
        if 0 <= choix < len(team):
            if choix == 0:
                print(f"{team[0]} est déjà actif !")
            else:
                # Échanger le Pokémon choisi avec le premier de la liste
                team[0], team[choix] = team[choix], team[0]
                print(f"{team[0]} est maintenant le Pokémon actif !")
            break
        else:
            print("Numéro invalide, réessayez.")
			
def soigner_team():
    for poke in team:
        pv_team[poke] = pv_max[poke]
    print("Tous vos Pokémon ont été soignés et sont maintenant à pleine vie !")








