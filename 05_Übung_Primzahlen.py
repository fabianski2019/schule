prim = int(input("Bitte Zahl eingeben: "))
nonprim_list = []
for n in range(2, prim):
    if prim % n == 0:
        nonprim_list.append(n)
        print(prim, "ist durch", nonprim_list , "teilbar, also ist sie keine Primzahl.")
    elif nonprim_list == []:
        print(prim, "ist eine Primzahl.")