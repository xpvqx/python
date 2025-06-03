def hitta_par(lista):
    if len(lista) < 2:
        raise ValueError('Listan är mindre än 2')

    högst_par = 0

    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            if lista[i] > högst_par:
                högst_par += lista[i]
    return högst_par

tal = [12, 25, 12, 11, 251, 251, 23, 37, 37]
print(hitta_par(tal)) # 25
