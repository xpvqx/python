from datetime import date

def dagar_kvar_till_jul(datum=None):
    idag = date.today()
    julafton = date(2025, 12, 24)

    if datum is None:
        datum = idag
    if datum > idag:
        raise ValueError('Datumet har redan inträffat')
    if datum > julafton:
        raise ValueError('Datumet är efter jul')
    return (julafton - datum).days
