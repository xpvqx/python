# Konvertera från Celcius till Fahrenheit
def c2f(temp_c):
    if temp_c < -273.15:
        raise ValueError('Temperatur under abs nollpunkt')
    temp_f = temp_c * 9 / 5 + 32
    return temp_f

# Konvertera från Fahrenheit till Celcius
def f2c(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    if temp_c < -273.15:
        raise ValueError('Temperatur under abs nollpunkt')
    return temp_c

if __name__ == '__main__':
    c = 85
    f = c2f(c)
    c2 = f2c(f)
    print(f'{c} grader Celcius -> {c2} grader Celcius')
