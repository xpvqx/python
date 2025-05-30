def snake_to_camel(snake):
    dela = snake.split('_')
    camel = dela[0]
    for word in dela[1:]:
        camel += word.capitalize()
    return camel 

snake = input('Skriv in ett ord med camel_case: ')
print(snake_to_camel(snake))
