# ValueError förhindrar programmet att krascha

# Upprepa tills giltigt tal angetts
while True:
    try:
        tal = float(input('Ange ett tal: '))
        print(f'Du angav talet {tal}')
        # Avbryt om inmatning lyckades
        break 
    except ValueError:
        print('Inte ett tal!')
print()
