

import unidecode
def ecrire_de_message(message,nom_de_ficher):
    
    message = message.upper()
    message = message.replace(" ","")
    message = unidecode.unidecode(message)
    fichier = open(nom_de_ficher, "a")
    fichier.write(message)
    fichier.close()
    return True
print(ecrire_de_message('Hello','sources.txt'))


