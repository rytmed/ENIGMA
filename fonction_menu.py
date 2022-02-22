"""Programme pour les fonctions menu(), LectureMessage(fichier,mesg) et SauvegardeMessage(fichier,mesg)"""


# Fonction de lecture du message
def LectureMessage(fichier, mesg):
    # On ouvre d'abord le fichier message
    with open("message.txt", "r") as fichier:
        fichi


# Notre dernière fonction est un menu, qui nous permet d'afficher des choix pour l'utilisateur
def menu():
    print(f"1. Lecture message")
    print(f"2. Ecriture message")
    print(f"4. *")
    print(f"6. Quitter")
    a = int(input(f"Faites un choix dans le menu"))
    if a == 1:
        LectureMessage(fichier, mesg)
    elif a == 2:
        EcritureMessage(fichier, mesg)
    elif a == 4:
        SauvegardeMessage(fichier, mesg)
    elif a == 6:
        exit()
    else:
        print(f"Impossible ! Retour au menu !")
        menu()
