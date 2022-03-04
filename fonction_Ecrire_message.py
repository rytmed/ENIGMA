

"""
    Je garde cette version pour avoir une idée si j'ai à nouveau des soucis.
import unidecode
def ecrire_de_message(message,nom_de_ficher):
    
    message = message.upper()
    message = message.replace(" ","")
    message = unidecode.unidecode(message)
    fichier = open(nom_de_ficher, "a")
    fichier.write(message)
    fichier.close()
    return True
print(ecrire_de_message('Gasien','sources.txt'))

"""

import re

def ecrire_de_message(message, nom_de_ficher):
    message = message.upper()
    message = message.replace(" ", "")
    message = message.replace("É","E")
    message = message.replace("@","A")
    message = message.replace("À", "A")
    message = message.replace("È","E")
    message = message.replace("€","E")
    message = message.replace("Ù", "U")
    message = message.replace("Ê", "E")
    message = message.replace("$", "S")
    message = message.replace("Ô","O")
    new_message = re.sub(r"[^a-zA-Z0-9]","",message)
    with open("sources.txt", "w") as fichier:
        fichier.write(new_message)
    return True


print(ecrire_de_message('$alùt@tiôn$ mon c@m@rade', 'sources.txt'))