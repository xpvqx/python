# Assert används för att avbryta programkörning, ge felmeddelanden

def division(täljare, nämnare):
    assert nämnare != 0, "Kan ej dividera med 0"
    return täljare / nämnare

täljare = int(input('Ange täljare: '))
nämnare = int(input('Ange nämnare: '))
res = division(täljare, nämnare)
print(res)
