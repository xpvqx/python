# grundregel: funktionens parameterar tilldelas värden
# som ges av de argument som skickas vid funktionsanropet,
# i den ordning de ges.

def sänkt_pris(ordinarie_pris, prissänkning_procent):
    # beräknar andel som återstår av priset
    # ex 1 - 0.25 = 0.75
    # ordinarie_pris * ... = sänkta priset
    return ordinarie_pris * (1 - prissänkning_procent / 100)

ordinarie_pris = float(input('Varans ordinarie pris: '))
prissänkning_procent = float(input('Prissänkning i procent: '))
nytt_pris = sänkt_pris(ordinarie_pris, prissänkning_procent)

print(f'Det sänkta priset blir {nytt_pris}')
