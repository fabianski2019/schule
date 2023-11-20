NotenListe = [0,0.2,0.26,0.33,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
maxBE = int(input ('Maximale Punktzahl eingeben: '))
UserBE = int(input ('Erziehlte Punktzahl eingeben: '))
Quotient = UserBE/maxBE
Note = -1
for i in range(len(NotenListe)):
    if Quotient >= NotenListe[i]:
        Note += 1
print(Note)

