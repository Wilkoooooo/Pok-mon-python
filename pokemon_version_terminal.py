import random 
from math import * 
#variables de tout le programme : 
monnaie = 50
XP = 0
hp_starter = 60 
#Variable PP des Pokémons : 
nbr_Dracochoc = 15
nbr_Lame_Air = 20
nbr_Ultralaser = 10
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
fossile = 0
#variable_amitié
amitié = 0
fuir = False
attraper = False
state_combat = False
# Dictionnaire des chemins : clé = choix, valeur = (nom, fonction) 
def game_over ():
	print(f"L'aventure s'arrête ici pour vous.")
	game_over_art = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
	print(game_over_art)
	quit()

def victoire (): 
	global prenom
	print(f"\n ———————Félicitations {prenom} ! Tu as trouvé l'unique fin gagnante de ce jeu qui aura été insuportable à coder.———————")
	b = """
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣷⠀⠀⠀⠀⣸⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡞⣿⣷⣮⣻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡝⢿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⠸⣸⣻⣏⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⡿⡀⠀⠀⠀⠀⠀⣾⡞⡝⣿⢿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠩⣾⣿⣶⢦⣤⣀⠸⠻⢭⣥⡻⣧⠀⡙⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⢠⣴⣾⣿⣿⣿⣏⣶⣾⡽⣿⣷⣟⣿⣿⣿⣻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⣀⣀⣀⠀⠀⠀⠸⣿⡿⠘⠻⢿⣿⣿⠟⠛⠿⠿⠃⢍⣿⣿⢸⣿⣿⣿⡽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⣰⣟⠛⠛⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣜⢿⣿⡿⡷⡿⣼⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⢰⣿⠃⠀⠀⠀⠈⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣯⣾⣿⡀⠀⠙⠻⢿⣶⣄⠀⠀⠀⠀⠀⠀⠀
                                ⢸⣿⠀⠀⠀⠀⠀⠀⢻⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣧⡀⠀⠀⠀⠙⢿⣧⡀⠀⠀⠀⠀⠀
                                ⢸⣿⡀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣬⣽⣿⣿⢟⣛⣳⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⠀
                                ⠀⣿⣇⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣷⢻⣾⣿⣿⣷⡽⣄⠀⠀⢀⣾⣿⣷⣄⠀⠀
                                ⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⣄⡀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⢹⣦⠀⢸⣇⠀⠹⣏⢧⡀
                                ⠀⠀⠹⣿⣷⡀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⢸⣿⡄⠈⠛⠀⣶⠟⠼⠇
                                ⠀⠀⠀⠹⣿⣿⣷⣤⡀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣿⣿⣿⡿⣾⣿⠁⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠙⣿⣿⣿⣿⣶⣄⠀⠀⠈⠻⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⡿⣱⣿⣿⣿⣿⢟⣼⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣧⡀⠀⠀⠈⠻⢿⣿⢸⣿⣿⣿⡿⢟⣫⣾⣿⣿⠿⣛⣵⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢈⣾⣿⡟⠙⠚⠛⠛⠋⠉⠀⠘⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠁⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣯⢻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠋⠘⠻⣿⣿⣷⣶⣒⣒⢢⡄⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⣏⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠟⠈⠁⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡿⠿⠿⠿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	"""
	c = """
 █████   █████    █████      █████████     ███████████       ███████       █████    ███████████      ██████████    ███
░░███   ░░███    ░░███      ███░░░░░███   ░█░░░███░░░█     ███░░░░░███    ░░███    ░░███░░░░░███    ░░███░░░░░█   ░███
 ░███    ░███     ░███     ███     ░░░    ░   ░███  ░     ███     ░░███    ░███     ░███    ░███     ░███  █ ░    ░███
 ░███    ░███     ░███    ░███                ░███       ░███      ░███    ░███     ░██████████      ░██████      ░███
 ░░███   ███      ░███    ░███                ░███       ░███      ░███    ░███     ░███░░░░░███     ░███░░█      ░███
  ░░░█████░       ░███    ░░███     ███       ░███       ░░███     ███     ░███     ░███    ░███     ░███ ░   █   ░░░ 
    ░░███         █████    ░░█████████        █████       ░░░███████░      █████    █████   █████    ██████████    ███
     ░░░         ░░░░░      ░░░░░░░░░        ░░░░░          ░░░░░░░       ░░░░░    ░░░░░   ░░░░░    ░░░░░░░░░░    ░░░ 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀
	"""
	print(c)
	print(b)
	quit()
	
