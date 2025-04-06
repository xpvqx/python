import datetime

def dagar_kvar_till_jul(datum):
    idag = datetime.date.today()
    jul = datetime.date(2024, 12, 24) 
    

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


#tester!!
egetdatum = input("skriv ett datum, [år månad dag]: ")
egetdatumlit = egetdatum.split()
try:
    datum5 = datetime.date(int(egetdatumlit[0]),int(egetdatumlit[1]),int(egetdatumlit[2]))
except:
    try:
        datum5 = int(egetdatum)
    except:
        datum5 = egetdatum
egetdatum2 = dagar_kvar_till_jul(datum5)
print(egetdatum2)
print(dagar_kvar_till_jul(datetime.date.today()))