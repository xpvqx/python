goal = int(input('What is your goal? '))

balance = 0
months = 0

while balance < goal:
    amount = int(input('How much do you want to deposit? '))
    if amount < 0:
        print('No deposits ')
        break
    balance += amount
    months += 1
else:
    print(f'You have reached your goal. It took {months} months. ')
