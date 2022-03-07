import unidecode
import rotors

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
			LectureMessage("message.txt")
		elif choix == 2 :
			SauvegardeMessage("dddddfgg gfg", "message.txt")
		elif choix == 3:
			print(f"Que voulez vous faire ?.\n"
			"1. Cryptage\n"
			"2. Décryptage\n")
			choix = faire_choix(f"Quel est votre choix(elle doit être dans [1, 2] ) ?\n")
			data = rotors.checkInput()
			cryptage = True if choix == 1 else False
			print(rotors.cryptage(formatString(data[0]), data[1], cryptage))
		elif choix == 4 :
			print("\n vous quittez ! Aplus")
			false_input = False
		else :
			false_input = True

def formatString(msg):
	msg = msg.upper()
	msg = msg.replace(" ","")
	msg = unidecode.unidecode(msg)
	return msg

def LectureMessage(source_file):
	try:
		with open(source_file, "r",encoding="utf8") as fichier:
			return (formatString(fichier.read()))
	except Exception:
		raise Exception("Une erreur s'est produit, vérifier le fichier ainsi que son chemin et réessayé")

def SauvegardeMessage(message, nom_de_ficher):
	try :
		with open(nom_de_ficher, 'w', encoding="utf8") as fichier:
			fichier.write(message)
	except Exception:
		return False
	return True 

