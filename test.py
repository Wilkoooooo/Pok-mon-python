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
			reponse_pp=int(input(f"Quel attaque choisissez vous ?")
			if reponse_pp == 1: 
				nbr_Flammèche = nbr_Flammèche - nbr_Flammèche + 15
			elif reponse_pp == 2: 
				nbr_Lance-Flammes = nbr_Lance-Flammes - nbr_Lance-Flammes + 20
			elif reponse_pp == 3: 
				nbr_Rebondifeu = nbr_Rebondifeu - nbr_Rebondifeu + 10
  elif choix == 3:
    print("tu n'as pas le droit on a pas encore coder cette partie et on le fera probablement jamais")
  elif choix == 4: 
    print(f"Quel Pokeball veux-tu utiliser ?\n1) Pokéball ({nbr_pokeball})\n2) Superball ({nbr_superball})\n3) Hyperball ({nbr_hyperball})")
    choix_pokeball = int(input("Choisis le bon numéro (1,2,3)")
    if choix_pokeball == 1 
      if nbr_pokeball > 0: 
				nbr_pokeball = nbr_pokeball - 1
        print("Vous lancez une Pokéball !")
        for i in range (3):
          n=0
          proba_poké_pop=random.randint(1,5+i)
          if proba_poké_pop == 5:
            print(f"La pokéball a pop à la secousse numéro {i+1}!")
            break
          else :
            print(f"La pokéball n'a pas pop à la secousse numéro {i+1}!")
            n=n+1
        if n % 2 != 0:
          print("le pokémon a été capturé. Bravo !")
      else:
				print("Vous n'avez plus de Pokeball c'était pourtant écrit... veuillez faire attention la prochaine fois !")     
  else:
    print("tu n'as pas le droit on a pas encore coder cette partie et on le fera probablement jamais")
    
