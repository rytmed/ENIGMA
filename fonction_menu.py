"""Programme pour les fonctions menu(), LectureMessage(fichier,mesg) et SauvegardeMessage(fichier,mesg)"""

#Notre dernière fonction est un menu, qui nous permet d'afficher des choix pour l'utilisateur
def menu():
    print(f"1. Lecture message")
    print(f"2. Ecriture message")
    print(f"3. *")
    print(f"4. Quitter")
    a=int(input(f"Faites un choix dans le menu"))
    if a=1:
        LectureMessage(fichier,mesg)
    elif a==2:
        EcritureMessage(fichier,mesg)
    elif a==3:
        SauvegardeMessage(fichier,mesg)
    elif a==4:
        exit()
    else:
        print("Impossible ! Retour au menu !")
        menu()