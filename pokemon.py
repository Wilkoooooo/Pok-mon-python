import random. 
from math import * 
#variables de tout le programme :
monnaie = 0
XP = 0

#Introduction
print ("Homme mystérieux : Bonjour jeune homme! Tu es perdu(e)? Tu ne devrais pas te promener seul(e) dans la forêt si tard le soir ! Il y a des rumeurs comme quoi cette forêt abrite les Pokemons les plus dangereux.")
print("Homme mystérieux : Comment t'appelles tu ? ") 
prenom_1 = input("Indiquez votre nom : ")
print("Homme mystérieux : Viens {prenom_1}, je vais te ramener chez tes parents, c'est dangereux ici !")
print("10 jours plus tard, alors que vous vous promenez dans Perdium, vous croisez une foule entourant le'homme que vous aviez croisez dans la forêt.") 

#Premier choix 
print("Que voulez vous faire : ")
print("1)Aller voir la foule de plus près\n 2)Partir dans le sens opposé") 
response_1 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))

#Branche 1 
if int(response_1) == 1:
	print("Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
	print("Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
	print("{prenom_1} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
	print("Homme mystérieux : Je viens visiter mon village natal, tu ne me connais pas ? ")
	print("{prenom_1} : Non! Qui êtes-vous ?")
	print("Homme mystérieux : Je suis le tout nouveau maitre Pokémon. Je viens de gagner le combat final de la ligue Pokémon")
	print("{prenom_1} : La ligue Pokémon ? C'est quoi ? ")	
	print("Homme mystérieux : Tu ne connais pas la ligue Pokémon ?")
	print("{prenom_1} : Non, c'est quoi ?")
	print("Homme mystérieux : C'est une ligue connue à l'internationale où tout les combattants pokémon s'affrontent pour savoir qui est le meilleur dresseur, ça t'intéresse ?")
	print("Que voulez vous faire : ")
	print("1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
	response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
#branche 1-1
	if int(response_2) == 1:
		print("Oui je veux entrer dans le monde Pokémon !")
		print("Homme mystérieux : Très bien alors il est temps de choisir ton premier pokémon !")
	elif int(response_2) == 2:
		print("Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
		quit()
#Branche 2
elif int(response_1) == 2: 
	print("Ash : ")

#Branche 
#Choix Pokémon de départ 
Print("Homme mystérieux : Alors, quel Pokémon t'acompagneras dans ton aventure vers la ligue Pokémon ?\n1) Arcko (Type Plante)\n2) Poussifeu (Type Feu)\n3)Gobou (Type Eau)")
Poké_dep_choix = int(input("Quel Pokémon choisissez vous ? (sélectionnez le numéro correspondant) : "))
if Poké_dep_choix == 1:
	Poké_ini = Arcko
	print(f"{Poké_ini} a été ajouté à ton Pokédex !")
	print(f"Stats pokemon") 
elif Poké_dep_choix == 2:
	Poké_ini = Poussifeu
	print(f"{Poké_ini} a été ajouté à ton Pokédex !")
	print(f"Stats pokemon") 
elif Poké_dep_choix == 3:
	Poké_ini = Gobou
	print(f"{Poké_ini} a été ajouté à ton Pokédex ! ")
	print(f"Stats pokemon") 
print(f"Homme mystérieux : Bravo ! Tu viens d'obtenir ton tout premier Pokémon, ton aventure va enfin pouvoir commencer. Cependant tu dois savoir plusieurs choses avant de te lacer dans ton aventure.\nPremièrement, ")

