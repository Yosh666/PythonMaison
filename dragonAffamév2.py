import random#pour le sphinx
choixSortie="Rien"
while choixSortie!="QUITTER":

    print ("tu te trouve dans l'entrée sombre d'un chateau")
    print ("tu dois choisir entre 4 portes")
    choixJoueur= input ("tapes 1 2 3 ou 4 ")
    if int(choixJoueur)==1 :
        print ("bravo tu as trouvé un trésor")

    elif int(choixJoueur)==2 :
        print ('oh non un monstre')
        print ("tu as un choix a faire Tu peux soit : ")
        print ("1 voloer l'or derrière le monstre")
        print ("2  essayer d'échapper a la bête affamée")
        
        choixMonstre= input ("Que choisis tu 1 ou 2 ")
        if int(choixMonstre)==1 :
            print ("le monstre t'as mordu")
            print ("tu deviens un zombie toi même game over")
        
        elif int(choixMonstre)==2 :
            print ("tu t'enfius mais tu es pauvre")
            print ("âs game over mais tout comme")
        
        else :
            print("tu dois rentrer 1 ou 2!")

    elif int(choixJoueur)==3 : 
        print ('Arf c\' est vide tout ça')

    elif int(choixJoueur)==4 :
        print ("tu entres dans une piéce sombre")
        print ("un sphin s'y tient! il te demande :")
        print("Combien de pattes as tu le matin? d'une voix rugissante oui je suis lyrique si je veux")
        nombre=int(input("Choisis ton chiffre! "))

        if nombre==random.randint(1,4):#fonction random randint donne l'intervalle
            print ("tu as deviné juste tu ne mourras pas aujourd'hui")
            print ("voici un souvenir!")
            print ("tu repars avec une plume de sphinx mais toujours pauvre")
        
        else:
            print ("tu es mort !")
            print ("Le sphinx te mange détendu ")
            print ("hey tu auras au moins servi à quelque chose hein c'est déjà ça")

    else :
        print("on t'as dit de taper 1 2 3 ou 4!")
    choixSortie=input("tapes quitter si tu en as marre sinon on recommence ").upper()
    #.upper() passe tout en majuscule
print("tu as quitté le jeu")




