def snake_to_camel(snake):
    dela = snake.split('_')
    camel = dela[0]

    for word in dela[1:]:
        camel += word.capitalize()
    return camel

test = input('Skriv in ett ord med snake_case: ')
converted = snake_to_camel(test)
print(converted)
