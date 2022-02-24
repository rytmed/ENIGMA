def ecrire ():

    fichier = open("sources.txt", "a")
    fichier.write(input("votre message"))
    fichier.close()

ecrire() 