from datetime import date

def dagar_kvar_till_jul(datum=None):
    idag = date.today()
    julafton = date(2025, 12, 24)

    if datum is None:
        datum = idag
    if datum < idag:
        raise ValueError('Datumet har redan inträffat')
    if datum > julafton:
        raise ValueError('Datumet infaller efter julafton')
    return(julafton - datum).days


# tests =)
if __name__ == '__main__':

    print(f'Dagens datum är {date.today()}. Det är {dagar_kvar_till_jul()} dagar kvar till jul.')

    print(f'Om datumet är 2025-12-2, är det {dagar_kvar_till_jul(date(2025, 12, 2))} dagar kvar till jul.')
