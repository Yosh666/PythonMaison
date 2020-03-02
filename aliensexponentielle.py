print ('------------------------')
print(' OMG LES ALIENS ATTAQUENT')
print ('------------------------')
print ('tu dois sauver le monde en entrant le mot de passe de défense planétaire!')
alien=3
password='XGLUGLU'
tentative=''
while alien<25 :
    tentative=input('Entre le mot de passe: ').upper()
    if tentative !=password:
        alien=alien*3
        print ("les aliens sont maintenant ",alien)
        print ("vite trouve le mot de passe")
    else:
        print ("BRavo tu as sauvé le monde END GAME")

print ("Oh mon dieu les aliens dominent le monde!! Tout est fini GAMEOVER!")