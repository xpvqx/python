print('Välkommen ')
längd = int(input('Hur lång är du? '))
har_vuxen_med = input('Hur du mamma eller pappa med dig? ')
if längd >= 130 or (längd >= 110 and har_vuxen_med == "ja"):
    print('Du vår åka ')
else:
    print('Du får inte åka ')