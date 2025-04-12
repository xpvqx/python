inmatning = input('Skriv in dagar (0-6): ').split()
vecko = ['måndag','tisdag','onsdag','torsdag','fredag','lördag','söndag']

for dagens in inmatning:
  
    print(vecko[eval(dagens)])