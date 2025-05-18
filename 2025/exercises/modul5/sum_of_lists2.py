def sum_of_index(value1, value2):
    addition = []
    for i in range(len(value1)):
        addition.append(value1[i] + value2[i])
    return addition

lst1 = [1, 1, 2, 2, 3, 3]
lst2 = [0, 1, 2, 3, 4, 5]
sum = sum_of_index(lst1, lst2)
print(sum)                           # [1, 2, 4, 5, 7, 8]

L1 = [1, 1, 1, 4, 4]
L2 = [3, 5, 6, 0, -1]
total = sum_of_index(L1, L2)
print(total)                           # [4, 6, 7, 4, 3]
