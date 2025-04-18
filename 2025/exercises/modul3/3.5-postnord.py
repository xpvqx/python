# Stora och små brev får vara: 

# Maximimått: längd 600 mm, tjocklek 100 mm, bred+längd+tjocklek högst 900 mm
# Minimått: längd 140 mm, bredd 90 mm

# Läs in brevets längd, bredd och tjocklek - är brevet tillåtet?

length = int(input('Brevets längd: '))
width = int(input('Brevets bredd: '))
thickness = int(input('Brevets tjocklet: '))

if (length <= 600 and thickness <= 100) and \
        (width + length + thickness <= 900) and \
        (length >= 140 and width >= 90):
            print('Brevet tillåts.')
else:
    print('Brevet tillåts inte.')
