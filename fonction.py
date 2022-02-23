'''Fonction menu machine ENIGMA
Fonctions utilisées : menu(), LectureMessage(fichier,mesg), RecMessage(fichier,mesg), Cryptage(fichier,mesg), Decryptage(fichier,mesg)'''

def menu():
	print(f"Bienvenue dans la machine ENIGMA.\n"
		"Plusieurs choix s'offrent à vous :\n\n"
		"1. Lecture du message\n"
		"2. Enregistrement du message\n"
		"3. Cryptage/Decryptage\n"
		"4. Quitter")
	choix=int(input(f"Quel est votre choix ?\n"))
	if choix==1:
		LectureMessage(fichier,mesg)
	elif choix==2:
		RecMessage(fichier,mesg)
	elif choix==3:
		cryptochoix=input(f"Souhaitez-vous crypter le message (1) ou le décrypter (2) ?\n")
		while type(cryptochoix)==str:
			cryptochoix=input("Non accepté. Veuillez rentrer 1 pour crypter le message ou 2 pour le décrypter.")
		else:
			if choix==1:
				Cryptage(fichier,mesg)
			else:
				Decryptage(fichier,mesg)
	elif choix==4:
		quit()

menu()
