# write a function that multiplies all values in a list
# if no value is given, multiply by 2
def multiply(lst, multiplier=2):
    result = []
    for i in range(len(lst)):
        result.append(lst[i] * multiplier)
    return result

values = [1, 3, 2, 1, 4, 0]
res1 = multiply(values, 8)
print(res1)

numbers = [9, 2, 12, 4, -2]
res2 = multiply(numbers)
print(res2)
