# ta en lista av värden som input
# hitta högsta paret med likadana värden som ligger intill varandra
# returnera det upprepade talet

def hitta_par(lista):
    högsta_par = 0
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            if lista[i] > högsta_par:
                högsta_par = lista[i]
    return högsta_par

if __name__ == '__Main__':
    tal = [12, 25, 12, 11, 25, 25, 23, 100, 100] 
    print(hitta_par(tal))