def combat_boss_final (hp_ennemi, nom_poke_ennemi, degat1, degat2, degat3):
	global XP, starter, nbr_Dracochoc, nbr_Lame_Air, nbr_Ultralaser, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter, fuir, attraper, attraper, prenom, state_combat
	if starter in (4,5,6):
		hp_starter += 40
		print(f"Que le combat commence !")
	elif starter in (7,8,9):
		hp_starter += 70
		print(f"Que le combat commence !")
	elif starter in (10, 11, 12, 13):
		hp_starter += 100
		print(f"Que le combat commence !")
	else:
	    print(f"Que le combat commence !")
	while hp_ennemi > 0 and hp_starter > 0 and not fuir and not attraper:
		print(f"\n À Vous de Jouer ! \n")
		if starter == 1:
			VAR_COMBAT = menu_combat_arcko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Désherbaffe = VAR_COMBAT[3]
			nbr_FouetsLiannes = VAR_COMBAT[4]
			nbr_LammeFeuille = VAR_COMBAT[5]
		elif starter == 2:
			VAR_COMBAT = menu_combat_poussifeu (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Flammèche = VAR_COMBAT[3]
			nbr_LanceFlammes = VAR_COMBAT[4]
			nbr_Rebondifeu = VAR_COMBAT[5]
		elif starter == 3:
			VAR_COMBAT = menu_combat_gobou (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Pistolet_à_O = VAR_COMBAT[3]
			nbr_Siphon = VAR_COMBAT[4]
			nbr_Hydrocanon = VAR_COMBAT[5]
		elif starter == 4:
			VAR_COMBAT = menu_combat_massko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Désherbaffe = VAR_COMBAT[3]
			nbr_FouetsLiannes = VAR_COMBAT[4]
			nbr_LammeFeuille = VAR_COMBAT[5]
		elif starter == 5:
			VAR_COMBAT = menu_combat_galifeu (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Flammèche = VAR_COMBAT[3]
			nbr_LanceFlammes = VAR_COMBAT[4]
			nbr_Rebondifeu = VAR_COMBAT[5]   
		elif starter == 6:
			VAR_COMBAT = menu_combat_flobio (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Pistolet_à_O = VAR_COMBAT[3]
			nbr_Siphon = VAR_COMBAT[4]
			nbr_Hydrocanon = VAR_COMBAT[5]
		elif starter == 7:
			VAR_COMBAT = menu_combat_jungko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Désherbaffe = VAR_COMBAT[3]
			nbr_FouetsLiannes = VAR_COMBAT[4]
			nbr_LammeFeuille = VAR_COMBAT[5]
		elif starter == 8:
			VAR_COMBAT = menu_combat_brasegali (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Flammèche = VAR_COMBAT[3]
			nbr_LanceFlammes = VAR_COMBAT[4]
			nbr_Rebondifeu = VAR_COMBAT[5]
		elif starter == 9:
			VAR_COMBAT = menu_combat_laggron (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Pistolet_à_O = VAR_COMBAT[3]
			nbr_Siphon = VAR_COMBAT[4]
			nbr_Hydrocanon = VAR_COMBAT[5]
		elif starter == 10:
			VAR_COMBAT = menu_combat_mega_jungko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Désherbaffe = VAR_COMBAT[3]
			nbr_FouetsLiannes = VAR_COMBAT[4]
			nbr_LammeFeuille = VAR_COMBAT[5]
		elif starter == 11:
			VAR_COMBAT = menu_combat_mega_brasegali (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Flammèche = VAR_COMBAT[3]
			nbr_LanceFlammes = VAR_COMBAT[4]
			nbr_Rebondifeu = VAR_COMBAT[5]
		elif starter == 12:
			VAR_COMBAT = menu_combat_mega_laggron (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Pistolet_à_O = VAR_COMBAT[3]
			nbr_Siphon = VAR_COMBAT[4]
			nbr_Hydrocanon = VAR_COMBAT[5]
		elif starter == 13:
			VAR_COMBAT = menu_combat_rayquaza (nbr_Dracochoc, nbr_Lame_Air, nbr_Ultralaser, hp_ennemi, hp_starter, nbr_superpotion, nbr_hyperpotion, nbr_pokeball, nbr_superball, nbr_hyperball)
			hp_ennemi = VAR_COMBAT[0]
			hp_starter = VAR_COMBAT[1]
			attraper = VAR_COMBAT[2]
			nbr_Dracochoc = VAR_COMBAT[3]
			nbr_Lame_Air = VAR_COMBAT[4]
			nbr_Ultralaser = VAR_COMBAT[5]
		print(f"\nle pokemon ennemie a {hp_ennemi} pv ")
		print(f"\nAu tour du pokémon adverse de jouer ! ")
		if hp_ennemi > 0 :
                        attaque_ennemi = random.randint(1,4)
                        if attaque_ennemi == 1:
                                hp_starter -= degat1
                                print(f"\n{nom_poke_ennemi} vous a infligé {degat1} dégats. Vous avez {hp_starter} points de vie.")
                        elif attaque_ennemi == 2:
                                hp_starter -= degat2
                                print(f"\n{nom_poke_ennemi} vous a infligé {degat2} dégats. Vous avez {hp_starter} points de vie.")
                        elif attaque_ennemi == 3:
                                hp_starter -= degat3
                                print(f"\n{nom_poke_ennemi} vous a infligé {degat3} dégats. Vous avez {hp_starter} points de vie.")
                        else:
                            attaque_ou_soin = random.randint(1,4) 
                            if attaque_ou_soin == 1:
                                hp_ennemi += 15
                                print(f"\n{nom_poke_ennemi} s'est soigné et a {hp_ennemi} points de vie.")
                            else:
                                attaque_ennemi_2 = random.randint(1,4)
                                if attaque_ennemi_2 == 1:
                                    hp_starter -= degat1
                                    print(f"\n{nom_poke_ennemi} vous a infligé {degat1} dégats. Vous avez {hp_starter} points de vie.")
                                elif attaque_ennemi_2 == 2:
                                    hp_starter -= degat2
                                    print(f"\n{nom_poke_ennemi} vous a infligé {degat2} dégats. Vous avez {hp_starter} points de vie.")
                                else:
                                    hp_starter -= degat3
                                    print(f"\n{nom_poke_ennemi} vous a infligé {degat3} dégats. Vous avez {hp_starter} points de vie.")
		else:
                        print(f"\n{nom_poke_ennemi} est mort ! Félicitation ! ")
                        if attraper == True:
                                print(f"\nTu as attrapé le Pokémon ! Bravo. Ça veut dire que je peux gagner tous mes combats en attrapant les pokémons adverses ? Imagine attraper un Pokémon destabiliserait l'île et tuerait tous les habitants. Nan je rigole mais imagine. ")
                                #faire texte manquant !!!!! si pokemon attraper = mort aussi 
                        if hp_starter <= 0:
                                print(f"{prenom} : NON ! Mon pokémon, il … il… il est… il est KO ! Je dois aller te soigner de suite !")
                                input("↓")
                                print(f"Cependant le pokémon ennemi commence à se charger de son énergie et la concentre tout autour de lui...")
                                input("↓")
                                print(f" {prenom} : Vite ! J-je.. je dois fuir !!")
                                input("↓")
                                print(f"le pokémon libère toute son énergie d'un coup et rase toute l'île où vous étiez !")
                                input("↓")
                                print(f"Vous n'avez pas réussi à portéger les habiatants de cette calamité, vous n'avez vraiment pas été à la hauteur... #lahonte")
                                game_over()
                        if hp_ennemi <= 0:
                                monnaie_gagne = random.randint(40,50)
                                monnaie += monnaie_gagne
                                print(f"Vous gagnez {monnaie_gagne} pièces. Vous avez maintenant {monnaie} pièces.")
                                input("↓")
                                print(f"En sortant de la grotte, celle-ci s'effondre au moment même où vous sortez")
                                input("↓")
                                print(f"Vous esquivez deux trois éboulements de rochers vous sautez vers la sortie et vous arrivez enfin à l'extérieur !")
                                input("↓")
                                print(f"En vous relevant, de nombreuses personnes se dirigent vers vous dont l'homme mystérieux de la ville de départ")
                                input("↓")
                                print(f"scientifique : Eh petit, t'as réussi à battre le pokémon à l'intérieur de la grotte ?")
                                input("↓")
                                print(f"{prenom} : Heu... Oui pourquoi ?")
                                input("↓")
                                print(f"scientifique : Hoo... Nous sommes sauvés ! Ce pokémon avait échappé à notre contrôle et il menacait de détruire toute l'île avec sa puissance de combat")
                                input("↓")
                                print(f"homme mystérieux : Bravo petit, je savais que tu allais accomplir de grandes choses !")
                                input("↓")
                                print(f"Vous avez sauvé l'île et vous êtes devenu le héros de tout ses habitants !")
                                victoire()
#Fonction combat
def boucle_combat(hp_ennemi, nom_poke_ennemi, degat1, degat2, degat3):
        global XP, starter, nbr_Dracochoc, nbr_Lame_Air, nbr_Ultralaser, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter, fuir, attraper, attraper, prenom, state_combat
        if starter in (4,5,6):
                hp_starter += 40
                print(f"Que le combat commence !")
        elif starter in (7,8,9):
                hp_starter += 70
                print(f"Que le combat commence !")
        elif starter in (10, 11, 12, 13):
                hp_starter += 100
                print(f"Que le combat commence !")
        else:
                print(f"Que le combat commence !")
        while hp_ennemi > 0 and hp_starter > 0 and not fuir and not attraper:
            print(f"\n À Vous de Jouer ! \n")
            if starter == 1:
                VAR_COMBAT = menu_combat_arcko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Désherbaffe = VAR_COMBAT[3]
                nbr_FouetsLiannes = VAR_COMBAT[4]
                nbr_LammeFeuille = VAR_COMBAT[5]
            elif starter == 2:
                VAR_COMBAT = menu_combat_poussifeu (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Flammèche = VAR_COMBAT[3]
                nbr_LanceFlammes = VAR_COMBAT[4]
                nbr_Rebondifeu = VAR_COMBAT[5]
            elif starter == 3:
                VAR_COMBAT = menu_combat_gobou (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Pistolet_à_O = VAR_COMBAT[3]
                nbr_Siphon = VAR_COMBAT[4]
                nbr_Hydrocanon = VAR_COMBAT[5]
            elif starter == 4:
                VAR_COMBAT = menu_combat_massko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Désherbaffe = VAR_COMBAT[3]
                nbr_FouetsLiannes = VAR_COMBAT[4]
                nbr_LammeFeuille = VAR_COMBAT[5]
            elif starter == 5:
                VAR_COMBAT = menu_combat_galifeu (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Flammèche = VAR_COMBAT[3]
                nbr_LanceFlammes = VAR_COMBAT[4]
                nbr_Rebondifeu = VAR_COMBAT[5]
            elif starter == 6:
                VAR_COMBAT = menu_combat_flobio (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Pistolet_à_O = VAR_COMBAT[3]
                nbr_Siphon = VAR_COMBAT[4]
                nbr_Hydrocanon = VAR_COMBAT[5]
            elif starter == 7:
                VAR_COMBAT = menu_combat_jungko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Désherbaffe = VAR_COMBAT[3]
                nbr_FouetsLiannes = VAR_COMBAT[4]
                nbr_LammeFeuille = VAR_COMBAT[5]
            elif starter == 8:
                VAR_COMBAT = menu_combat_brasegali (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Flammèche = VAR_COMBAT[3]
                nbr_LanceFlammes = VAR_COMBAT[4]
                nbr_Rebondifeu = VAR_COMBAT[5]
            elif starter == 9:
                VAR_COMBAT = menu_combat_laggron (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Pistolet_à_O = VAR_COMBAT[3]
                nbr_Siphon = VAR_COMBAT[4]
                nbr_Hydrocanon = VAR_COMBAT[5]
            elif starter == 10:
                VAR_COMBAT = menu_combat_mega_jungko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Désherbaffe = VAR_COMBAT[3]
                nbr_FouetsLiannes = VAR_COMBAT[4]
                nbr_LammeFeuille = VAR_COMBAT[5]
            elif starter == 11:
                VAR_COMBAT = menu_combat_mega_brasegali (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Flammèche = VAR_COMBAT[3]
                nbr_LanceFlammes = VAR_COMBAT[4]
                nbr_Rebondifeu = VAR_COMBAT[5]
            elif starter == 12:
                VAR_COMBAT = menu_combat_mega_laggron (nbr_Pistolet_à_O,nbr_Siphon,nbr_Hydrocanon,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Pistolet_à_O = VAR_COMBAT[3]
                nbr_Siphon = VAR_COMBAT[4]
                nbr_Hydrocanon = VAR_COMBAT[5]
            elif starter == 13:
                VAR_COMBAT = menu_combat_rayquaza (nbr_Dracochoc, nbr_Lame_Air, nbr_Ultralaser, hp_ennemi, hp_starter, nbr_superpotion, nbr_hyperpotion, nbr_pokeball, nbr_superball, nbr_hyperball)
                hp_ennemi = VAR_COMBAT[0]
                hp_starter = VAR_COMBAT[1]
                attraper = VAR_COMBAT[2]
                nbr_Dracochoc = VAR_COMBAT[3]
                nbr_Lame_Air = VAR_COMBAT[4]
                nbr_Ultralaser = VAR_COMBAT[5]
            # Attaque du Pokémon ennemi
            print(f"\nle pokemon ennemie a {hp_ennemi} pv ")
            print(f"\nAu tour du pokémon adverse de jouer ! ")
            if hp_ennemi > 0 : 
                attaque_ennemi = random.randint(1,4)
                if attaque_ennemi == 1:
                    hp_starter -= degat1
                    print(f"\n{nom_poke_ennemi} vous a infligé {degat1} dégats. Vous avez {hp_starter} points de vie.")
                elif attaque_ennemi == 2:
                    hp_starter -= degat2
                    print(f"\n{nom_poke_ennemi} vous a infligé {degat2} dégats. Vous avez {hp_starter} points de vie.")
                elif attaque_ennemi == 3:
                    hp_starter -= degat3
                    print(f"\n{nom_poke_ennemi} vous a infligé {degat3} dégats. Vous avez {hp_starter} points de vie.")
                else:
                    attaque_ou_soin = random.randint(1,4) 
                    if attaque_ou_soin == 1:
                        hp_ennemi += 15
                        print(f"\n{nom_poke_ennemi} s'est soigné et a {hp_ennemi} points de vie.")
                    else:
                        attaque_ennemi_2 = random.randint(1,4)
                        if attaque_ennemi_2 == 1:
                            hp_starter -= degat1
                            print(f"\n{nom_poke_ennemi} vous a infligé {degat1} dégats. Vous avez {hp_starter} points de vie.")
                        elif attaque_ennemi_2 == 2:
                            hp_starter -= degat2
                            print(f"\n{nom_poke_ennemi} vous a infligé {degat2} dégats. Vous avez {hp_starter} points de vie.")
                        else:
                            hp_starter -= degat3
                            print(f"\n{nom_poke_ennemi} vous a infligé {degat3} dégats. Vous avez {hp_starter} points de vie.")
            else:
                    print(f"\n{nom_poke_ennemi} est mort ! Félicitation ! ")
            if attraper == True:
                    print(f"\nTu as attrapé le Pokémon ! Bravo. Ça veut dire que je peux gagner tous mes combats en attrapant les pokémons adverses ? Imagine attraper un Pokémon destabiliserait l'île et tuerait tous les habitants. Nan je rigole mais imagine. ")
                    hp_ennemi = 0 
            if hp_starter <= 0:
                    print(f"\n{prenom} : NON ! Mon pokémon, il … il… il est… il est KO ! Je dois aller te soigner de suite !")
                    monnaie_gagne = random.randint(20,30)
                    monnaie += monnaie_gagne
                    print(f"\nVous gagnez quand même {monnaie_gagne} pièces. Vous avez maintenant {monnaie} pièces.")
                    return (XP, starter, hp_starter, state_combat, nbr_Dracochoc, nbr_Lame_Air, nbr_Ultralaser, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille)
                    
            if hp_ennemi <= 0:
                    XP_gagne=random.randint(100,200)
                    XP += XP_gagne
                    monnaie_gagne = random.randint(50,60)
                    monnaie += monnaie_gagne
                    state_combat = True 
                    if XP >= 500:
                        XP = 0
                        print(f"\nFélicitation, vous avez gagné(e) votre combat face à {nom_poke_ennemi}. Vous gagnez {monnaie_gagne} pièces. Vous avez maintenant {monnaie} pièces. Vous avez gagné(e) {XP_gagne} XPs. Vous avez maintenant {XP} XPs!\n Que ce passe-t-il ?\n\n\n Le Pokémon évolue !")
                        if starter in (1,2,3,4,5,6,7,8,9):
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
                                XP -= 500
                                return (XP, starter, hp_starter, state_combat, nbr_Dracochoc, nbr_Lame_Air, nbr_Ultralaser, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille)
                        else:
                                print("\n")
                    else:
                        print(f"\nFélicitation, vous avez gagné(e) votre combat face à {nom_poke_ennemi}. Vous gagnez {monnaie_gagne} pièces. Vous avez maintenant {monnaie} pièces. Vous avez gagné(e) {XP_gagne} XPs ! Vous avez maintenant {XP} XPs")
                        return (XP, starter, hp_starter, state_combat, nbr_Dracochoc, nbr_Lame_Air, nbr_Ultralaser, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille)

def menu_combat_rayquaza (nbr_Dracochoc, nbr_Lame_Air, nbr_Ultralaser, hp_ennemi, hp_starter, nbr_superpotion, nbr_hyperpotion, nbr_pokeball, nbr_superball, nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Dracochoc  (-75 hp) {nbr_Dracochoc}/15 \n 2)Lame d'Air (-70 hp) {nbr_Lame_Air}/20 \n 3)Ultralaser (-80 hp) {nbr_Ultralaser}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Dracochoc (-15 hp) {nbr_Dracochoc}/15 \n 2)Lame d'Air (-10 hp) {nbr_Lame_Air}/20 \n 3)Ultralaser (-20 hp) {nbr_Ultralaser}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Dracochoc > 0:
				hp_ennemi -= 15 
				nbr_Dracochoc -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Pistolet à O, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_Lame_Air > 0:
				hp_ennemi -= 10 
				nbr_Lame_Air -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Siphon, faites attention la prochaine fois ")
		elif quelle_attaque == 3: 
			if nbr_Ultralaser > 0:
				hp_ennemi -= 20 
				nbr_Ultralaser -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Hydrocanon, faites attention la prochaine fois ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superpotion > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de super potion...")
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0:
				hp_starter = 60 
				nbr_hyperpotion -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus d'hyper potion...")
		elif choixsoin == 3:
                    print(f"Sur quelle attaque : \n1)Dracochoc (-15 hp) {nbr_Dracochoc}/15 \n 2)Lame d'Air (-10 hp) {nbr_Lame_Air}/20 \n 3)Ultralaser (-20 hp) {nbr_Ultralaser}/10 ")
                    reponse_pp=int(input(f"Quel attaque choisissez vous ?"))
                    while not response_pp in (1,2,3):
                        print(f"Veuillez saisir un nombre correct")
                        print(f"Sur quelle attaque : \n1)Dracochoc (-15 hp) {nbr_Dracochoc}/15 \n 2)Lame d'Air (-10 hp) {nbr_Lame_Air}/20 \n 3)Ultralaser (-20 hp) {nbr_Ultralaser}/10 ")
                        reponse_pp=int(input(f"Quel attaque choisissez vous ?"))
                    if reponse_pp == 1:
                        nbr_Dracochoc = 15
                        return hp_ennemi, hp_starter, attraper
                    elif reponse_pp == 2:
                        nbr_Siphon = 20
                        return hp_ennemi, hp_starter, attraper
                    else:
                        nbr_Hydrocanon = 10
                        return hp_ennemi, hp_starter, attraper
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
                    print(f"Vous lancez une Pokéball !")
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
                            attraper = True
                            print(f"le pokémon a été capturé. Bravo !")
                    else:
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
                    return hp_ennemi, hp_starter, attraper
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                                attraper = True
                                print(f"le pokémon a été capturé. Bravo !")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Dracochoc, nbr_Lame_Air, nbr_Ultralaser)


def menu_combat_gobou (nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, hp_ennemi, hp_starter, nbr_superpotion, nbr_hyperpotion, nbr_pokeball, nbr_superball, nbr_hyperball):
	fuir = False
	attraper = False
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
			else:
				print(f"Vous n'avez plus de Pistolet à O, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_Siphon > 0:
				hp_ennemi -= 10 
				nbr_Siphon -= 1
			else:
				print(f"Vous n'avez plus de Siphon, faites attention la prochaine fois ")
		elif quelle_attaque == 3: 
			if nbr_Hydrocanon > 0:
				hp_ennemi -= 20 
				nbr_Hydrocanon -= 1
			else:
				print(f"Vous n'avez plus de Hydrocanon, faites attention la prochaine fois ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superpotion > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
			else:
				print(f"Vous n'avez plus de super potion...")
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0:
				hp_starter = 60 
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
                    print(f"Vous lancez une Pokéball !")
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
                            attraper = True
                            print(f"le pokémon a été capturé. Bravo !")
                    else:
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
                    return hp_ennemi, hp_starter, attraper
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                                attraper = True
                                print(f"le pokémon a été capturé. Bravo !")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon)
def menu_combat_flobio (nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, hp_ennemi, hp_starter, nbr_superpotion, nbr_hyperpotion, nbr_pokeball, nbr_superball, nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs\n4) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-25 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-20 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-30 hp) {nbr_Hydrocanon}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-25 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-20 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-30 hp) {nbr_Hydrocanon}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Pistolet_à_O > 0:
				hp_ennemi -= 25 
				nbr_Pistolet_à_O -= 1
			else:
				print(f"Vous n'avez plus de Pistolet à O, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_Siphon > 0:
				hp_ennemi -= 20 
				nbr_Siphon -= 1
			else:
				print(f"Vous n'avez plus de Siphon, faites attention la prochaine fois ")
		elif quelle_attaque == 3: 
			if nbr_Hydrocanon > 0:
				hp_ennemi -= 30 
				nbr_Hydrocanon -= 1
			else:
				print(f"Vous n'avez plus de Hydrocanon, faites attention la prochaine fois ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superpotion > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
			else:
				print(f"Vous n'avez plus de super potion...")
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0:
				hp_starter = 60 
				nbr_hyperpotion -= 1
			else:
				print(f"Vous n'avez plus d'hyper potion...")
		elif choixsoin == 3:
                    print(f"Sur quelle attaque : \n 1)Pistolet à O  (-25 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-20 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-30 hp) {nbr_Hydrocanon}/10 ")
                    reponse_pp=int(input(f"Quel attaque choisissez vous ?"))
                    while not response_pp in (1,2,3):
                        print(f"Veuillez saisir un nombre correct")
                        print(f"Sur quelle attaque : \n 1)Pistolet à O  (-25 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-20 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-30 hp) {nbr_Hydrocanon}/10 ")
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else:
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon)
def menu_combat_laggron (nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, hp_ennemi, hp_starter, nbr_superpotion, nbr_hyperpotion, nbr_pokeball, nbr_superball, nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs\n4) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-35 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-30 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-40 hp) {nbr_Hydrocanon}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-35 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-30 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-40 hp) {nbr_Hydrocanon}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Pistolet_à_O > 0:
				hp_ennemi -= 35 
				nbr_Pistolet_à_O -= 1
			else:
				print(f"Vous n'avez plus de Pistolet à O, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_Siphon > 0:
				hp_ennemi -= 30 
				nbr_Siphon -= 1
			else:
				print(f"Vous n'avez plus de Siphon, faites attention la prochaine fois ")
		elif quelle_attaque == 3: 
			if nbr_Hydrocanon > 0:
				hp_ennemi -= 40 
				nbr_Hydrocanon -= 1
			else:
				print(f"Vous n'avez plus de Hydrocanon, faites attention la prochaine fois ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superpotion > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
			else:
				print(f"Vous n'avez plus de super potion...")
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0:
				hp_starter = 60 
				nbr_hyperpotion -= 1
			else:
				print(f"Vous n'avez plus d'hyper potion...")
		elif choixsoin == 3:
                    print(f"Sur quelle attaque : \n 1)Pistolet à O  (-35 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-30 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-40 hp) {nbr_Hydrocanon}/10 ")
                    reponse_pp=int(input(f"Quel attaque choisissez vous ?"))
                    while not response_pp in (1,2,3):
                        print(f"Veuillez saisir un nombre correct")
                        print(f"Sur quelle attaque : \n 1)Pistolet à O  (-35 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-30 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-40 hp) {nbr_Hydrocanon}/10 ")
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else:
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon)

def menu_combat_mega_laggron (nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, hp_ennemi, hp_starter, nbr_superpotion, nbr_hyperpotion, nbr_pokeball, nbr_superball, nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs\n4) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-45 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-40 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-50 hp) {nbr_Hydrocanon}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Pistolet à O  (-45 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-40 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-50 hp) {nbr_Hydrocanon}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Pistolet_à_O > 0:
				hp_ennemi -= 45 
				nbr_Pistolet_à_O -= 1
			else:
				print(f"Vous n'avez plus de Pistolet à O, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_Siphon > 0:
				hp_ennemi -= 40 
				nbr_Siphon -= 1
			else:
				print(f"Vous n'avez plus de Siphon, faites attention la prochaine fois ")
		elif quelle_attaque == 3: 
			if nbr_Hydrocanon > 0:
				hp_ennemi -= 50 
				nbr_Hydrocanon -= 1
			else:
				print(f"Vous n'avez plus de Hydrocanon, faites attention la prochaine fois ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superpotion > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
			else:
				print(f"Vous n'avez plus de super potion...")
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0:
				hp_starter = 60 
				nbr_hyperpotion -= 1
			else:
				print(f"Vous n'avez plus d'hyper potion...")
		elif choixsoin == 3:
                    print(f"Sur quelle attaque : \n 1)Pistolet à O  (-45 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-40 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-50 hp) {nbr_Hydrocanon}/10 ")
                    reponse_pp=int(input(f"Quel attaque choisissez vous ?"))
                    while not response_pp in (1,2,3):
                        print(f"Veuillez saisir un nombre correct")
                        print(f"Sur quelle attaque : \n 1)Pistolet à O  (-45 hp) {nbr_Pistolet_à_O}/15 \n 2)Siphon (-40 hp) {nbr_Siphon}/20 \n 3)Hydrocanon (-50 hp) {nbr_Hydrocanon}/10 ")
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else:
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon)
	
def menu_combat_poussifeu (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	attraper = False
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
			else:
				print(f"Vous n'avez plus de Flammèche, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_LanceFlammes > 0:
				hp_ennemi -= 10 
				nbr_LanceFlammes -= 1
			else:
				print(f"Vous n'avez plus de Lance Flammes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_Rebondifeu > 0:
				hp_ennemi -= 20 
				nbr_Rebondifeu -= 1
			else:
				print(f"Vous n'avez plus de Rebondifeu, veuillez en chosir une autre ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
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
			print(f"Sur quelle attaque : \n1)Flammèche (-15 hp) {nbr_Flammèche}/15 \n 2)Lance-Flammes (-10 hp) {nbr_Lance-Flammes}/20 \n 3)Rebondifeu (-20 hp) {nbr_Rebondifeu}/10 ")
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else :
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu)
def menu_combat_galifeu (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-25 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-20 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-30 hp) {nbr_Rebondifeu}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-25 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-20 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-30 hp) {nbr_Rebondifeu}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Flammèche > 0:
				hp_ennemi -= 25 
				nbr_Flammèche -= 1
			else:
				print(f"Vous n'avez plus de Flammèche, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_LanceFlammes > 0:
				hp_ennemi -= 20 
				nbr_LanceFlammes -= 1
			else:
				print(f"Vous n'avez plus de Lance Flammes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_Rebondifeu > 0:
				hp_ennemi -= 30 
				nbr_Rebondifeu -= 1
			else:
				print(f"Vous n'avez plus de Rebondifeu, veuillez en chosir une autre ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
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
			print(f"Sur quelle attaque : \n 1)Flammèche (-25 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-20 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-30 hp) {nbr_Rebondifeu}/10 ")
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else :
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu)

def menu_combat_brasegali (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-35 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-30 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-40 hp) {nbr_Rebondifeu}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-35 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-30 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-40 hp) {nbr_Rebondifeu}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Flammèche > 0:
				hp_ennemi -= 35 
				nbr_Flammèche -= 1
			else:
				print(f"Vous n'avez plus de Flammèche, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_LanceFlammes > 0:
				hp_ennemi -= 30 
				nbr_LanceFlammes -= 1
			else:
				print(f"Vous n'avez plus de Lance Flammes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_Rebondifeu > 0:
				hp_ennemi -= 40 
				nbr_Rebondifeu -= 1
			else:
				print(f"Vous n'avez plus de Rebondifeu, veuillez en chosir une autre ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
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
			print(f"Sur quelle attaque : \n 1)Flammèche (-35 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-30 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-40 hp) {nbr_Rebondifeu}/10 ")
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else :
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu)
def menu_combat_mega_brasegali (nbr_Flammèche,nbr_LanceFlammes,nbr_Rebondifeu,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-45 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-40 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-50 hp) {nbr_Rebondifeu}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Flammèche (-45 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-40 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-50 hp) {nbr_Rebondifeu}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Flammèche > 0:
				hp_ennemi -= 45 
				nbr_Flammèche -= 1
			else:
				print(f"Vous n'avez plus de Flammèche, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_LanceFlammes > 0:
				hp_ennemi -= 40 
				nbr_LanceFlammes -= 1
			else:
				print(f"Vous n'avez plus de Lance Flammes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_Rebondifeu > 0:
				hp_ennemi -= 50 
				nbr_Rebondifeu -= 1
			else:
				print(f"Vous n'avez plus de Rebondifeu, veuillez en chosir une autre ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
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
			print(f"Sur quelle attaque :  \n 1)Flammèche (-45 hp) {nbr_Flammèche}/15 \n 2)LanceFlammes (-40 hp) {nbr_LanceFlammes}/20 \n 3)Rebondifeu (-50 hp) {nbr_Rebondifeu}/10 ")
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else :
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu)
def menu_combat_arcko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-15 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Lianness (-10 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-20 hp) {nbr_LammeFeuille}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-15 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-10 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-20 hp) {nbr_LammeFeuille}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Désherbaffe > 0:
				hp_ennemi -= 15 
				nbr_Désherbaffe -= 1
			else:
				print(f"Vous n'avez plus de Désherbaffe, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_FouetsLiannes > 0:
				hp_ennemi -= 10 
				nbr_FouetsLiannes -= 1
			else:
				print(f"Vous n'avez plus de Fouets-Liannes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_LammeFeuille > 0:
				hp_ennemi -= 20 
				nbr_LammeFeuille -= 1
			else:
				print(f"Vous n'avez plus de Lamme-Feuille, veuillez en chosir une autre ")
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
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
			print(f"Sur quelle attaque : \n 1)Désherbaffe (-15 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-10 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-20 hp) {nbr_LammeFeuille}/10 ")
			reponse_pp=int(input(f"Quelle attaque choisissez vous ?"))
			if reponse_pp == 1:
			    nbr_Désherbaffe = 15
			elif reponse_pp == 2: 
			    nbr_FouetsLiannes == 2
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else:
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille)	
def menu_combat_massko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-25 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-20 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-30 hp) {nbr_LammeFeuille}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-25 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-20 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-30 hp) {nbr_LammeFeuille}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Désherbaffe > 0:
				hp_ennemi -= 25 
				nbr_Désherbaffe -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Désherbaffe, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_FouetsLiannes > 0:
				hp_ennemi -= 20 
				nbr_FouetsLiannes -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Fouets-Liannes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_LammeFeuille > 0:
				hp_ennemi -= 30 
				nbr_LammeFeuille -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Lamme-Feuille, veuillez en chosir une autre ")
				return hp_ennemi, hp_starter, attraper
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superption > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
				return hp_ennemi, hp_starter, attraper
			if nbr_superpotion == 0 :
				print(f"Vous n'avez plus de super potion...")
				return hp_ennemi, hp_starter, attraper
				
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0 :
				hp_starter = 60 
				nbr_hyperpotion -= 1
				return hp_ennemi, hp_starter, attraper
			if nbr_hyperpotion == 0 :
				print(f"vous n'avez plus d'hyper potion...")
				return hp_ennemi, hp_starter, attraper
				
		elif choixsoin == 3: 
			print(f"Sur quelle attaque : \n 1)Désherbaffe (-25 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-20 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-30 hp) {nbr_LammeFeuille}/10 ")
			reponse_pp=int(input(f"Quelle attaque choisissez vous ?"))
			if reponse_pp == 1:
			    nbr_Désherbaffe = 15
			    return hp_ennemi, hp_starter, attraper
			elif reponse_pp == 2: 
			    nbr_FouetsLiannes == 2
			    return hp_ennemi, hp_starter, attraper
			else:
				nbr_LammeFeuille = 10
				return hp_ennemi, hp_starter, attraper
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else:
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille)
def menu_combat_jungko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-35 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-30 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-40 hp) {nbr_LammeFeuille}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-35 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-30 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-40 hp) {nbr_LammeFeuille}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Désherbaffe > 0:
				hp_ennemi -= 35 
				nbr_Désherbaffe -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Désherbaffe, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_FouetsLiannes > 0:
				hp_ennemi -= 30 
				nbr_FouetsLiannes -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Fouets-Liannes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_LammeFeuille > 0:
				hp_ennemi -= 40 
				nbr_LammeFeuille -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Lamme-Feuille, veuillez en chosir une autre ")
				return hp_ennemi, hp_starter, attraper
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superption > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
				return hp_ennemi, hp_starter, attraper
			if nbr_superpotion == 0 :
				print(f"Vous n'avez plus de super potion...")
				return hp_ennemi, hp_starter, attraper
				
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0 :
				hp_starter = 60 
				nbr_hyperpotion -= 1
				return hp_ennemi, hp_starter, attraper
			if nbr_hyperpotion == 0 :
				print(f"vous n'avez plus d'hyper potion...")
				return hp_ennemi, hp_starter, attraper
				
		elif choixsoin == 3: 
			print(f"Sur quelle attaque : \n 1)Désherbaffe (-35 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-30 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-40 hp) {nbr_LammeFeuille}/10 ")
			reponse_pp=int(input(f"Quelle attaque choisissez vous ?"))
			if reponse_pp == 1:
			    nbr_Désherbaffe = 15
			    return hp_ennemi, hp_starter, attraper
			elif reponse_pp == 2: 
			    nbr_FouetsLiannes == 2
			    return hp_ennemi, hp_starter, attraper
			else:
				nbr_LammeFeuille = 10
				return hp_ennemi, hp_starter, attraper
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else:
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille)
def menu_combat_mega_jungko (nbr_Désherbaffe,nbr_FouetsLiannes,nbr_LammeFeuille,hp_ennemi,hp_starter,nbr_superpotion,nbr_hyperpotion,nbr_pokeball,nbr_superball,nbr_hyperball):
	fuir = False
	attraper = False
	print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Pokéballs \n4) Fuir")
	choix=int(input("choisissez le bon numéro "))
	while not  choix in (1,2,3,4):
		print(f"Veuillez saisir un nombre correct")
		print(f"Que voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon \n4) Pokéballs\n5) Fuir")
		choix=int(input("choisissez le bon numéro "))
	if choix == 1: 
		print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-45 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-40 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-50 hp) {nbr_LammeFeuille}/10 ")
		quelle_attaque=int(input("choisissez le bon numéro "))
		while not quelle_attaque in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle attaque voulez vous utiliser ? \n 1)Désherbaffe (-45 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-40 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-50 hp) {nbr_LammeFeuille}/10 ")
			quelle_attaque=int(input("choisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbr_Désherbaffe > 0:
				hp_ennemi -= 45 
				nbr_Désherbaffe -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Désherbaffe, faites attention la prochaine fois ")
		elif quelle_attaque == 2: 
			if nbr_FouetsLiannes > 0:
				hp_ennemi -= 40 
				nbr_FouetsLiannes -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Fouets-Liannes, veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbr_LammeFeuille > 0:
				hp_ennemi -= 50 
				nbr_LammeFeuille -= 1
				return hp_ennemi, hp_starter, attraper
			else:
				print(f"Vous n'avez plus de Lamme-Feuille, veuillez en chosir une autre ")
				return hp_ennemi, hp_starter, attraper
	elif choix == 2: 
		print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3) Remplir vos PPs ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2,3):
			print(f"Veuillez saisir un nombre correct")
			print(f"Quelle objet pour se soigner ? \n 1)Super Potion \n 2)Hyper potion \n 3)Remplir vos PPs ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			if nbr_superption > 0 :
				hp_starter += 20
				nbr_superpotion -= 1
				return hp_ennemi, hp_starter, attraper
			if nbr_superpotion == 0 :
				print(f"Vous n'avez plus de super potion...")
				return hp_ennemi, hp_starter, attraper
				
		elif choixsoin == 2: 
			if nbr_hyperpotion > 0 :
				hp_starter = 60 
				nbr_hyperpotion -= 1
				return hp_ennemi, hp_starter, attraper
			if nbr_hyperpotion == 0 :
				print(f"vous n'avez plus d'hyper potion...")
				return hp_ennemi, hp_starter, attraper
				
		elif choixsoin == 3: 
			print(f"Sur quelle attaque : \n 1)Désherbaffe (-45 hp) {nbr_Désherbaffe}/15 \n 2)Fouets-Liannes (-40 hp) {nbr_FouetsLiannes}/20 \n 3)Lamme-Feuille (-50 hp) {nbr_LammeFeuille}/10 ")
			reponse_pp=int(input(f"Quelle attaque choisissez vous ?"))
			if reponse_pp == 1:
			    nbr_Désherbaffe = 15
			    return hp_ennemi, hp_starter, attraper
			elif reponse_pp == 2: 
			    nbr_FouetsLiannes == 20
			    return hp_ennemi, hp_starter, attraper
			else:
				nbr_LammeFeuille = 10
				return hp_ennemi, hp_starter, attraper
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
                    print(f"Vous lancez une Pokéball !")
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
                        print(f"le pokémon a été capturé. Bravo !")
                        attraper = True
                    else:
                        print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Pokéball c'était pourtant écrit... veuillez faire attention la prochaine fois !")    
            elif choix_pokeball == 2:
                if nbr_superball > 0: 
                    nbr_superball -= 1
                    print(f"Vous lancez une Superball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Superball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
            elif choix_pokeball == 3:
                if nbr_hyperball > 0: 
                    nbr_hyperball -= 1
                    print(f"Vous lancez une Hyperball !")
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
                            print(f"le pokémon a été capturé. Bravo !")
                            attraper = True
                        else:
                            print(f"dommage")
                else:
                    print(f"Vous n'avez plus de Hyperball c'était pourtant écrit... veuillez faire attention la prochaine fois !")
	else:
            print(f"Vous ne voullez pas combattre car vous êtes une énorme tapette et décidez de fuir le combat !")
            fuir = True 
	return (hp_ennemi, hp_starter, attraper, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille)
#fonction boutique
def boutique ():
        global XP, starter, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter
        print(f" Accueil : Bienvenue à la boutique que souhaitez vous acheter ?")
        print(f"\n1)Acheter des Pokéballs\n2)Acheter des potions\n3)Quitter")
        achat_boutique = int(input("\nQue choisissez vous ? (sélectionnez le bon numéro) : "))
        while not achat_boutique in (1,2,3):
                print(f"Veuillez saisir un nombre correct")
                print(f"\n1)acheter des Pokéballs\n2)acheter des potions\n3)Quitter")
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
        elif achat_boutique == 2:
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
        elif achat_boutique == 3 :
        	print(f"à la prochaine !")	


def medecin ():
        global XP, starter, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter
        monnaie -= 5
        print(f"Vous devez payer 5 pièces de monnaie pour frais de consultation, il vous reste donc {monnaie} monnaie")
        input("↓")
        print(f"Faites attention à ne pas vous blesser la prochaine fois !")
				
# --- Définition des fonctions associées à chaque chemin --- #

def ville_donjon ():
        global XP, starter, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter
        print(f"Tu as choisis de te diriger vers la ville donjon du nom de Versailles")
        input("↓")
        print(f"Après quelques heures de marche tu te retrouves face au château de Versailles")
        input("↓")
        print(f"{prenom} : Ce château me donne des frissons dans le dos mais je suis sûr de trouver des super pokémons et récompenses !")
        input("↓")
        print(f"Tu rentres dans le château et tu t'enfonces dans une salle obscure...")
        input("↓")
        print(f"Tu observes deux objets scintillants à quelques mètres de toi")
        input("↓")
        print(f"Les lumières de la salle s'allument et tu te retrouves face à un ténéfix !")
        input("↓")
        print(f"Que le combat commence")
        #combat ténéfix
        combat1 = boucle_combat(65, "Ténéfix", 15, 10, 20)
        XP = combat1 [0]
        starter = combat1 [1]
        hp_starter = combat1 [2]
        hp_starter = 60
        nbr_Dracochoc = combat1 [4]
        nbr_Lame_Air = combat1 [5]
        nbr_Ultralaser = combat1 [6]
        nbr_Flammèche = combat1 [7]
        nbr_LanceFlammes = combat1 [8]
        nbr_Rebondifeu = combat1 [9]
        nbr_Pistolet_à_O = combat1 [10]
        nbr_Siphon = combat1 [11]
        nbr_Hydrocanon = combat1 [12]
        nbr_Désherbaffe = combat1 [13]
        nbr_FouetsLiannes =	combat1 [14]
        nbr_LammeFeuille = combat1 [15]
        nbr_Dracochoc = 15
        nbr_Lame_Air = 20
        nbr_Ultralaser = 10
        nbr_Flammèche = 15
        nbr_LanceFlammes = 20
        nbr_Rebondifeu = 10
        nbr_Pistolet_à_O = 15
        nbr_Siphon = 20
        nbr_Hydrocanon = 10
        nbr_Désherbaffe = 15
        nbr_FouetsLiannes =	20
        nbr_LammeFeuille = 10
        boutique ()
        print(f"Après ce rude combat, tu t'orientes vers le fond de la salle")
        input("↓")
        print(f"2 portes s'offrent à toi...")
        input("↓")
        print(f"Que voulez vous faire :")
        print(f"1)porte de gauche \n2)porte de droite")
        choix_porte = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
        while not choix_porte in (1,2):
                print(f"Veuillez saisir un nombre correct")
                print(f"1)porte de gauche \n2)porte de droite")
                choix_porte = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
        if choix_porte == 1 :
                print(f"Vous vous dirigez vers la porte de gauche")
                input("↓")
                print(f"Vous entendez un rugissement venant de derrière la porte...")
                input("↓")
                print(f"Vous décidez quand même d'entrer car vous savez porter vos balls")
                input("↓")
                print(f"Vous vous tenez devant absol, le combat risque d'être compliqué !")
                input("↓")
                print(f"Que le combat commence !")
                #combat absol
                combat2 = boucle_combat(60, "Absol", 15, 10, 20)
                XP = combat2 [0]
                starter = combat2 [1]
                hp_starter = combat2 [2]
                hp_starter = 60
                nbr_Dracochoc = combat2 [4]
                nbr_Lame_Air = combat2 [5]
                nbr_Ultralaser = combat2 [6]
                nbr_Flammèche = combat2 [7]
                nbr_LanceFlammes = combat2 [8]
                nbr_Rebondifeu = combat2 [9]
                nbr_Pistolet_à_O = combat2 [10]
                nbr_Siphon = combat2 [11]
                nbr_Hydrocanon = combat2 [12]
                nbr_Désherbaffe = combat2 [13]
                nbr_FouetsLiannes =	combat2 [14]
                nbr_LammeFeuille = combat2 [15]
                nbr_Dracochoc = 15
                nbr_Lame_Air = 20
                nbr_Ultralaser = 10
                nbr_Flammèche = 15
                nbr_LanceFlammes = 20
                nbr_Rebondifeu = 10
                nbr_Pistolet_à_O = 15
                nbr_Siphon = 20
                nbr_Hydrocanon = 10
                nbr_Désherbaffe = 15
                nbr_FouetsLiannes =	20
                nbr_LammeFeuille = 10
                boutique ()
                print(f"Après ce rude combat vous vous dirigez vers le la porte au fond de la salle")
                input("↓")
                print(f"Vous vous retrouvez dans un long couloir comme ceux qui mènent au boss dans les jeux...")
                input("↓")
                print(f"Vous poussez la porte et vous tombez face à un trioxhydre, bone chance...")
                boss_donjon ()
        else :
                print(f"Vous vous dirigez vers la porte de droite")
                input("↓")
                print(f"Vous entendez un cri effrayant venant de derrière la porte...")
                input("↓")
                print(f"Vous décidez quand même d'entrer car vous savez porter vos balls")
                input("↓")
                print(f"Vous vous tenez devant spectrum, le combat risque d'être compliqué !")
                input("↓")
                print(f"Que le combat commence !")
                #combat spectrum
                combat3 = boucle_combat(75, "Spectrum", 15, 10, 20)
                XP = combat3 [0]
                starter = combat3 [1]
                hp_starter = combat3 [2]
                hp_starter = 60
                nbr_Dracochoc = combat3 [4]
                nbr_Lame_Air = combat3 [5]
                nbr_Ultralaser = combat3 [6]
                nbr_Flammèche = combat3 [7]
                nbr_LanceFlammes = combat3 [8]
                nbr_Rebondifeu = combat3 [9]
                nbr_Pistolet_à_O = combat3 [10]
                nbr_Siphon = combat3 [11]
                nbr_Hydrocanon = combat3 [12]
                nbr_Désherbaffe = combat3 [13]
                nbr_FouetsLiannes = combat3 [14]
                nbr_LammeFeuille = combat3 [15]
                nbr_Dracochoc = 15
                nbr_Lame_Air = 20
                nbr_Ultralaser = 10
                nbr_Flammèche = 15
                nbr_LanceFlammes = 20
                nbr_Rebondifeu = 10
                nbr_Pistolet_à_O = 15
                nbr_Siphon = 20
                nbr_Hydrocanon = 10
                nbr_Désherbaffe = 15
                nbr_FouetsLiannes = 20
                nbr_LammeFeuille = 10
                boutique ()
                print(f"Après ce rude combat vous vous dirigez vers le la porte au fond de la salle, et, juste avant de la franchir vous êtes intrigués par une trappe dans un coin de la salle")
                print(f"Que voulez vous faire :")
                print(f"1)porte\n2)trappe")
                choix_trappe = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
                while not choix_trappe in (1,2):
                        print(f"Veuillez saisir un nombre correct")
                        print(f"1)porte\n2)trappe")
                        choix_trappe = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
                if choix_trappe == 1:
                        print(f"Vous vous retrouvez dans un long couloir comme ceux qui mènent au boss dans les jeux")
                        input("↓")
                        print(f"En poussant la grande porte au bout du couloir vous tombez face à un trioxhydre, bonne chance...")
                        boss_donjon ()
                else:
                        print(f"Vous passez la trappe et vous êtes arrivés dans une salle avec plusieurs portes")
                        labyrinthe = {
                                "entrée": {
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
                                        "droite": "D"
                                        },
                                "D": {
                                        "face": "Q",
                                        "gauche": "R",
                                        },
                                "E": {
                                        "face": "O",
                                        "droite": "H",
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
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        },
                                "J": {
                                        "droite": "K",
                                        "gauche": "L"
                                        },
                                "K": {
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        },
                                "L": {
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        },
                                "M": {
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        },
                                "N": {
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        },
                                "O": {
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        },
                                "P": {
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        },
                                "Q": {
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        },
                                "R": {
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        },
                                "S":{
                                        "sortie"
                                        },
                                "T": {
                                        "gauche": None,
                                        "face": None,
                                        "droite": None
                                        }
                                }
                        position = "entrée"
                        while True:
                                print(f"Vous êtes à : {position}")
                                chemins = labyrinthe[position]
                                if position == "S":
                                        print(f" Bravo ! Vous avez trouvé la sortie du labyrinthe ! ")
                                        input("↓")
                                        print(f"Vous êtes arrivés dans la salle au trésor caché et un objet mystérieux est placé au centre de la pièce...")
                                        input("↓")
                                        print(f"Vous vous rapprochez et prenez l'objet. C'est une partie d'un fossile mâchoire !")
                                        input("↓")
                                        fossile += 1
                                        if fossile1 and fossile2 == 1:
                                                print(f"\n Vos fossiles semble s'agiter ! \n\n Vous remarquez qu'il s'assemblent parfaitement.\nQue se passe-t-il, un rayquaza apparait !")
                                                ray=int(input("\nVoulez vous mettre Rayquaza comme Pokémon principal de votre équipe ? \n\n1) Oui\n2) Non"))
                                                if ray == 1:
                                                        print(f"Rayquaza a été ajouté à votre équipe !")
                                                        starter = 13
                                                else:
                                                        print(f"Rayquaza n'a pas été ajouté à votre équipe et disparait ! ")
                                        print(f"une porte se tient au fond de la pièce pour sortir, vous la prenez et vous tombez directement dans la salle du boss !")
                                        input("↓")
                                        print(f"Un trioxhydre fait son appirition, bonne chance...")
                                        boss_donjon()
                                        break
                                if all(direction is None for direction in chemins.values()):
                                        print(f"Cul-de-sac ! Retour à l'entrée...\n")
                                        position = "entrée"
                                        continue
                                print(f"Options disponibles :")
                                for direction, destination in chemins.items():
                                        print(f"  - {direction} -> {destination}")
                                        choix = input("Choissisez une direction entre : (gauche, face, droite) : ")
                                        if choix not in chemins:
                                                print(f"Direction invalide.\n")
                                                continue
                                        position = chemins[choix]
                                        print()

def boss_donjon ():
        global XP, starter, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter
        #combat trioxhydre
        combat7 = boucle_combat(100, "Trioxhydre", 15, 10, 20)
        XP = combat7 [0]
        starter = combat7 [1]
        hp_starter = combat7 [2]
        hp_starter = 60
        nbr_Dracochoc = combat7 [4]
        nbr_Lame_Air = combat7 [5]
        nbr_Ultralaser = combat7 [6]
        nbr_Flammèche = combat7 [7]
        nbr_LanceFlammes = combat7 [8]
        nbr_Rebondifeu = combat7 [9]
        nbr_Pistolet_à_O = combat7 [10]
        nbr_Siphon = combat7 [11]
        nbr_Hydrocanon = combat7 [12]
        nbr_Désherbaffe = combat7 [13]
        nbr_FouetsLiannes =	combat7 [14]
        nbr_LammeFeuille = combat7 [15]
        nbr_Dracochoc = 15
        nbr_Lame_Air = 20
        nbr_Ultralaser = 10
        nbr_Flammèche = 15
        nbr_LanceFlammes = 20
        nbr_Rebondifeu = 10
        nbr_Pistolet_à_O = 15
        nbr_Siphon = 20
        nbr_Hydrocanon = 10
        nbr_Désherbaffe = 15
        nbr_FouetsLiannes =	20
        nbr_LammeFeuille = 10
        boutique()
        
def grotte_boss ():
        global XP, starter, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter
        print(f"vous decidez de prendre la direction du Volcan de l'ile qui se trouve être de plus en plus instable récemment")
        input("↓")
        print(f"En te rapprochant du volcan tu te retrouves face à une grotte")
        input("↓")
        print(f"Que voulez vous faire :")
        print(f"1)rentrer dans la grotte\n2)faire demi-tour")
        response_17 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
        while not response_17 in (1,2):
                print(f"Veuillez saisir un nombre correct")
                print(f"1)rentrer dans la grotte\n2)faire demi-tour")
                response_17 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
        if response_17 == 1 :
                print(f"Vous avez décidé de rentrer dans la grotte, vous marchez pendant de longues minutes jusqu'à vous retrouver dans une salle souterraine")
                input("↓")
                print(f"Un pokémon que vous n'avez encore jamais croisé fait son apparition")
                #combat pokémon mystérieux
                combat_boss_final (10, "Mewtoo Shiny", 40, 35, 50)
        else:
                print("tu meurs")
                quit()
		
def arènes_pokémons ():
        global XP, starter, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter
        print(f"Vous arrivez à présent aux arènes pokémons espérant gagner de nombreuses récompenses et faire évoluer vos pokémons")
        input("↓")
        print(f"quelqu'un à l'entrée de l'arène vous attend pour vous expliquer les règles de l'arène pokémon")
        input("↓")
        print(f"organisateur : Bonjour jeune homme, vous êtes arrivé à l'arène pokémon, ici de nombreux dresseurs s'affrontent en espérant atteindre la finale du tournoi pour gagner un pokémon rarissime !")
        input("↓")
        print(f"organisateur : Le fonctionnement est très simple, vous démarrez quand 32 dresseurs pokémons arrivent dans l'arène et dès que vous perdez vous devez attendre le prochain tournoi, par contre à chaque fois que vous gagnez vous passez à l'étape supérieure et vous affrontez de noueaux dresseurs. Vous avez le droit d'utliser des potions de soins sur vos pokémons seulement entre chaque combat; Bonne chance !")
        input("↓")
        print(f"Organisateur : Alors ça te tente ?")
        input("↓")
        print(f"Que voulez vous faire :")
        print(f"1)S'inscrire au tournoi\n2)partir de l'arène pokémon")
        response_8 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
        while not response_8 in (1,2):
                print(f"Veuillez saisir un nombre correct")
                print(f"1)S'inscrire au tournoi\n2)partir de l'arène pokémon")
                response_8 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
        if response_8 == 1:
                print(f"votre premier combat commence !")
                arene1 = boucle_combat(65, "Azurill", 15, 10, 20)
                XP = arene1 [0]
                starter = arene1 [1]
                hp_starter = arene1 [2]
                hp_starter = 60
                state_combat = arene1 [3]
                nbr_Dracochoc = arene1 [4]
                nbr_Lame_Air = arene1 [5]
                nbr_Ultralaser = arene1 [6]
                nbr_Flammèche = arene1 [7]
                nbr_LanceFlammes = arene1 [8]
                nbr_Rebondifeu = arene1 [9]
                nbr_Pistolet_à_O = arene1 [10]
                nbr_Siphon = arene1 [11]
                nbr_Hydrocanon = arene1 [12]
                nbr_Désherbaffe = arene1 [13]
                nbr_FouetsLiannes =	arene1 [14]
                nbr_LammeFeuille = arene1 [15]
                if state_combat == True:
                        print("Bravo, vous passez au dresseur suivant !")
                        print(f"votre deucième combat commence !")
                        state_combat = False
                        arene2 = boucle_combat(70, "Malosse", 15, 10, 20)
                        XP = arene2 [0]
                        starter = arene2 [1]
                        hp_starter = arene2 [2]
                        hp_starter = 60
                        state_combat = arene2 [3]
                        nbr_Dracochoc = arene2 [4]
                        nbr_Lame_Air = arene2 [5]
                        nbr_Ultralaser = arene2 [6]
                        nbr_Flammèche = arene2 [7]
                        nbr_LanceFlammes = arene2 [8]
                        nbr_Rebondifeu = arene2 [9]
                        nbr_Pistolet_à_O = arene2 [10]
                        nbr_Siphon = arene2[11]
                        nbr_Hydrocanon = arene2 [12]
                        nbr_Désherbaffe = arene2 [13]
                        nbr_FouetsLiannes =	arene2 [14]
                        nbr_LammeFeuille = arene2 [15]
                        if state_combat == True:
                                print("Bravo, vous passez au dresseur suivant !")
                                print(f"votre premier combat commence !")
                                state_combat = False
                                arene3 = boucle_combat(80, "Mackogneur", 25, 20, 30)
                                XP = arene3 [0]
                                starter = arene3 [1]
                                hp_starter = arene3 [2]
                                hp_starter = 60
                                state_combat = arene3 [3]
                                nbr_Dracochoc = arene3 [4]
                                nbr_Lame_Air = arene3 [5]
                                nbr_Ultralaser = arene3 [6]
                                nbr_Flammèche = arene3 [7]
                                nbr_LanceFlammes = arene3 [8]
                                nbr_Rebondifeu = arene3 [9]
                                nbr_Pistolet_à_O = arene3 [10]
                                nbr_Siphon = arene3 [11]
                                nbr_Hydrocanon = arene3 [12]
                                nbr_Désherbaffe = arene3 [13]
                                nbr_FouetsLiannes =	arene3 [14]
                                nbr_LammeFeuille = arene3 [15]
                                if state_combat == True:
                                        print("Bravo, vous passez au dresseur suivant !")
                                        print(f"votre premier combat commence !")
                                        state_combat = False
                                        arene4 = boucle_combat(90, "Dracofeu", 25, 20, 30)
                                        XP = arene4 [0]
                                        starter = arene4 [1]
                                        hp_starter = arene4 [2]
                                        hp_starter = 60
                                        state_combat = arene4 [3]
                                        nbr_Dracochoc = arene4 [4]
                                        nbr_Lame_Air = arene4 [5]
                                        nbr_Ultralaser = arene4 [6]
                                        nbr_Flammèche = arene4 [7]
                                        nbr_LanceFlammes = arene4 [8]
                                        nbr_Rebondifeu = arene4 [9]
                                        nbr_Pistolet_à_O = arene4 [10]
                                        nbr_Siphon = arene4 [11]
                                        nbr_Hydrocanon = arene4 [12]
                                        nbr_Désherbaffe = arene4 [13]
                                        nbr_FouetsLiannes =	arene4 [14]
                                        nbr_LammeFeuille = arene4 [15]
                                        nbr_Dracochoc = 15
                                        nbr_Lame_Air = 20
                                        nbr_Ultralaser = 10
                                        nbr_Flammèche = 15
                                        nbr_LanceFlammes = 20
                                        nbr_Rebondifeu = 10
                                        nbr_Pistolet_à_O = 15
                                        nbr_Siphon = 20
                                        nbr_Hydrocanon = 10
                                        nbr_Désherbaffe = 15
                                        nbr_FouetsLiannes =	20
                                        nbr_LammeFeuille = 10
                                        if state_combat == True:
                                                print("Bravo, tu es le nouveau maitre de cette arènes Pokémon ! ")
                                                boutique()
                                        else:
                                                print("Dommage… La prochaine fois peut-être.")
                                                print(f"Vous sortez des arènes pokémons, la queue entre les jambes (#tapette)")
                                                input("↓")
                                                print(f"À la sortie des arenes Pokémon vous rencontrés votre mère qui a honte de vous. Elle vous ramène alors jusqu'à chez vous et vous finissez votre vie à jouer à LOL comme un gros puant #pasdemeufscommemathruin")
                                                game_over ()
                                else:
                                        print("Dommage… La prochaine fois peut-être.")
                                        print(f"Vous sortez des arènes pokémons, la queue entre les jambes (#tapette)")
                                        input("↓")
                                        print(f"À la sortie des arenes Pokémon vous rencontrés votre mère qui a honte de vous. Elle vous ramène alors jusqu'à chez vous et vous finissez votre vie à jouer à LOL comme un gros puant #pasdemeufscommemathruin")
                                        game_over ()
                        else:
                                print("Dommage… La prochaine fois peut-être.")
                                print(f"Vous sortez des arènes pokémons, la queue entre les jambes (#tapette)")
                                input("↓")
                                print(f"À la sortie des arenes Pokémon vous rencontrés votre mère qui a honte de vous. Elle vous ramène alors jusqu'à chez vous et vous finissez votre vie à jouer à LOL comme un gros puant #pasdemeufscommemathruin")
                                game_over ()
        else:
                print(f"Vous sortez des arènes pokémons, la queue entre les jambes (#tapette)")
                input("↓")
                print(f"À la sortie des arenes Pokémon vous rencontrés votre mère qui a honte de vous. Elle vous ramène alors jusqu'à chez vous et vous finissez votre vie à jouer à LOL comme un gros puant #pasdemeufscommemathruin")
                game_over ()

def forêt_pangorn ():
        global XP, starter, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter
        print(f"Après quelques dizaines de minutes de marche, vous arrivez à l'entrée de la forêt Pangorn")
        input("↓")
        print(f"{prenom} : j'entends de l'eau qui coule vers l'ouest. J'aprçois une lueur pas loin devant moi. J'entends aussi la terre qui tremble à quelques centaines de mètres à ma droite")
        input("↓")
        print(f"Que voulez vous faire :")
        print(f"1)Se diriger vers les bruits de l'eau\n2)S'approcher de la lueur\n3)Se rendre aux lieux des tremblements de terre")
        response_9 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
        while not response_9 in (1,2,3):
                print(f"Veuillez saisir un nombre correct")
                print(f"1)Se diriger vers les bruits de l'eau\n2)S'approcher de la lueur\n3)Se rendre aux lieux des tremblements de terre")
                response_9 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
        if response_9 == 1 :
                print(f"Vous êtes émerveillé par une magnifique cascade cependant vous ne vous rendez même pas compte qu'un Crocodil vous observe")
                input("↓")
                print(f"Le Crocodil vous saute dessus seulement vous le voyez au dernier moment et vus avez le choix entre esquiver en vous baissant ou en sautant vers la rivière")
                input("↓")
                print(f"que voulez vous faire ?")
                print(f"1)esquiver en se baissant\n2)esquiver en sautant vers la rivière")
                response_10 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
                while not response_10 in (1,2,3):
                        print(f"Veuillez saisir un nombre correct")
                        print(f"1)esquiver en se baissant\n2)esquiver en sautant vers la rivière")
                        response_10 : int(input("que choisissez vous ? (sélectionnez le numéro) : "))
                if response_10 == 1 :
                        Croco_griffe = random.randint(1,2)
                        if Croco_griffe == 1:
                                print(f"Le crocodil vous érafle le dos mais vous êtes légèrment blessé, il va falloir consulter un médecin")
                                medecin ()
                                input("↓")
                                print(f"Le Crocodil se dresse devant vous, préparez vous au combat !")
                                combat10 = boucle_combat(65, "Crocodil", 15, 10, 20)
                                XP = combat10 [0]
                                starter = combat10 [1]
                                hp_starter = combat10 [2]
                                hp_starter = 60
                                nbr_Dracochoc = combat10 [4]
                                nbr_Lame_Air = combat10 [5]
                                nbr_Ultralaser = combat10 [6]
                                nbr_Flammèche = combat10 [7]
                                nbr_LanceFlammes = combat10 [8]
                                nbr_Rebondifeu = combat10 [9]
                                nbr_Pistolet_à_O = combat10 [10]
                                nbr_Siphon = combat10 [11]
                                nbr_Hydrocanon = combat10 [12]
                                nbr_Désherbaffe = combat10 [13]
                                nbr_FouetsLiannes = combat10 [14]
                                nbr_LammeFeuille = combat10 [15]
                                nbr_Dracochoc = 15
                                nbr_Lame_Air = 20
                                nbr_Ultralaser = 10
                                nbr_Flammèche = 15
                                nbr_LanceFlammes = 20
                                nbr_Rebondifeu = 10
                                nbr_Pistolet_à_O = 15
                                nbr_Siphon = 20
                                nbr_Hydrocanon = 10
                                nbr_Désherbaffe = 15
                                nbr_FouetsLiannes =20
                                nbr_LammeFeuille = 10
                                boutique ()
                        else:
                                print(f"vous avez esquivé de justesse, préparez vous au combat !")
                elif response_10 == 2 :
                        print(f"Vous vous retrouvez au bord de la rivière et un léviator surgit et vous mange tout cru !")
                        game_over ()
        elif response_9 == 2 :
                print(f"Au fur et à mesure que vous vous approchez de la lumière vous sentez une odeur de brûlé")
                input("↓")
                print(f"Vous avez trop avancé et vous êtes maintenant encerclés par des flammes. Vite il faut s'échapper !")
                input("↓")
                print(f"En vous retournant vous vous retrouvez face à un Ouisticram qui vous bloque le passage. Préparez-vous au combat !")
                #combat
                combat5 = boucle_combat(65, "Ouisticram", 15, 10, 20)
                XP = combat5 [0]
                starter = combat5 [1]
                hp_starter = combat5 [2]
                hp_starter = 60
                nbr_Dracochoc = combat5 [4]
                nbr_Lame_Air = combat5 [5]
                nbr_Ultralaser = combat5 [6]
                nbr_Flammèche = combat5 [7]
                nbr_LanceFlammes = combat5 [8]
                nbr_Rebondifeu = combat5 [9]
                nbr_Pistolet_à_O = combat5 [10]
                nbr_Siphon = combat5 [11]
                nbr_Hydrocanon = combat5 [12]
                nbr_Désherbaffe = combat5 [13]
                nbr_FouetsLiannes = combat5 [14]
                nbr_LammeFeuille = combat5 [15]
                nbr_Dracochoc = 15
                nbr_Lame_Air = 20
                nbr_Ultralaser = 10
                nbr_Flammèche = 15
                nbr_LanceFlammes = 20
                nbr_Rebondifeu = 10
                nbr_Pistolet_à_O = 15
                nbr_Siphon = 20
                nbr_Hydrocanon = 10
                nbr_Désherbaffe = 15
                nbr_FouetsLiannes = 20
                nbr_LammeFeuille = 10
                boutique ()
        elif response_9 == 3 :
                print(f"Vous vous rapprochez des tremblements de terre, et vous apercevez un onix mais il n'a pas l'air dans son état normal, il se tape contre une falaise...")
                input("↓")
                print(f"cependant à cause des secousses vous trébuchez et vous vous retrouvez par terre")
                input("↓")
                print(f"à cause des coups donnés par onix sur la falaise des rochers tombent droit sur vous !")
                input("↓")
                print(f"Que voulez vous faire ?")
                print(f"1)se cacher derrière un arbre\n 2)plonger en avant")
                response_13 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
                while not response_13 in (1,2):
                        print(f"Veuillez saisir un nombre correct")
                        print(f"1)se cacher derrière un arbre\n 2)plonger en avant")
                        response_13 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
                if response_13 == 1:
                        arbre = random.randint(1,4)
                        if arbre == 1 :
                                print(f"Un rocher vous à éraflé dans sa chute, vous êtes plutôt sérieusement blessé, il va falloir se rendre chez un médecin")
                                medecin ()
                                onix_secret ()
                        else :
                                print(f"Vous avez réussi à esquiver la chute de rochers, mais pourquoi le Onix est-il aussi intrigué par cette falaise ?")
                                onix_secret()
                else :
                        print(f"vous vous êtes foulé la cheville mais vous avez esquivé la chute de rochers, cependant il va falloir se rendre chez un médecin")
                        medecin ()
                        onix_secret()
def onix_secret ():
        global XP, starter, nbr_Flammèche, nbr_LanceFlammes, nbr_Rebondifeu, nbr_Pistolet_à_O, nbr_Siphon, nbr_Hydrocanon, nbr_Désherbaffe, nbr_FouetsLiannes, nbr_LammeFeuille, nbr_pokeball, nbr_superball, nbr_hyperball, nbr_superpotion, nbr_hyperpotion, monnaie, hp_starter
        print(f"Il va falloir combattre pour savoir ce qui intrigue ce onix !")
        #combat onix
        combat6 = boucle_combat(70, "Onix", 15, 10, 20)
        XP = combat6 [0]
        starter = combat6 [1]
        hp_starter = combat6 [2]
        hp_starter = 60
        nbr_Dracochoc = combat6 [4]
        nbr_Lame_Air = combat6 [5]
        nbr_Ultralaser = combat6 [6]
        nbr_Flammèche = combat6 [7]
        nbr_LanceFlammes = combat6 [8]
        nbr_Rebondifeu = combat6 [9]
        nbr_Pistolet_à_O = combat6 [10]
        nbr_Siphon = combat6 [11]
        nbr_Hydrocanon = combat6 [12]
        nbr_Désherbaffe = combat6 [13]
        nbr_FouetsLiannes = combat6 [14]
        nbr_LammeFeuille = combat6 [15]
        nbr_Dracochoc = 15
        nbr_Lame_Air = 20
        nbr_Ultralaser = 10
        nbr_Flammèche = 15
        nbr_LanceFlammes = 20
        nbr_Rebondifeu = 10
        nbr_Pistolet_à_O = 15
        nbr_Siphon = 20
        nbr_Hydrocanon = 10
        nbr_Désherbaffe = 15
        nbr_FouetsLiannes = 20
        nbr_LammeFeuille = 10
        boutique()
        print(f" Pfiou, ce combat n'était pas facile mais que cache cette falaise ? Je n'ai d'autre choix que d'escalader mais c'est risqué !")
        input("↓")
        print(f"Que voulez-vous faire ?")
        print(f"1) Grimper la falaise\n2)Rebrousser chemin")
        response_14 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
        while not response_14 in (1,2):
            print(f"Veuillez saisir un nombre correct")
            print(f"1) Grimper la falaise\n2)Rebrousser chemin")
            response_14 = int(input("que choisissez vous ? (sélectionnez le numéro) : "))
        if response_14 == 1 :
                print(f"{prenom} : c'est parti pour une petite séance d'escalade !")
                chutes = 0
                bonnes_prises = 0
                while chutes != 5 and bonnes_prises != 5:
                    response_15 = int(input("Que voulez vous faire ? : \n1)Monter la main gauche ?\n2)Monter la main droite ? (sélectionnez le numéro) : "))
                    while not response_15 in (1,2):
                        print(f"Veuillez saisir un nombre correct")
                        reponse_15 = int(input("Que voulez vous faire ? : \n1)Monter la main gauche ?\n2)Monter la main droite ? (sélectionnez le numéro) : "))
                    if response_15 == 1:
                    	print(f"La prise ne tient pas, vous êtes tombé(e)")
                    	chutes += 1
                    	bonnes_prises = 0
                    	print(f"Vous avez {chutes} chute(s) et les bonnes prises ont été remise à {bonnes_prises}. \n	⚠️ Attention à ne pas trop chuter ! ⚠️")
                    else :
                    	print(f"La prise tient, reste plus qu'à continuer comme ça !")
                    	bonnes_prises += 1
                    	print(f"Vous avez {chutes} chute(s) et {bonnes_prises} bonnes prises. \n	⚠️ Attention à ne pas trop chuter ! ⚠️")
                    if bonnes_prises == 5 :
                    	print(f"{prenom} : Pas simple cette ascension mais je suis enfin arrivé dans cette grotte qui intrguait le Onix")
                    	input("↓")
                    	print(f"Vous avancez jusqu'au fond de la grotte et un caillou avec une forme étrange se trouve au centre de la grotte")
                    	input("↓")
                    	print(f"Vous venez de trouver un fossile mâchoire ! Ce fossile, si les conditions sont réunies, va se transformer en un ptyranidur !")
                    	input("↓")
                    	print(f"{prenom} : Quel incroyable trésor ! Il est peut-être temps de partir maitenant")
                    	fossile += 1
                    	if fossile == 2:
                                print(f"\n Vos fossiles semble s'agiter ! \n\n Vous remarquez qu'il s'assemblent parfaitement.\nQue se passe-t-il, un rayquaza apparait !")
                                ray=int(input("\nVoulez vous mettre Rayquaza comme Pokémon principal de votre équipe ? \n\n1) Oui\n2) Non"))
                                if ray == 1:
                                        print(f"Rayquaza a été ajouté à votre équipe !")
                                        starter = 13
                                else:
                                        print(f"Rayquaza n'a pas été ajouté à votre équipe et disparait ! ")
                    else :
                       print(f"vous êtes tombés trop de fois, vous êtes morts de chute")
                       game_over ()
        else:
                print(f"Vous rebroussez chemin ! ") 

#Introduction
print(f"Homme mystérieux : Bonjour jeune homme! Tu es perdu ? Tu ne devrais pas te promener seul dans la forêt si tard le soir ! Il y a des rumeurs comme quoi cette forêt abrite les Pokemons les plus dangereux.")
input("↓")
print(f"Homme mystérieux : Comment t'appelles tu ? ") 
prenom = input("Indiquez votre nom : ")
print(f"Homme mystérieux : Viens {prenom}, je vais te ramener chez tes parents, c'est dangereux ici !")
input("↓")
print(f"10 jours plus tard, alors que vous vous promenez dans Perdium, vous croisez une foule entourant l'homme que vous aviez croisé dans la forêt.") 
input("↓")

#Premier choix 
print(f"Que voulez vous faire :")
print(f"1)Aller voir la foule de plus près\n2)Partir dans le sens opposé") 
response_1 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
while not response_1 in (1,2):
	print(f"Veullez saisir un nombre correct")
	print(f"1)Aller voir la foule de plus près\n2)Partir dans le sens opposé") 
	response_1 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
#Branche 1 (direct foule) 
if int(response_1) == 1:
	print(f"Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
	input("↓")
	print(f"Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
	input("↓")
	print(f"{prenom} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
	input("↓")
	print(f"Homme mystérieux : Je viens visiter mon village natal, tu ne me connais pas ? ")
	input("↓")
	print(f"{prenom} : Non! Qui êtes-vous ?")
	input("↓")
	print(f"Homme mystérieux : Je suis le tout nouveau maitre Pokémon. Je viens de gagner le combat final de la ligue Pokémon")
	input("↓")
	print(f"{prenom} : La ligue Pokémon ? C'est quoi ? ")	
	input("↓")
	print(f"Homme mystérieux : Tu ne connais pas la ligue Pokémon ?")
	input("↓")
	print(f"{prenom} : Non, c'est quoi ?")
	input("↓")
	print(f"Homme mystérieux : C'est une ligue connue à l'internationale où tout les combattants pokémon s'affrontent pour savoir qui est le meilleur dresseur, ça t'intéresse ?")
	input("↓")
	print(f"Que voulez vous faire :")
	print(f"1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
	response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	while not response_2 in (1,2):
		print(f"Veuillez saisir un nombre correct")
		print(f"1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
		response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
	#branche 1-1 (il accepte le défi de devenir dresseur) 
	if int(response_2) == 1:
		print(f"{prenom} : Oui je veux entrer dans le monde Pokémon !")
		input("↓")
		print(f"Homme mystérieux : Très bien alors il est temps de choisir ton premier pokémon !")
	#Branche 1-2 (il renonce au défi fin du jeu) 
	elif int(response_2) == 2:
		print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
		game_over ()
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
		print(f"{prenom} : Je m'appelle {prenom}, je suis de retour ici, et toi comment tu t'appelles?")
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
			print(f"{prenom} : Oui bien sûr, ça te dit qu'on se rapproche de la foule ?")
			input("↓")
			print(f"Vous vous rapprochez de la foule")
			input("↓")
			print(f"Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
			input("↓")
			print(f"Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
			input("↓")
			print(f"{prenom} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
			input("↓")
			print(f"Homme mystérieux : Je viens visiter mon village natal, tu ne me connais pas ? ")
			input("↓")
			print(f"{prenom} : Non! Qui êtes-vous ?")
			input("↓")
			print(f"Homme mystérieux : Je suis le tout nouveau maitre Pokémon. Je viens de gagner le combat final de la ligue Pokémon")
			input("↓")
			print(f"{prenom} : La ligue Pokémon ? C'est quoi ? ")	
			input("↓")
			print(f"Homme mystérieux : Tu ne connais pas la ligue Pokémon ?")
			input("↓")
			print(f"{prenom} : Non, c'est quoi ?")
			input("↓")
			print(f"Homme mystérieux : C'est une ligue connue à l'internationale où tout les combattants pokémon s'affrontent pour savoir qui est le meilleur dresseur, ça t'intéresse ?")
			print(f"Que voulez vous faire :")
			print(f"1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
			response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
			while not response_2 in (1,2):
				print(f"Veuillez saisir un nombre correct")
				print(f"1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
				response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
			#branche 1-1 (il accepte le défi de devenir dresseur) 
			if int(response_2) == 1:
				print(f"{prenom} : Oui je veux entrer dans le monde Pokémon !")
				print(f"Homme mystérieux : Très bien alors il est temps de choisir ton premier pokémon !")
		#Branche 1-2 (il renonce au défi fin du jeu) 
			elif int(response_2) == 2:
				print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
				game_over ()
		elif int(response_4)== 2:
				print(f"{prenom} : Non désolé je suis trop occupé, à la prochaine")
				print(f"Vous regretterez sans doute ce choix...")
				amitié += 1
				print(f"Attiré par les bruits de la foule, vous vous rapprochez")
				input("↓")
				print(f"Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
				input("↓")
				print(f"Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
				input("↓")
				print(f"{prenom} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
				input("↓")
				print(f"Homme mystérieux : Je viens visiter mon village natal, tu ne me connais pas ? ")
				input("↓")
				print(f"{prenom} : Non! Qui êtes-vous ?")
				input("↓")
				print(f"Homme mystérieux : Je suis le tout nouveau maitre Pokémon. Je viens de gagner le combat final de la ligue Pokémon")
				input("↓")
				print(f"{prenom} : La ligue Pokémon ? C'est quoi ? ")	
				input("↓")
				print(f"Homme mystérieux : Tu ne connais pas la ligue Pokémon ?")
				input("↓")
				print(f"{prenom} : Non, c'est quoi ?")
				input("↓")
				print(f"Homme mystérieux : C'est une ligue connue à l'internationale où tout les combattants pokémon s'affrontent pour savoir qui est le meilleur dresseur, ça t'intéresse ?")
				input("↓")
				print(f"Que voulez vous faire :")
				print(f"1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
				response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
				if int(response_2) == 1:
					print(f"{prenom} : Oui je veux entrer dans le monde Pokémon !")
					print(f"Homme mystérieux : Très bien alors il est temps de me prouver que tu en es capable !")
				elif int(response_2) == 2:
					print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
					game_over ()
	elif int(response_3)== 2:
		print(f"{prenom} : Non désolé je suis trop occupé, à la prochaine")
		input("↓")
		print(f"Vous regretterez sans doute ce choix...") 
		amitié += 1
		print(f"Attiré par les bruits de la foule, vous vous rapprochez")
		input("↓")
		print(f"Alors que vous vous approchez de la foule, l'homme au milieu de la foule vous remarque et vous interpelle ! ")
		input("↓")
		print(f"Homme mystérieux : Comment ça va depuis notre dernière rencontre ?")
		input("↓")
		print(f"{prenom} : Ça va mais pourquoi es-tu entouré de toute cette foule ? ")
		input("↓")
		print(f"Homme mystérieux : Je viens visiter mon village natal, tu ne me connais pas ? ")
		input("↓")
		print(f"{prenom} : Non! Qui êtes-vous ?")
		input("↓")
		print(f"Homme mystérieux : Je suis le tout nouveau maitre Pokémon. Je viens de gagner le combat final de la ligue Pokémon")
		input("↓")
		print(f"{prenom} : La ligue Pokémon ? C'est quoi ? ")	
		input("↓")
		print(f"Homme mystérieux : Tu ne connais pas la ligue Pokémon ?")
		input("↓")
		print(f"{prenom} : Non, c'est quoi ?")
		input("↓")
		print(f"Homme mystérieux : C'est une ligue connue à l'internationale où tout les combattants pokémon s'affrontent pour savoir qui est le meilleur dresseur, ça t'intéresse ?")
		input("↓")
		print(f"Que voulez vous faire :")
		print(f"1)Oui je veux me lancer dans le monde Pokémon!\n2)Non merci ça ne m'intéresse pas") 
		response_2 = int(input("Que choisissez vous ? (sélectionnez le numéro) : "))
		if int(response_2) == 1:
			print(f"{prenom} : Oui je veux entrer dans le monde Pokémon !")
			input("↓")
			print(f"Homme mystérieux : Très bien alors il est temps de me prouver que tu en es capable !")
		elif int(response_2) == 2:
			print(f"Homme mystérieux : Tant pis, ça n'est pas fait pour tout le monde. Tu ne me semblais pas avoir les épaules pour ce challenge.")
			game_over ()
#le jouer fait son premier combat tutoriel 
print(f"Homme Mysterieux : Tiens prend ce Pikachu et essaye de vaincre le Pikachu adverse ! Si tu réussis à le vaincre je te laisserais prendre un de mes pokémons pour commencer ton aventure !")
hppokefightinitial = 50
hp_fight_ini_joueur = 300
nbrattaque1 = 15
nbrattaque2 = 20
nbrattaque3 = 10
while hppokefightinitial > 0:
	print(f"\nle pokemon adverse a {hppokefightinitial} points de vie, quel voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon")
	choix=int(input("\nchoisissez le bon numéro "))
	while not choix in (1,2,3):
		print(f"\nVeuillez saisir un nombre correct")
		print(f"\nle pokemon adverse a {hppokefightinitial} points de vie, quel voulez vous faire ? \n1) Attaquer \n2) Se soigner \n3) Changer de pokémon")
		choix=int(input("\nchoisissez le bon numéro "))
	if choix == 1: 
		print(f"\nQuelle attaque voulez vous utiliser ? \n1)Éclair (-15 hp) {nbrattaque1}/15 \n2)Cage-Éclair (-10 hp) {nbrattaque2}/20 \n3)Tonnerre (-20 hp) {nbrattaque3}/10 ")
		quelle_attaque=int(input("\nchoisissez le bon numéro "))
		if quelle_attaque == 1:
			if nbrattaque1 > 0:
				hppokefightinitial = hppokefightinitial - 15 
				nbrattaque1 = nbrattaque1 - 1
			else:
				print(f"\nVous n'avez plus d'Éclair veuillez en chosir une autre ")
		elif quelle_attaque == 2: 
			if nbrattaque2 > 0:
				hppokefightinitial = hppokefightinitial - 10 
				nbrattaque2 = nbrattaque2 - 1
			else:
				print(f"\nVous n'avez plus de Cage-Éclaire veuillez en chosir une autre ")
		elif quelle_attaque == 3: 
			if nbrattaque3 > 0:
				hppokefightinitial = hppokefightinitial - 20 
				nbrattaque3 = nbrattaque3 - 1
			else:
				print(f"\nVous n'avez plus de Tonerre veuillez en chosir une autre ")
	elif choix == 2:
		print(f"\nQuelle objet pour se soigner ? \n1)super potion \n2)hyper potion ")
		choixsoin=int(input("Quel objet choisissez vous ?"))
		while not choixsoin in (1,2):
			print(f"\nVeuillez saisir un nombre correct")
			print(f"\nQuelle objet pour se soigner ? \n1)super potion \n2)hyper potion ")
			choixsoin=int(input("Quel objet choisissez vous ?"))
		if choixsoin == 1: 
			hp_fight_ini_joueur += 20
			nbr_superpotion -= 1
		elif choixsoin == 2: 
			hp_fight_ini_joueur = 60 
			nbr_hyperpotion -= 1
	else: 
		print(f"\ntu n'as pas le droit")
	if hppokefightinitial < 10:
		proba_soin=random.randint(1,3)
		if proba_soin == 1:
			print(f"\nle pokemon adverse se soigne ! Il regénère 10 hp")
			hppokefightinitial = hppokefightinitial + 1 
		else: 
			proba_attaque=random.randint(1,2)
			if proba_attaque == 1:
				print(f"il utilise Éclair")
				hp_fight_ini_joueur -= 2 
			elif proba_attaque == 2:
				print(f"il utilise Cage-Éclair")
				hp_fight_ini_joueur -= 1
			elif proba_attaque == 3:
				print(f"il utilise Tonnerre")
				hp_fight_ini_joueur -= 5

	else: 
			proba_attaque=random.randint(1,2)
			if proba_attaque == 1:
				print(f"il utilise Éclair")
				hp_fight_ini_joueur -= 2 
			elif proba_attaque == 2:
				print(f"il utilise Cage-Éclair")
				hp_fight_ini_joueur -= 1
			elif proba_attaque == 3:
				print(f"il utilise Tonnerre")
				hp_fight_ini_joueur -= 5
print(f"Bravo ! Tu as gagné ton premier combat (tu ne pouvais pas perdre donc prend pas trop la confiance sale merde")
input("↓")
print(f"homme mystérieux : Tu es maintenant un dresseur pokémon ! Différents choix s'offrent à toi. Tu peux par exemple partir pour les arènes pokémons pour essayer de gagner des récompenses et faire évoluer ton pokémon")
input("↓")
print(f"homme mystérieux : tu peux aussi partir pour la forêt pangorn à proximité pour obtenir de nouveaux pokémons mais fais attention à prendre des pokéballs avec toi")
input("↓")
print(f"homme mystérieux : il existe de nombreuses villes à proximité si l'envie t'ne prends de faire du tourisme")
input("↓")
print(f"homme mystérieux : Tu peux même si tu le souhaites explorer les environs")
input("↓")
print(f"mais d'abord choisis un de mes pokémons : ")
input("↓")
print(f"Homme mystérieux : Alors, quel Pokémon t'acompagneras dans ton aventure vers la ligue Pokémon ?\n1) Arcko (Type Plante)\n2) Poussifeu (Type Feu)\n3) Gobou (Type Eau)")
starter = int(input("Quel Pokémon choisissez vous ? (sélectionnez le numéro correspondant) : "))
while not starter in {1,2,3} : 
    print(f"Vous vous êtes trompés de numéro")
    print(f"Homme mystérieux : Alors, quel Pokémon t'acompagneras dans ton aventure vers la ligue Pokémon ?\n1) Arcko (Type Plante)\n2) Poussifeu (Type Feu)\n3)Gobou (Type Eau)")
    starter = int(input("Quel Pokémon choisissez vous ? (sélectionnez le numéro correspondant) : "))
    starter = 1
if starter == 1:
    print(f"Arcko a été ajouté à ton Pokédex !")
    print(f"Arcko est un pokémon de type Plante, cela veut dire qu'il sera très éfficace face aux Pokémons de type Eau, Roche et Sol !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
elif starter == 2:
    print(f"Poussifeu a été ajouté à ton Pokédex !")
    print(f"Poussifeu est un pokémon de type Feu, cela veut dire qu'il sera très éfficace face aux Pokémons de type Plante et Glace !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
    starter = 2
elif starter == 3:
    print(f"Gobou a été ajouté à ton Pokédex !")
    print(f"Gobou est un pokémon de type Eau, cela veut dire qu'il sera très éfficace face aux Pokémons de type Feu, Roche et Sol !\nIl faut donc que tu sois attentif au type du Pokémon adverse afin de gagner tes combats plus facilement")
    starter = 3
print(f"homme mystérieux : très bon choix, je te conseille avant de partir de passer par la boutique pour te munir de gadgets très utiles lors de tes combats")
print(f"homme mystérieux : Combien d'argent as tu sur toi ?")
print(f"{prenom} : j'ai {monnaie} monnaie sur moi actuellement")
boutique ()
print(f"Maintenant tu es prêt à visiter l'île, profite de ton aventure.")
chemins = {
    "1": ("Ville Donjon", ville_donjon),
    "2": ("La forêt Pangorn", forêt_pangorn),
    "3": ("Les arênes Pokémon", arènes_pokémons),
    "4": ("Le Volcan instable de l'île", grotte_boss)
}
while chemins:
    print(f"\nChemins disponibles :")
    for numero, (nom, _) in chemins.items():
        print(f"{numero} - {nom}")

    choix = input("Choisis un chemin : ") 

    if choix in chemins:
        nom, fonction = chemins[choix]
        print(f"\nTu as choisi : {nom}\n")
        fonction()  #  Lance la fonction liée
        del chemins[choix]  #  Supprime le chemin
    else:
        print(f"Choix invalide, fais un effort !")

print(f"\n Game Over ! ")
