import random
nombre=random.randint(1,20)

deviner= int(input("Je pense un nombre entre 1 et 20. Lequel est ce? "))
while deviner!=nombre:
    if deviner<nombre:
        print ("ton nombre est trop bas")
    else:
        print("ton nombre est trop haut")
    deviner= int(input("Essaie à nouveau"))

print ("Félicitations! Bonne Réponse")
