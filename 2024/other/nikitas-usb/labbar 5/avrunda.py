def round_list(numbers):
    for i in range(len(numbers)):
        numbers[i] = round(numbers[i], 2)
    return numbers
values = [45.0523, 88.31467, 0.3263, 67.3, 783.00321, 5]
print(round_list(values))
