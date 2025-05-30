# convertera snake_case till camelCase

# snake_case = allt är små bokstäver, ord skiljs åt av _
# camelCase = alla ord skrips ihop
# - allt ord förutom det första börjar med stor bokstav

def snake_to_camel(snake):
    delar = snake.split('_')
    camel = delar[0] # första ordet behåller små bokstäver
    for word in delar[1:]:
        camel += word.capitalize()
    return camel

if __name__ == '__main__':
    snake = input('Skriv in ett variabelnamn i snake_case: ')
    print(snake_to_camel(snake))
