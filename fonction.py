def menu():
    print(f"Programme de sélection de la machine ENIGMA. Voici les différentes options :\n\n"
          "1. Lecture message\n"
          "2. Enregistrer message\n"
          "3. Cryptage/Décryptage\n"
          "4. Quitter\n")
    choix=int(input("Quel choix souhaitez-vous faire ?\n"))
    if choix==1:
        LectureMessage()
    elif choix==2:
        EnregistrerMessage()
    elif choix==3:
        Cryptage
    else:
        sys.exit()
menu()