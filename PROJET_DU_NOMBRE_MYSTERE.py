#  Projet du nombre mystere.
from random import *
from sys import *

nombre_mystere = randint(0,100)
p_essai = 5
essai = 1


print("****LE JEU DU NOMBRE MYSTERE***\n")
print (f"IL vous reste {p_essai} essais.")
user_choice = input("Devinez le nombre : ")

while True:
    while not user_choice.isdigit():
        print("Saisie incorrecte.\n")
        print (f"IL vous reste {p_essai} essais.")
        user_choice = input("Devinez le nombre : ")


    if int(user_choice) != nombre_mystere:

        if p_essai !=1:
           p_essai = p_essai-1
           if int(user_choice) < nombre_mystere:
               print(f"Le nombre mystere est superieur a {user_choice}\n")
           else:
               print(f"Le nombre mystere est inferieur a {user_choice}\n")
           print(f"il vous reste {p_essai} essais.")  
           user_choice = input("Devinez le nombre : ")

        elif p_essai == 1:
            print(f"Dommage , le nombre mystere etait : {nombre_mystere}.")
            print("FIN DU JEU")
            exit()


    elif int(user_choice) == nombre_mystere:
      if p_essai == 5:
        print(f"FELICITATIONS , nombre mystere est bien {nombre_mystere}. ")
        print(f"Vous avez reussi en {essai} essais.\n")
        print("FIN DU JEU")
        exit()
      elif p_essai == 4:
        print(f"FELICITATIONS , nombre mystere est bien {nombre_mystere}. ")
        print(f"Vous avez reussi en {essai+1} essais.\n")
        print("FIN DU JEU")
        exit()
      elif p_essai == 3:  
         print(f"FELICITATIONS , nombre mystere est bien {nombre_mystere}. ")
         print(f"Vous avez reussi en {essai+2} essais.\n")
         print("FIN DU JEU")
         exit()
      elif p_essai == 2:
        print(f"FELICITATIONS , nombre mystere est bien {nombre_mystere}. ")
        print(f"Vous avez reussi en {essai+3} essais.\n")
        print("FIN DU JEU")
        exit()
      elif p_essai == 1:
        print(f"FELICITATIONS , nombre mystere est bien {nombre_mystere}. ")
        print(f"Vous avez reussi en {essai+4} essais.\n")
        print("FIN DU JEU")
        exit()
