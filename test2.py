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
# Dictionnaire des chemins : clé = choix, valeur = (nom, fonction) 
chemins = {
    "1": ("Ville Donjon", ville_donjon),
    "2": ("La forêt Pangorn", forêt_pangorn),
    "3": ("Les arênes Pokémon", arènes_pokémons),
    "4": ("Le Volcan instable de l'île", grotte_boss)
}
# Dictionnaire de combat
pokedex = {}
pv_team = {}
pv_max = {}
#Liste de team
team = []
inventaire = {
    "nbr_superpotion": 3,
    "nbr_hyperpotion": 1,
    "nbr_pokeball": 5,
    "nbr_superball": 2,
    "nbr_hyperball": 1
}
pokedex = {}
etat_combat = {
    "pv": pv_team[actif],                   
    "pp": pp_par_pokemon[actif],             
    "objets": inventaire_global,
    "hp_ennemi": hp_ennemi,
    "nom_ennemi": nom_poke_ennemi
}
pv_team = {
    "Gobou": 60,
    "Poussifeu": 60,
    "Arcko": 60
}
pp_par_pokemon = {
    "Gobou": {
        "Pistolet à O": 15,
        "Hydrocanon": 10,
        "Siphon": 20
    },
    "Poussifeu": {
        "Flammèche": 15,
        "LanceFlamme": 20,
		"Rebondifeu": 10
    },
    "Arcko": {
        "Désherbaffe": 15,
        "FouetsLiannes": 20,
		"LammeFeuille": 10
    }
}
params_Poke = {
    "nbr_Pistolet_à_O": 15,
    "nbr_Hydrocanon": 10,
    "nbr_Siphon": 20,
    "pv_max": 70
}
ajouter_pokemon("Gobou", menu_combat_gobou, params_Gobou)
def ajouter_pokemon(pokemon_nom, menu_combat, params_pokemon):
    # 1) Ajout au pokedex
    pokedex[pokemon_nom] = {
        "fonction": fonction_combat,
        "parametres": params_pokemon
    }
    
    # 2) Initialisation PV
    pv_max[pokemon_nom] = params_pokemon.get("pv_max", 60)  # default 60 si non fourni
    pv_team[pokemon_nom] = pv_max[pokemon_nom]
    
    # 3) Ajout à la team si moins de 6
    if len(team) < 6:
        team.append(pokemon_nom)
        print(f"{pokemon_nom} a été ajouté à votre équipe !")
    else:
        print(f"{pokemon_nom} est ajouté à votre réserve (pokedex), mais votre équipe est pleine.")

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
#fonction boutique
def boutique (monnaie,nbr_pokeball,nbr_superball,nbr_hyperball,nbr_superpotion,nbr_hyperpotion):
	print(f" accueil : Bienvenue à la boutique que souhaitez vous acheter ?")
	print(f"\n1)acheter des Pokéballs\n2)acheter des potions")
	achat_boutique = int(input("\nQue choisissez vous ? (sélectionnez le bon numéro) : ")) 
	if achat_boutique == 1:
		print(f"Quelle type de pokéball voulez-vous acheter ?")
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
def menu_combat_arcko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_poke_joueur,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Fuir \n4) Pokéballs\n5) Changer de Pokemon")
	choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-15 hp) {nbr_Désherbaffe}/15 \n 2)Fouets Liannes (-10 hp) {nbr_FouetsLiannes}/20 \n 3)Lame Feuille (-20 hp) {nbr_LammeFeuille}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Désherbaffe > 0:
				hp_ennemi -= 15 
				nbr_Désherbaffe -= 1
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
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Fuir \n4) Pokéballs\n5) changer de Pokemon")
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
	
def menu_combat_poussifeu (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_poke_joueur,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Fuir \n4) Pokéballs\n5) changer de Pokemon")
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


def gérer_equipe():
    # Tous les Pokémon capturés = clés du pokedex
    tous_les_pokemon = list(pokedex.keys())

    # Réserve = pokémon capturés mais pas dans l'équipe
    reserves = [p for p in tous_les_pokemon if p not in team]

    if len(reserves) == 0:
        print("Vous n'avez aucun Pokémon en réserve.")
        return

    print("\n=== Pokémon de l'équipe (max 6) ===")
    for i, poke in enumerate(team):
        print(f"{i+1}) {poke} (PV : {pv_team[poke]}/{pv_max[poke]})")

    print("\n=== Pokémon en réserve ===")
    for i, poke in enumerate(reserves):
        print(f"{i+1}) {poke} (PV : {pv_team[poke]}/{pv_max[poke]})")

    print("\nQuel Pokémon voulez-vous retirer de votre équipe ?")
    while True:
        choix_team = int(input("Numéro à retirer : ")) - 1
        if 0 <= choix_team < len(team):
            poke_sortant = team[choix_team]
            break
        else:
            print("Choix invalide.")

    print("\nQuel Pokémon de la réserve voulez-vous ajouter ?")
    while True:
        choix_reserve = int(input("Numéro à ajouter : ")) - 1
        if 0 <= choix_reserve < len(reserves):
            poke_entrant = reserves[choix_reserve]
            break
        else:
            print("Choix invalide.")

    team[choix_team] = poke_entrant

    print(f"\n{poke_sortant} a été envoyé dans la réserve.")
    print(f"{poke_entrant} a rejoint votre équipe !\n")


def boucle_combat(hp_ennemi, nom_poke_ennemi):
    # Copie temporaire de l'équipe pour ce combat
    team_combat = team.copy()
	
    while hp_ennemi > 0 and Fuir = False and poké_pop_compteur % 2 == 0 and any(pv_team[poke] > 0 for poke in team_combat):
        actif = team_combat[0]   # Pokémon actif

        # Appel du menu de combat correspondant au Pokémon actif
        pokedex[actif](etat_combat)

        # Attaque du Pokémon ennemi
		print("Au tour du pokémon adverse de jouer ! ")
		if hp_ennemi > 10: 
			attaque_ennemi = random.randint(1,4)
			if attaque_ennemi == 1:
				pv_team[actif] -= 10
				print(f"{nom_poke_ennemi} vous a infligé 20 dégats. Vous avez {pv_team[actif]} points de vie.")
			elif attaque_ennemi == 2:
				pv_team[actif] -= 20
				print(f"{nom_poke_ennemi} vous a infligé 15 dégats. Vous avez {pv_team[actif]} points de vie.")
			else:
				pv_team[actif] -= 15
				print(f"{nom_poke_ennemi} vous a infligé 10 dégats. Vous avez {pv_team[actif]} points de vie.")
		else: 
			attaque_ou_soin = random.randint(1,4)
			if attaque_ou_soin == 1:
				hp_ennemi += 15
				print(f"{nom_poke_ennemi} s'est soigné et a {hp_ennemi} points de vie.")
			else: 
				attaque_ennemi_2 = random.randint(1,4)
				if attaque_ennemi_2 == 1:
					pv_team[actif] -= 10
					print(f"{nom_poke_ennemi} vous a infligé 20 dégats. Vous avez {pv_team[actif]} points de vie.")
				elif attaque_ennemi_2 == 2:
					pv_team[actif] -= 20
					print(f"{nom_poke_ennemi} vous a infligé 15 dégats. Vous avez {pv_team[actif]} points de vie.")
				else:
					pv_team[actif] -= 15
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

ajouter_pokemon(Poussifeu, menu_combat_poussifeu, params_Poussifeu)
ajouter_pokemon(Arcko, menu_combat_arcko, params_Arcko)
boucle_combat(30, Pikkachu)




 
