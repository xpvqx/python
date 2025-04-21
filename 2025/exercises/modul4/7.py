user_data = input('Ange värden: ').split() # 7 3 -5 0 2 -1 8 -3
positiva = []
user_data = [int(x) for x in user_data]     # list comprehension

for i in range(len(user_data)):
    if user_data[i] >= 0:
        positiva.append(user_data[i])
print(positiva)                             # [7, 3, 0, 2, 8]
