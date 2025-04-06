# Läs in totalvikt
total = int(input('Ange max vikt i kg: '))

vikt = 0
count = 0           # Vi behöver en räknare till while-satsen

while vikt <= total:
    vikt2 = int(input('Ange paketets vikt: '))          # Läs in vikt av paketet
    vikt += vikt2                                       # Lägg till paketets vikt till den totala vikten
    count += 1                                          # Ökna räknaren för antalet paket

# Bryt loopen on vikten överstiger total vikten
    if vikt >= total:
        print(f'Du kan bara lasta {count -1} paket. Totalvikten är {vikt - vikt2} kg')
        break
