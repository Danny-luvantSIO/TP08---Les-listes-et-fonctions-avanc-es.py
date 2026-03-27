#EXERCICE 1
from unittest import result


list1=[10, 12, 13, 14, 15]
print(list1)
print("la somme est : ", sum(list1))
print("la moyenne est : ", sum(list1)/len(list1))

print("--------------------------------")
#EXERCICE 2
list=nombres=[2,13,9,41,7,9,12,17,8,21,3,39]
print("les nombres pairs sont : ", [x for x in nombres if x % 2 == 0])
print("les nombres > 10 sont : ", [x for x in nombres if x > 10])
print("la valeur maximale est : ", max(nombres))
print("--------------------------------")
#EXERCICE 3 
def ajouter_note(liste, note):
    liste.append(note)
    return liste
notes = [15, 18, 12]
ajouter_note(notes, 20)
#EXERCICE 4 
def compter_sup(liste, seuil):
    count = 0
    for x in liste:
        if x > seuil:
            count += 1
    return count
#EXERCICE 5
def multiplier_liste(liste, facteur):
    return [x * facteur for x in liste]
#EXERCICE 6
def filtrer_pairs(liste):
    return [x for x in liste if x % 2 == 0] 
#EXERCICE 7
def inverser_liste(liste):
    return liste[::-1]
#EXERCICE 8
def somme_indices_pairs(liste):
    return sum(liste[i] for i in range(len(liste)) if i % 2 == 0)
#EXERCICE 9
def supprimer_doublons(liste):
    return list(set(liste))
#EXERCICE 10
def deux_plus_grands(liste):
    if len(liste) < 2:
        raise ValueError("La liste doit contenir au moins deux éléments")
    triee = sorted(liste, reverse=True)
    return triee[0], triee[1]
#PARTIE B: Mini projet type Pendu
#EXERCICE 6
def afficher_mot_cache(mot, lettres_trouvees):
    resultat = ""
    
    for lettre in mot:
        if lettre in lettres_trouvees:
            resultat += lettre
        else:
            resultat += "_"
    
    return resultat


mot = "python"
lettres_trouvees = ["p", "o"]

resultat = afficher_mot_cache(mot, lettres_trouvees)
print(resultat)


print("--------------------------------")
#EXERCICE 7
def lettre_dans_mot(mot, lettre):
    if lettre in mot: 
        return True
    else:
        return False
lettre_dans_mot("python", "p")
lettre_dans_mot("python", "z")
#EXERCICE 8
def ajouter_lettre(liste, lettre):
    if lettre not in liste:
        liste.append(lettre)
    return liste
lettres = ["p", "o"]
ajouter_lettre(lettres, "p")
ajouter_lettre(lettres, "y")
#EXERCICE 9
def mot_complet(mot, lettres_trouvees):
    for lettre in mot:
        if lettre not in lettres_trouvees:
            return False
    return True
mot = "python"
lettres = ["p", "y", "t", "h", "o", "n"]
#EXERCICE 10#PARTIE B: Mini projet type Pendu
print("---------------EXO 6-----------------")
#EXERCICE 6
def afficher_mot_cache(mot, lettres_trouvees):
    resultat = ""
    
    for lettre in mot:
        if lettre in lettres_trouvees:
            resultat += lettre
        else:
            resultat += "_"
    
    return resultat


mot = "python"
lettres_trouvees = ["p", "o"]

resultat = afficher_mot_cache(mot, lettres_trouvees)
print(resultat)

print("--------------------------------")
#EXERCICE 7
def lettre_dans_mot(mot, lettre):
    if lettre in mot: 
        return True
    else:
        return False
lettre_dans_mot("python", "p")
lettre_dans_mot("python", "z")
#EXERCICE 8
def ajouter_lettre(liste, lettre):
    if lettre not in liste:
        liste.append(lettre)
    return liste
lettres = ["p", "o"]
ajouter_lettre(lettres, "p")
ajouter_lettre(lettres, "y")
#EXERCICE 9
def mot_complet(mot, lettres_trouvees):
    for lettre in mot:
        if lettre not in lettres_trouvees:
            return False
    return True
mot = "python"
lettres = ["p", "y", "t", "h", "o", "n"]
#EXERCICE 10
mot = "python"
lettres_trouvees = []

while True:
    lettre = input("Lettre ? : ")
    lettres_trouvees.append(lettre)

    mot_cache = ""
    for l in mot:
        if l in lettres_trouvees:
            mot_cache += l
        else:
            mot_cache += "_"

    print(mot_cache)

    if "_" not in mot_cache:
        print("Mot trouvé !")
        break
#BONUS
def gerer_erreur(mot, lettre, vies):
    vies = 5
    if lettre not in mot:
        if vies > 0:
            vies -= 1
            print(f"Lettre incorrecte. Il vous reste {vies} vies.")
    return vies
print("--------------------------------")
#Bonus 2
def afficher_etat(mot, lettres_trouvees, lettres_testees):
    
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    
    print("Mot :", mot_cache)

    
    print("Lettres testées :", " ".join(lettres_testees))
#bonus 3
def lettre_deja_proposee(lettre, lettres_testees):
    if lettre in lettres_testees:
        return True
    else:
        return False
#bonus 4 
import random

def choisir_mot(liste_mots):
    return random.choice(liste_mots)
#bonus 5
def lettres_restantes(mot, lettres_trouvees):
    restantes = 0
    for lettre in mot:
        if lettre not in lettres_trouvees:
            restantes += 1
    return restantes
#bonus 6
import random

# Liste de mots
mots = ["python", "reseau", "serveur", "code", "instruction",
        "algorithmie", "boucle", "condition", "fonction", "indentation"]

mot = random.choice(mots)


lettres_trouvees = []
lettres_testees = []
vies = 3


def afficher_etat(mot, lettres_trouvees, lettres_testees, vies):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    
    print("\n===== ÉTAT DU JEU =====")
    print("Mot        :", mot_cache)
    print("Testées    :", " ".join(lettres_testees))
    print("Vies       :", vies)
    print("========================")


def lettre_deja_proposee(lettre, lettres_testees):
    return lettre in lettres_testees


while True:
    afficher_etat(mot, lettres_trouvees, lettres_testees, vies)

    
    if all(l in lettres_trouvees for l in mot):
        print("Mot trouvé !")
        break

    # Vérifier défaite
    if vies <= 0:
        print("Perdu ! Le mot était :", mot)
        break

    
    lettre = input("Lettre ? : ").lower()

    if len(lettre) != 1 or not lettre.isalpha():
        print("Entrée invalide. Tape une seule lettre.")
        continue

    if lettre_deja_proposee(lettre, lettres_testees):
        print("Lettre déjà proposée.")
        continue

    
    lettres_testees.append(lettre)

    
    if lettre in mot:
        lettres_trouvees.append(lettre)
        print("Bonne lettre !")
    else:
        vies -= 1
        print("Mauvaise lettre !")