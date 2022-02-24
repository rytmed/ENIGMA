#Fonction de lecture du message entré par l'utilisateur
def LectureMessage():
    with open("sources.txt", "r", encoding='utf-8') as fichier:
        for item in fichier.readlines() :
            print("/n" + item)
    return 1

LectureMessage()
