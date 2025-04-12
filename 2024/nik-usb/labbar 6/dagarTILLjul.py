import datetime

def dagar_kvar_till_jul(datum):
    idag = datetime.date.today()
    jul = datetime.date(idag.year, 12, 24) 
    
    try:
        datum2 = datetime.date(int(datum[0]),int(datum[1]),int(datum[2]))
    except:
        datum2 = datetime.date.today()
    
    if idag > datum2:
        raise ValueError("datumet har redan inträffat!")
    
    if datum2 > jul:
        raise ValueError("datumet är efter jul!")
    
    datum3 = (jul - datum2).days
    
    return datum3
    

if __name__ == "__main__":
    egetdatum = input("skriv ett datum, [år månad dag]: ").split()
    egetdatum2 = dagar_kvar_till_jul(egetdatum)
    if egetdatum2 > 1:
        print(f'det är {egetdatum2} dagar kvar')
    else:
        print(f'det är {egetdatum2} dag kvar')