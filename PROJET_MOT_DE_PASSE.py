#MOT DE PASSE
password = input("Entrer votre mot de passe(min 8 caracteres) : ")
mdp_trop_court ="votre mot de passe est trop court."
if len(password) ==0 :
    print(mdp_trop_court.upper())
elif len(password)>0 and len(password)< 8 :
    print(mdp_trop_court.capitalize())
elif len(password)>=8 and password.isdigit() == True:
   print ("Votre mot de passe ne contient que des nombres.")
else :
    print("Inscription terminee.") 