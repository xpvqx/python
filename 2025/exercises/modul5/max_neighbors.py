# Skriv en funktion med namnet max_neighbors som tar en lista av tal och returnerar det största värdet man kan få genom att addera två på varandra följande element.

def max_neighbors(lst):
    max_sum = lst[0] + lst[1] # antar största summan är första grannparet
    for i in range(1, len(lst) - 1):    # loopa från index 1 till näst sista
        current_sum = lst[i] + lst[i + 1] #addera i och i+1 (ett grannpar)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
