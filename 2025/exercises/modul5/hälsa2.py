def welcome(name):
    if name == '':
        return
    print(f'Welcome {name}!')

question = input('What is your name? ')
greet = welcome(question)
