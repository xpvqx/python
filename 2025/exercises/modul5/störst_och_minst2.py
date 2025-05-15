# definera funktionen
def largest_smallest(lst):
    largest = max(lst)
    smallest = min(lst)
    return (largest, smallest)

a_list = [4, 9, 1, 7, 5]
res = largest_smallest(a_list)
print(res)
