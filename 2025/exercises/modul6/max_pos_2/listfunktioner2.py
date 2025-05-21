# skapa en def hitta positionen för listans största element
def arg_max(lst):
    # anta att max_pos = 0
    max_pos = 0
    # iterera över alla element i listan
    for i in range(len(lst)):
        # om index i listan är större än ...
        if lst[i] > lst[max_pos]:
            max_pos = i
    return max_pos

if __name__ == '__main__':
    my_list = [3, 7, -2, -8, 6]
    my_max = arg_max(my_list)
    print(my_max)
