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
				print(f"{nom_poke_ennemi} est mort ! Félicitations ! ")
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
