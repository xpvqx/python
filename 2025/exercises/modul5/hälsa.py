def hälsa_välkommen(namn):
    if namn == '':
        return
    else:
        return(namn)

user_input = input('Vad heter du?: ')
greet = hälsa_välkommen(user_input)
print('Välkommen', greet)
print()
