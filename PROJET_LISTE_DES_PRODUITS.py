#  Projet Liste des courses

from sys import *
LISTE =[]
menu=""""Choisissez parmi les cinq options suivantes :
1. Ajouter un élément à la liste de courses.
2. Retirer un élément de la liste de courses.
3. Afficher les éléments de la liste de courses.
4. Vider la liste de courses.
5. Quitter le programme.   """

Liste_de_choix=["1","2","3","4","5"]

while True:
    print(menu)
    choix =input("ENTRER VORTRE CHOIX :")

    for element in Liste_de_choix:
      while choix not in Liste_de_choix:
        print(menu)
        choix =input("ENTRER VORTRE CHOIX :")

    if choix==Liste_de_choix[0]:
       ajout=input("Entrer le nom de l'element a ajouter : ")
       while ajout.isdigit():
          ajout =input("Entrer le nom de l'element a ajouter : ")
       LISTE.append(ajout)  
       print(f" L'ELEMENT {ajout} A BIEN ETE AJOUTE.\n")  
     
    elif choix==Liste_de_choix[1]:
        supprimer=input("Entrer le nom de l'element a supprimer :")
        if supprimer not in LISTE:
            print(f"L'element {supprimer} n'existe pas dans la liste.\n")
        else :
            LISTE.remove(supprimer)
            print(f"L'element {supprimer} a bien ete supprimer de la liste.\n")  

    elif choix==Liste_de_choix[2] :
        for i,element in enumerate(LISTE,1):
            print(f"{i}. {element}")

    elif choix==Liste_de_choix[3]:
        LISTE.clear()
        print("La liste a ete videe")

    elif choix==Liste_de_choix[4] :
        print("MERCI ET A BIENTOT.")
        exit()       
    print("-"*50)
