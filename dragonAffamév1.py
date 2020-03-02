print ("tu te trouve dans l'entrée sombre d'un chateau")
print ("tu dois choisir entre 3 portes")
choixJoueur= input ("tapes 1 2 ou 3 ")
if int(choixJoueur)==1 :
    print ("bravo tu as trouvé un trésor")
elif int(choixJoueur)==2 :
    print ('oh non un monstre')
elif int(choixJoueur)==3 : 
    print ('Arf c\' est vide tout ça')
else :
    print("on t'as dit de taper 1 2 ou 3!")
