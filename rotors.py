#coding: utf-8
import re
import json

""" 
    MODULE CRYPTAGE VERSION SIMPLOFOER MACHINE ENIGMA
"""

# DECLARATION DES CONSTANTES 

# DECLARATION DES FONCTIONS

def checkInput():
    items = []
    while len(items) != 4 :   
        print("Format du message => message rotor2 rotor3 rotor1 ref2")
        data = input("Entrer le message => ")  # exception crt+c à gerer
        match = re.match("[\"\'](.*)[\"\'](.*)", data)
        list_rotors = ""
        if match is not None :    
            msg = match[1]
            list_rotors = match[2]
        list_rotors = list_rotors.strip()
        items = list_rotors.split(" ")
    return [msg, list(items)]

#print("le message est ", checkInput())

def rotor(item, string_equiv, crypt_rot):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return str(string_equiv[alphabet.index(str(item))]) if crypt_rot else str(alphabet[string_equiv.index(str(item))]) #exception à gerer pour index

#print(rotor("X", "EKMFLGDQVZNTOWYHXUSPAIBRCJ"))

def reflecteur(item, string_equiv, crypt_rot):
    return rotor(item, string_equiv, crypt_rot)

def cryptage(msg, list_rotors, crypt_rot): 
    msg_crypt=""
    with open("rotors.json", "r") as f :
        data = f.read()
    dict_rotors = json.loads(data)
    #print(dict_rotors["rotors"])
    for item in msg :
        item_crypt = item
        for i in range(2):
            list_rotors_search = list_rotors[:len(list_rotors)-1] if i == 0 else list_rotors[1:]
            for r in list_rotors_search:
                for val in dict_rotors["rotors"]:
                    if r in val:
                        #print(r)
                        item_crypt = rotor(item_crypt, val[r], crypt_rot)  
                        break 
            if i == 0 :    
                for val in dict_rotors["refleceurs"]:
                    if list_rotors[-1] in val:
                        item_crypt = reflecteur(item_crypt, val[list_rotors[-1]], crypt_rot)  
                        #print(list_rotors[-1])
                        break 
            list_rotors.reverse()           
        msg_crypt += item_crypt
    return msg_crypt
        

#print(cryptage("LCIGUDFBZKRD",["RA","RB","RC","RFA"], False))

#print(cryptage("BAZZETTTYY",["RA","RB","RC","RFB"]))
"""
try:
    
except Exception :
    print("youpi je gere l erreur")
"""


#093986890