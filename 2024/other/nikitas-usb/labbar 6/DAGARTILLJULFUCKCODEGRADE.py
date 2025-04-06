import datetime

def dagar_kvar_till_jul(datum=None):
    idag = datetime.date.today()
    jul = datetime.date(2024, 12, 24) 
    if datum is None:
        datum = idag

    
    try:
        if isinstance(datum, datetime.date or datetime.date.today()):
            datum2 = datum
        else:
            datum2 = idag
    
    except:
        datum2 = idag
    
    if idag > datum2:
        raise ValueError("datumet har redan inträffat!")
    
    if datum2 > jul:
        raise ValueError("datumet är efter jul!")
    
    datum3 = (jul - datum2).days
    
    return datum3