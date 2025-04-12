# Read user-input
n = int(input('Enter an even number: '))
# If remainder of integer division is equal to 0 ...
if n % 2 == 0:
    print("The number is even ")
# ... the remainder when dividing an integer by 2 is 1 (no other possibilities)
else:
    print("The number is odd ")
