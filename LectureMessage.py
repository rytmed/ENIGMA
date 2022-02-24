#Fonction de lecture du message entré par l'utilisateur
def LectureMessage():
    with open("message.txt", "r", encoding='utf-8') as fichier:
        return fichier.read()

LectureMessage()
