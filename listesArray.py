listeEspace=[ "fusée","planéte", "astéroide","alien"]
print (listeEspace[0])

listeEspace[0]="lune"
print (listeEspace[0])

del listeEspace[0]
listeEspace.append("Mars")
for element in listeEspace:#equivalent foreach
    print(element)