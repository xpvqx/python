from datetime import date

def dagar_kvar_till_jul(datum=None):
    idag = date.today()
    julafton = date(2025, 12, 24)

    # Om inget datum anges ska funktionen räkna från idag
    if datum is None:
        datum = idag
    # Error: datumet har redan inträffat
    if datum < idag:
       raise ValueError('Datumet har redan inträffat')
    # Error: Om datumet infaller efter julafton i år
    if datum > julafton:
       raise ValueError('Datumet infaller efter julafton')
    # Returnera hur många dagar är kvar till jul
    return(julafton - datum).days

print(f'{date.today()}: {dagar_kvar_till_jul()}')
