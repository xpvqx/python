def hitta_par(lista):
    högsta_par = 0 
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            if lista[i] > högsta_par:
                högsta_par += lista[i]
    return högsta_par

tal = [12, 25, 12, 11, 25, 25, 23, 36, 36]
högsta = hitta_par(tal)
print(högsta)
