import random 
from math import * 
#variables de tout le programme :
monnaie = 0
XP = 0

#Introduction
print(f"Homme mystérieux : Bonjour jeune homme! Tu es perdu ? Tu ne devrais pas te promener seul dans la forêt si tard le soir ! Il y a des rumeurs comme quoi cette forêt abrite les Pokemons les plus dangereux.")
print(f"Homme mystérieux : Comment t'appelles tu ? ") 
prenom_1 = input("Indiquez votre nom :")
print(f"Homme mystérieux : Viens {prenom_1}, je vais te ramener chez tes parents, c'est dangereux ici !")
print(f"10 jours plus tard, alors que vous vous promenez dans Perdium, vous croisez une foule entourant l'homme que vous aviez croisé dans la forêt.") 

#Premier choix 
print("Que voulez vous faire :")
print("1)Aller voir la foule de plus près\n2)Partir dans le sens opposé") 
response_1 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))

#Branche 1 
if int(response_1) == 1:
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
#branche 1-1
	if int(response_2) == 1:
		print(f"{prenom_1} : Oui je veux entrer dans le monde Pokémon !")
		print(f"Homme mystérieux : Très bien alors il est temps de choisir ton premier pokémon !")
#Branche 1-2
	elif int(response_2) == 2:
		print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
		quit()
#Branche 2
elif int(response_1) == 2: 
	print("Quelqu'un vous tape à l'épaule et vous vous retournez")
	print("jeune garçon : Salut comment tu t'appelles ? Tu es nouveau ici ?")
	print("Que voulez vous faire :")
	print("1)Faire connaissance\n2)L'ignorer") 
	response_3
	= int(input("Que choisissez vous ? (sélectionnez le numéro) : "))

	
	print(f"{prenom_1} : Je m'appelle {prenom_1} 

#Branche 
#Choix Pokémon de départ 
print("Homme mystérieux : Alors, quel Pokémon t'acompagneras dans ton aventure vers la ligue Pokémon ?\n1) Arcko (Type Plante)\n2) Poussifeu (Type Feu)\n3)Gobou (Type Eau)")
Poké_dep_choix = int(input("Quel Pokémon choisissez vous ? (sélectionnez le numéro correspondant) : "))
if Poké_dep_choix == 1:
	print("Arcko a été ajouté à ton Pokédex !")
elif Poké_dep_choix == 2:
	print("Poussifeu a été ajouté à ton Pokédex !")
elif Poké_dep_choix == 3:
	print("Gobou a été ajouté à ton Pokédex ! ")

