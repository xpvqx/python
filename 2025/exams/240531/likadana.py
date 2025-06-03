def hitta_sekvens(lista):
    max_längd = 1
    nuvarande_längd = 1
    resultat = lista[0]

    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1]:
            nuvarande_längd += 1
            if nuvarande_längd > max_längd:
                max_längd = nuvarande_längd
                resultat = lista[i]
        else:
            nuvarande_längd = 1

    return resultat

if __name__ == '__main__':
    tal = [12, 25, 12, 11, 25, 25, 23, 36, 10]
    print(hitta_sekvens(tal)) # 25
