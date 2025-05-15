# definera vad funktionen ska göra
def avg(a, b):      # function parameters
    return (a + b) / 2

x = int(input('Enter the first number: '))  # argument
y = int(input('Enter the second number: ')) # argument

# resultat:
res = avg(x, y)

print(f'The average number is {res}.')
