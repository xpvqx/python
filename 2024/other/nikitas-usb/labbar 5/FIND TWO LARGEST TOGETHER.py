def max_neighbors(lst):
   
    max_sum = lst[0] + lst[1]
    

    for i in range(1, len(lst) - 1):
        current_sum = lst[i] + lst[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum


print(max_neighbors([9, 4, 13, 7, 8, 5])) 
print(max_neighbors([8, 0, -4, 10, -12, 22, -5])) 