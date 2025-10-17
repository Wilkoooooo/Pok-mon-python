import random. 
from math import * 
#Introduction
print ("Homme mystérieux : Bonjour jeune homme! Tu es perdu(e)? Tu ne devrais pas te promener seul(e) dans la forêt si tard le soir ! Il y a des rumeurs comme quoi cette forêt abrite les Pokemons les plus dangereux.")
print("Homme mystérieux : Comment t'appelles tu ? ") 
prenom_1 = input("Indiquez votre nom :")
print("Homme mystérieux : Viens {prenom_1}, je vais te ramener chez tes parents, c'est dangereux ici !")
print("10 jours plus tard, alors que vous vous promenez dans Perdium, vous croisez une foule entourant le'homme que vous aviez croisez dans la forêt.") 

#Premier choix 
print("Que voulez vous faire :")
print("1)Aller voir la foule de plus près\n 2)Partir dans le sens opposé") 
response_1 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))

#Branche 1 
if int(response_1) == 1:
	print("Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
	print("Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
	print("{prenom_1} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
	print("Je viens visiter mon village natal, tu ne me connais pas ? ")
	print("Non! Qui êtes-vous ?")
