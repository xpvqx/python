def scrabble(ord):
    # bokstäverna q och w ska inte vara med!
    bokstäver = 'abcdefghijklmnoprstuvxyzåäö'  

    poäng = [
            1, 4, 8, 1, 1, 3, 2, 2, 1,
            7, 2, 1, 2, 1, 2, 4, 1, 1,
            1, 4, 3, 8, 7, 10, 4, 3, 3
            ]

    poängtabell = dict(zip(bokstäver, poäng))
    total = 0
    # för varje bokstav i ordet:
    for bokstav in ord:
        if bokstav in poängtabell:
            # lägg till bokstavpoängen
            total += poängtabell[bokstav]
        else:
            print(f"Varning: '{bokstav}' finns inte i poängtabellen och ger 0 poäng")
    return total

användarord = input('Skriv ett ord: ')
ordpoäng = scrabble(användarord)
print(f'Din ordpoäng är {ordpoäng}.')
