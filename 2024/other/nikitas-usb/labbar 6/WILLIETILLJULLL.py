import datetime
def dagar_kvar_till_jul(datum=None):
    idag = datetime.date.today()
    jul = datetime.date(2024, 12, 24)

    if datum is None:
        datum = idag
    try:
        

    if datum >= jul: #KAN BARA SKRIVA JUL!
        raise ValueError("Datumet har redan inträffat")
    else:
        tills_jul = jul - datum
        if tills_jul < datetime.timedelta(days=0):
            raise ValueError("Datumet inträffar efter julafton i år.")
        else:
            pass
    return tills_jul
        
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