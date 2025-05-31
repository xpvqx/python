# snake_case = små och stora bokstäver, skiljer ord med _
# camelCase = första bokstaven av ett ord är litet, annars börjar med stor

def snake_to_camel(snake):
    dela = snake.split('_')
    camel = dela[0]

    for word in dela[1:]:
        camel += word.capitalize()
    return camel

print(snake_to_camel('nb_light_bulbs'))
