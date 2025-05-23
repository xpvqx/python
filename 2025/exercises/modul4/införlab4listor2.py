lst = ['mån', 'tis', 'ons', 'tors', 'fre', 'lör', 'sön']
user_input = input('Skriv in ett nummer 0-6 ')
user_input2 = [int(x) for x in user_input]

for item in user_input2:
    print(lst[item])
print()
