def faire_choix(message):
	false_input = True
	while(false_input) : 
		try :  
			choix = int(input(message))
			false_input = False
		except (ValueError):
			false_input = True
			pass
	return choix

def menu():
	print(f"Bienvenue dans la machine ENIGMA.\n"
	"Plusieurs choix s'offrent à vous :\n\n"
	"1. Lecture du message\n"
	"2. Enregistrement du message\n"
	"3. Cryptage\Decryptage\n"
	"4. Quitter")
	false_input = True
	while false_input:
		false_input = False
		choix = faire_choix(f"Quel est votre choix(elle doit etre dans [1, 2, 3, 4] ) ?\n")
		if choix == 1 :
			pass
		elif choix == 2 :
			pass
		elif choix == 3:
			pass
		elif choix == 4 :
			pass
		else :
			false_input = True