# Läs in tal, skapa en lista som består av alla icke-negativa tal

user_data = input('Enter values ')
datalist = [float(x) for x in user_data.split()]

positives = []

for item in datalist:
    if item >= 0:
        positives.append(item)
print(positives)
