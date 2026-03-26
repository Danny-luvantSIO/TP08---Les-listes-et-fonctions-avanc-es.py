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
if __name__ == "__main__":
    mot = "python"
    lettres_trouvees = []

    while not mot_complet(mot, lettres_trouvees):
        print("Mot :", afficher_mot_cache(mot, lettres_trouvees))
        lettre = input("Lettre ? : ").strip().lower()
        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre.")
            continue

        if lettre in lettres_trouvees:
            print("Vous avez déjà trouvé cette lettre.")
            continue

        ajouter_lettre(lettres_trouvees, lettre)

    print("Mot :", afficher_mot_cache(mot, lettres_trouvees))
    print("Félicitations, vous avez trouvé PASSE-MURAILLE !")