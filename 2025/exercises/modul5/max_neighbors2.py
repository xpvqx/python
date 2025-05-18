# Funktion ska ta en lista med tal och returnera det största värdet man kan få,
# genom att addera två på varandra följande element (grannpar)

def max_neighbors(lst):
    max_sum = lst[0] + lst[1]
    for i in range(1, len(lst) - 1):
        current_sum = lst[i] + lst[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

print(max_neighbors([9, 4, 13, 7, 8, 5]))           # 20 (17+3)
print(max_neighbors([8, 0, -4, 10, -12, 22, -5]))   # 17 (22 + (-5))

# 1. anta att största summan är det första grannparet (element 0 + 1)
# 2. loopa från första elementet till näst sista element
# 3. på varje steg, addera i och i+1 (ett grannpar)
# 4. om current_sum är större än max_sum som vi skapade tidigare = spara
# 5. returnera max_sum
