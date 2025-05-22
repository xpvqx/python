from datetime import date

def dagar_kvar_till_jul():
    idag = date.today()
    return idag

idag = dagar_kvar_till_jul() 
print(f'Idag är det {idag}')
