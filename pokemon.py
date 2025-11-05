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

#Branche 1 (direct foule) 
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
	#branche 1-1 (il accepte le défi de devenir dresseur) 
	if int(response_2) == 1:
		print(f"{prenom_1} : Oui je veux entrer dans le monde Pokémon !")
		print(f"Homme mystérieux : Très bien alors il est temps de choisir ton premier pokémon !")
	#Branche 1-2 (il renonce au défi fin du jeu) 
	elif int(response_2) == 2:
		print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
		quit()
#Branche 2 (il va dans l'autre sens et rencontre son meilleur pote) 
elif int(response_1) == 2: 
	print(f"Quelqu'un vous tape à l'épaule et vous vous retournez")
	print(f"jeune garçon : Salut comment tu t'appelles ? Tu es nouveau ici ?")
	print(f"Que voulez vous faire :")
	print(f"1)Faire connaissance\n2)L'ignorer") 
	response_3 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	if int(response_3)== 1:
		print(f"{prenom_1} : Je m'appelle {prenom_1}, je suis de retour ici, et toi comment tu t'appelles?")
		print(f"jeune garçon : Je m'appelle Victor, ça te dit qu'on devienne potes?")
		print(f"Que voulez vous faire :")
		print(f"1)devenir amis\n2)Le repousser")
		response_4 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		if int(response_4)== 1:
			print(f"{prenom_1} : Oui bien sûr, ça te dit qu'on se rapproche de la foule ?")
			print(f"Vous vous rapprochez de la foule")
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

print("Homme mystérieux : Alors, quel Pokémon t'acompagneras dans ton aventure vers la ligue Pokémon ?\n1)Arcko (Type Plante)\n2)Poussifeu (Type Feu)\n3)Gobou (Type Eau)")
Poké_dep_choix = int(input("Quel Pokémon choisissez vous ? (sélectionnez le numéro correspondant) : "))
print("Homme mystérieux : Alors, quel Pokémon t'acompagneras dans ton aventure vers la ligue Pokémon ?\n1) Arcko (Type Plante)\n2) Poussifeu (Type Feu)\n3)Gobou (Type Eau)")
Poké_dep_choix = int(input("Quel Pokémon choisissez vous ? (sélectionnez le numéro correspondant) : "))
while not Poké_dep_choix in {1,2,3} : 
    print("Vous vous êtes trompés de numéro")
    print("Homme mystérieux : Alors, quel Pokémon t'acompagneras dans ton aventure vers la ligue Pokémon ?\n1) Arcko (Type Plante)\n2) Poussifeu (Type Feu)\n3)Gobou (Type Eau)")
    Poké_dep_choix = int(input("Quel Pokémon choisissez vous ? (sélectionnez le numéro correspondant) : "))
if Poké_dep_choix == 1:
    print("Arcko a été ajouté à ton Pokédex !")
    print("Arcko est un pokémon de type Plante, cela veut dire qu'il sera très éfficace face aux Pokémons de type Eau, Roche et Sol !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
elif Poké_dep_choix == 2:
    print("Poussifeu a été ajouté à ton Pokédex !")
    print("Poussifeu est un pokémon de type Feu, cela veut dire qu'il sera très éfficace face aux Pokémons de type plante et Glace !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
elif Poké_dep_choix == 3:
    print("Gobou a été ajouté à ton Pokédex !")
    print("Gobou est un pokémon de type Eau, cela veut dire qu'il sera très éfficace face aux Pokémons de type Feu, Roche et Sol !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")

