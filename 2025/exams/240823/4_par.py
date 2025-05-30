# ta en lista av värden som input
# hitta det högsta paret av likadana värden som ligger intill varandra i listan

def hitta_par(lista):
    högsta_par = 0
    for i in range(len(lista) - 1):
        if lista[i] == lista[i+1]:
            if lista[i] > högsta_par:
                högsta_par = lista[i]
    return högsta_par

lista = [12, 25, 12, 11, 25, 25, 23, 36, 10]
par = hitta_par(lista)
print(par)
