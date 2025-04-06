print('Välkommen: ')
längd = int(input('Hur lång är du? '))

if längd >= 130:
    print('Du får åka ') 
elif längd >= 110:
    har_du_vuxen_med_dig = input('Har du vuxen med dig? ') 
    if har_du_vuxen_med_dig == "ja":
        print('Du får åka!')
    else:
        print('Du får inte åka! ')