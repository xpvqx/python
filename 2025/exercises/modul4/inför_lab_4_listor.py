number = input('Skriv in dagar 0-6 ').split()
lst = ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag', 'lördag', 'söndag']
numbers2 = [int(x) for x in number]

for item in numbers2:
    print(lst[item])
