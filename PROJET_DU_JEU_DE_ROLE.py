from random import *
from sys import *

mes_points = 50
points_ennemi =50
nbre_potion =3




menu ="Souhaitez-vous attaquer(1) ou utilisez une potion(2)? : "
nbre_choix = ["1" , "2"]

while True:

    mes_attaques = randint(5,10)
    attaques_ennemi = randint(5,15)


  

    
    
    points_potion = randint(15,50)
    
    
   
   
   





    choix = input(menu)

    for element in nbre_choix :
        if choix not in nbre_choix :
            choix = input(menu)



    if choix == nbre_choix[0]:
        
        while mes_points >0 and  points_ennemi >0 :
              points_ennemi = points_ennemi - mes_attaques
              mes_points = mes_points - attaques_ennemi

              if mes_points >0 and  points_ennemi >0 :
                print (f"Vous avez inflige a l'ennemi {mes_attaques} points de degats.")
                print (f"l'ennemi vous a inflige {attaques_ennemi} points de degats.")
                print (f"Il vous reste {mes_points} points.")
                print(f"Il reste a l'ennemi {points_ennemi} points.")

              if mes_points <= 0 and mes_points < points_ennemi :
                   print (f"l'ennemi vous a inflige {attaques_ennemi} points de degats.")
                   print("Vous avez perdu.")
                   print("FIN DU JEU.") 
                   exit()
              elif points_ennemi <=0 and mes_points > points_ennemi :
                   print (f"Vous avez inflige a l'ennemi {mes_attaques} points de degats.")
                   print("Vous avez gagne.")
                   print("FIN DU JEU.")
                   exit()      
              break
      




    elif choix == nbre_choix[1]:
           

            if nbre_potion!=0:
                 mes_points = mes_points + points_potion
                 mes_points = mes_points - attaques_ennemi
                 nbre_potion=nbre_potion-1   
                 
                 print(f"Vous avez recupere {points_potion} points.")
                 print(f"Il vous reste {nbre_potion} potions.")
                 print(f"l'ennemi vous a inflige {attaques_ennemi} points.")
                 print(f"Il vous reste {mes_points} points")
                 print(f"Il reste a l'ennemi {points_ennemi} points.")
                 print("-"*50)
                 attaques_ennemi = randint(5,15)
                 mes_points = mes_points - attaques_ennemi
                 print("Vous passez votre tour...")
                 print(f"l'ennemi vous a inflige {attaques_ennemi} points.")
                 print (f"Il vous reste {mes_points} points.")
                 print(f"Il reste a l'ennemi {points_ennemi} points.")
                 continue
                
            elif nbre_potion==0:
              print("Vous n'avez plus de potions.")
              continue






        

       
    print("-"*50)
            




