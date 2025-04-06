def cheapest_3h(numbers):
    max_sum = float('-inf')  # Sätt max_sum till ett mycket litet värde i början
    
    for i in range(len(numbers) - 1):
        pair_sum = numbers[i] + numbers[i + 1]
        if pair_sum > max_sum:
            max_sum = pair_sum
    
    return max_sum