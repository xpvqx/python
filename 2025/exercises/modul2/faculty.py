# ask user for a number, turn into integer
n = int(input("n: "))

# faculty = 1 * 2 * 3 * 4 * ... n, repeated multiplication
# if n_faculty = 0, result will = 0 always
# create variable to store result
n_faculty = 1

# multiply integers from 1 to n
# if n + 1 is not specified - range begins with 0 to n - 1
for i in range(1, n + 1):       
    n_faculty *= i              # multiply with 1,2,3, ...n
    print(n_faculty)
# print result
print('n!:', n_faculty)
