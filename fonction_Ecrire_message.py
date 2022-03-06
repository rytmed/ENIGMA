import unidecode
def ecrire_de_message(message, nom_de_ficher):
    print('merd')
    message = message.upper()
    message = message.replace(" ","")
    message = unidecode.unidecode(message)
    try :
        with open(nom_de_ficher, 'W') as fichier:
            fichier.write(message)
    except Exception:
        return False
        
    return True 
print(ecrire_de_message('Gasien','sources.txt'))

