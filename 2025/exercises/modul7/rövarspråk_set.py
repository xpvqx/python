def rövarspråk(ord):
    vokaler = frozenset('aouåeiyäö')
    översättning = ''
    for c in ord:
        if c in vokaler:
            översättning += c
        else:
            översättning += c + 'o' + c
    return översättning

svenskt_ord = input('Skriv ett ord: ')
översatt_ord = rövarspråk(svenskt_ord)
print(f'På rövarspråket blir det {översatt_ord}.')


# funktionen ska översätta givna ördet till rövarspråk
# iterera över strängen ord, kontrollera om var och en av
# bokstäverna finns i mängden vokaler
# alla volaker (aouåeiyäö) i ordet ska läggas till som de är
# i den nya strängen översättning
# alla konsonanter (alla andra bokstäver) ska läggas till
# med dubbelt 'o' emellan
