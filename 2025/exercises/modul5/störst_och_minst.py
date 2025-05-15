def störst_och_minst(lst):
    störst = max(lst)
    minst = min(lst)
    return(störst, minst)

en_lista = [4, 3, 7, 9, 5, 8]
resultat = störst_och_minst(en_lista)

print(resultat)
