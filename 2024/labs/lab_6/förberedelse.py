import datetime

def dagar_kvar_till_jul(datum=None):
    jul = datetime.date(2024, 12, 24)
    idag = datetime.date.today()


    if datum is None:
        skillnad = abs(idag - jul)

    elif datum < idag:
        raise ValueError("Datumet har redan inträffat")

    elif datum <= jul:
        skillnad = (jul - datum)

    else:
        raise ValueError("Datumet infaller efter julafton")

    return skillnad.days