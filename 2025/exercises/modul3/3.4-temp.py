t = float(input('Temp? '))
if t < 18:
    print('Det är kallt')
    print('Sätt på värmen')
    if t < 12:
        print('Sätt på jackan!')
        if t < 6:
            print('Det är svinkalt!')
else:
    print('Det är varmt')
    if t > 22:
        print('Stäng av värmen!')
        if t > 26:
            print('Det är svinvarmt!')

print(f'Det är {t:.1f} grader.')
