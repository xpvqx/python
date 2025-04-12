def arg_max(lst):
    max_pos = 0
    for i in range(len(lst)):
        if lst[i] > lst[max_pos]:
            max_pos = i
    return max_pos

if __name__=='__main__': #ger en lista om det är huvud koden alltså denna som kör koden!
    my_list = [-9,-7,-2,-8,-6]
    my_max = arg_max(my_list)
    print(my_max)
