'''
3eme option du menu.
Fonction de lecture du message entré par l'utilisateur.
'''
import re  # Bibliothèque des expressions régulières. Va grandement simplifier notre travail.


def LectureMessage():
    global message
    message = message.upper()  # Passer en lettres majuscules sert à réduire le nombre de cas.
    message = message.replace(" ", "")
    message = message.replace("É", "E")
    message = message.replace("@", "A")
    message = message.replace("À", "A")
    message = message.replace("È", "E")
    message = message.replace("€", "E")
    message = message.replace("Ù", "U")
    message = message.replace("Ê", "E")
    message = message.replace("$", "S")
    message = message.replace("Ô", "O")
    message = message.replace("µ", "M")
    new_message = re.sub(r"[^a-zA-Z0-9]", "", message)
    with open("sources.txt", "w") as fichier:
        fichier.write(new_message)
    return print(f'Le nouveau message, après modifications est donc :', new_message)


f = open("sources.txt", "r",
         encoding='utf-8')  # On ouvre le fichier texte contenant notre message pas encore transformé.
message = f.read()
print(f'Le message avant modification est {message}')
f.close()
LectureMessage()
