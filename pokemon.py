import random 
from math import * 
#variables de tout le programme :
monnaie = 50
XP = 0
hp_poke_joueur = 60 
hppokefightinitial = 50 
nbr_Flammèche = 15
nbr_Lance-Flammes = 20
nbr_Rebondifeu = 10
nbr_Pistolet_à_O = 15
nbr_Siphon = 20
nbr_Hydrocanon = 10

def menu_combat_gobou ():
	print(f"le pokemon adverse a {hppokefightinitial} points de vie, quel voulez vous faire ? \n 1) Attaquer \n 2) Se soigner \n 3) Changer de pokémon")
	choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-15 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-10 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-20 hp) {nbr_Hydrocanon}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Pistolet_à_O > 0:
				hppokefightinitial = hppokefightinitial - 15 
				nbr_Pistolet_à_O = nbr_Pistolet_à_O - 1
			else:
				print("Vous n'avez plus de Pistolet à O, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_Siphon > 0:
				hppokefightinitial = hppokefightinitial - 10 
				nbr_Siphon = nbr_Siphon - 1
			else:
				print("Vous n'avez plus de Siphon, faites attention la prochaine fois ")
		elif quelle_attaque == 3: 
			if nbr_Hydrocanon > 0:
				hppokefightinitial = hppokefightinitial - 20 
				nbr_Hydrocanon = nbr_Hydrocanon - 1
			else:
				print("Vous n'avez plus de Hydrocanon, faites attention la prochaine fois ")
	elif choix == 2: 
		print("Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			hp_poke_joueur = hp_poke_joueur + 20
		elif choixsoin == 2: 
			hp_poke_joueur = 60 
		elif choixsoin == 3:  
			print("Sur quelle attaque : \n1)Pistolet à O  (-15 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-10 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-20 hp) {nbr_Hydrocanon}/10 ")
			reponse_pp=int(input(f"Quel attaque choisissez vous ?")
			if reponse_pp == 1: 
				nbr_Pistolet_à_O = nbr_Pistolet_à_O - nbr_Pistolet_à_O + 15
			elif reponse_pp == 2: 
				nbr_Siphon = nbr_Siphon - nbr_Siphon + 20
			elif reponse_pp == 3: 
				nbr_Hydrocanon = nbr_Hydrocanon - nbr_Hydrocanon + 10
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
def choix ():
	print("Que voulez vous faire :")
	print("1)Partir pour les arènes pokémons\n2)Explorer la forêt Pangorn\3)Visiter les villes à proximité\4)Explorer les environs") 
	response_7 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	while not response_7 in {1,2,3,4}
	print("vous vous êtes trompées de numéro")
	choix ()
	if response_7 == 1 :
		arènes_pokémons():
	if response_7 == 2 :
		forêt_pangorn ():
	if response_7 == 3 :
		ville_donjon ():
	if response_7 == 4 :
		grotte_boss ():


def arènes_pokémons ():
		print("Vous arrivez à présent aux arènes pokémons espérant gagner de nombreuses récompenses et faire évoluer vos pokémons")
		print("quelqu'un à l'entrée de l'arène vous attend pour vous expliquer les règles de l'arène pokémon")
		print("organisateur : Bonjour jeune homme, vous êtes arrivé à l'arène pokémon, ici de nombreux dresseurs s'affrontent en espérant atteindre la finale du tournoi pour gagner un pokémon rarissime !")
		print("organisateur : Le fonctionnement est très simple, vous démarrez quand 32 dresseurs pokémons arrivent dans l'arène et dès que vous perdez vous devez attendre le prochain tournoi, par contre à chaque fois que vous gagnez vous passez à l'étape supérieure et vous affrontez de noueaux dresseurs. Vous avez le droit d'utliser des potions de soins sur vos pokémons seulement entre chaque combat; Bonne chance !")
		print("Organisateur : Alors ça te tente ?")
		print("Que voulez vous faire :")
		print("1)S'inscrire au tournoi\n2)partir de l'arène pokémon")
		response_8 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		if response_8 = 1:
			print("votre premer combat commence !")
		if response_8 = 2:
			print("Vous sortez des arènes pokémons")
			def choix ():

def forêt_pangorn ():
	print("Après quelques dizaines de minutes de marche, vous arrivez à l'entrée de la forêt Pangorn")
	print("{prenom_1} : j'entends de l'eau qui coule vers l'ouest. J'aprçois une lueur pas loin devant moi. J'entends aussi la terre qui tremble à quelques centaines de mètres à ma droite")
	print("Que voulez vous faire :")
	print("1)Se diriger vers les bruits de l'eau\n2)S'approcher de la lueur\n3)Se rendre aux lieux des tremblements de terre")
	response_9 : int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	if response_9 = 1 :
		print("Vous êtes émerveillé par une magnifique cascade cependant vous ne vous rendez même pas compte qu'un Crocodil vous observe")
		print("Le Crocodil vous saute dessus seulement vous le voyez au dernier moment et vus avez le choix entre esquiver en vous baissant ou en sautant vers la rivière")
		print("que voulez vous faire ?")
		print("1)esquiver en se baissant\n2)esquiver en sautant vers la rivière")
		response_10 : int(input("que choisissez vous ? (sélectionnez le numéro) : "))
		if response_10 = 1 :
			Croco_griffe = random.randint(1,2)
			if Croco_griffe == 1:
				print("Le crocodil vous érafle le dos mais vous êtes légèrment blessé, il va falloir soigner cela avant que ça ne s'infecte")
				print("Le Crocodil se dresse devant vous, préparez vous au combat !")
			
			if Croco_griffe == 2:
				print("vous avez esquivé de justesse, préparez vous au combat !")
		
		if response_10 = 2 :
		print(" Vous vous retrouvez au bord de la rivière et un léviator surgit et vous mange tout cru !")
		print("Game over")
		quit()
	
	if response_9 = 2 :
		print("Au fur et à mesure que vous vous approchez de la lumière vous sentez une odeur de brûlé")
		print("Que voulez vous faire ?")
		print("1)continuer à avancer\n2)faire demi-tour")
		response_11 : int(input("que choisissez vous ? (sélectionnez le numéro) : "))
		if response_11 = 1 :
			print("Vous avez trop avancé et vous êtes maintenant encerclés par des flammes. Vite il faut s'échapper !")
			print("En vous retournant vous vous retrouvez face à un ouisticram qui vous bloque le passage. Préparez-vous au combat !")
			
		if response_11 = 2 :
			print("Vous vous retrouvez à l'entrée de la forêt")
			print("Que voulez vous faire ?")
			print("1)quitter la forêt\n2)continuer d'explorer la forêt")
			response_12 : int(input("que choisissez vous ? (sélectionnez le numéro) : "))
			if response_12 = 1 :
				choix ():
			if response_12 = 2 :
				forêt_pangorn ():
	if response_9 = 3 :
		print("Vous vous rapprochez des tremblements de terre, et vous apercevez un onix mais il n'a pas l'air dans son état normal, il se tape contre une falaise...")
		print("cependant à cause des secousses vous trébuchez et vous vous retrouvez par terre")
		print("à cause des coups donnés par onix sur la falaise des rochers tombent droit sur vous !")
		print("Que voulez vous faire ?")
		print("1)se cacher derrière un arbre\n 2)plonger en avant")
		response_13 : int(input("que choisissez vous ? (sélectionnez le numéro) : "))
		if response_13 = 1:
			arbre = random.randint(1,4)
			if arbre = 1 :
				print("Un rocher vous à éraflé dans sa chute, vous êtes plutôt sérieusement blessé, il va falloir se rendre chez un médecin")
			else :
				print("Vous avez réussi à esquiver la chute de rochers, mais pourquoi le Onix est-il aussi intrigué par cette falaise ?")
				onix_secret()
		if response_13 = 2:
			print("vous vous êtes foulé la cheville mais vous avez esquivé la chute de rochers, cependant il va falloir se rendre chez un médecin")
			onix_secret()
def onix_secret ():
	
	print("Il va falloir combattre pour savoir ce qui intrigue ce onix !")
	-> combat onix
	print(" {prenom_1} : Pfiou, ce combat n'était pas facile mais que cache cette falaise ? Je n'ai d'autre choix que d'escalader mais c'est risqué !")
	print("Que voulez-vous faire ?")
	print("1) Grimper la falaise\n2)Rebrousser chemin")
	response_14 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
	if response_14 = 1 :
		print("{prenom_1} : c'est parti pour une petite séance d'escalade !")
		while not bonnes_prises = 5 :
			chutes = 0
			bonnes_prises = 0
			print("Que voulez vous faire ?")
			print("1)Monter la main gauche\n2)Monter la main droite")
			response_15 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
			escalade_1 = random.randint(1,4)
			escalade_2 = random.randint(1,5)
			if response_15 = 1:
				if escalade_1 = 1 :
					print("La prise ne tient pas, vous êtes tombé")
					chutes += 1
				else : 
					print("La prise tient, reste plus qu'à continuer comme ça !")
					bonnes_prises += 1
			if response_15 = 2 :
				if escalade_2 = 1 :
					print("La prise ne tient pas, vous êtes tombé")
					chutes += 1
				else : 
					print("La prise tient, reste plus qu'à continuer comme ça !")
					bonnes_prises += 1
			if chutes = 5 :
				print("vous êtes tombés trop de fois, vous êtes morts de chute")
				print("Game Over")
				quit()
			if bonnes_prises = 5 :
				print("{prenom_1} : Pas simple cette ascension mais je suis enfin arrivé dans cette grotte qui intrguait le Onix")
				print("Vous avancez jusqu'au fond de la grotte et un caillou avec une forme étrange se trouve au centre de la grotte")
				print("Vous venez de trouver un fossile mâchoire ! Ce fossile, si les conditions sont réunies, va se transformer en un ptyranidur !") 
				print("{prenom_1} : Quel incroyable trésor ! Il est peut-être temps de partir maitenant")

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
	if int(response_3)== 1:
		print(f"{prenom_1} : Je m'appelle {prenom_1}, je suis de retour ici, et toi comment tu t'appelles?")
		input("↓")
		print(f"jeune garçon : Je m'appelle Victor, ça te dit qu'on devienne potes?")
		input("↓")
		print(f"Que voulez vous faire :")
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
#Le joueur choisit son pokémon de départ 
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
    print("Poussifeu est un pokémon de type Feu, cela veut dire qu'il sera très éfficace face aux Pokémons de type Plante et Glace !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
elif Poké_dep_choix == 3:
    print("Gobou a été ajouté à ton Pokédex !")
    print("Gobou est un pokémon de type Eau, cela veut dire qu'il sera très éfficace face aux Pokémons de type Feu, Roche et Sol !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
#le jouer fait son premier combat tutoriel 
while hppokefightinitial > 0:
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
		print("Quelle objet pour se soigner ? n\1)Objet 1 n\2)Objet 2 ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			hp_poke_joueur = hp_poke_joueur + 20
		elif choixsoin == 2: 
			hp_poke_joueur = 60 
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
choix ():







print("Tu rencontres un Aspicot ")
	
	
	

		



