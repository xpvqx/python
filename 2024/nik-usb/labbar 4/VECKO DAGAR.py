inmatning = input('Skriv in dagar (0-6): ')
hej_list = inmatning.split(' ')
vecko = ['måndag','tisdag','onsdag','torsdag','fredag','lördag','söndag']

for dagens in hej_list:
  
    print(vecko[eval(dagens)])