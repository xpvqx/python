#konvertera celsius till fahrenheit
def c2f(temp_c):
    temp_f = temp_c * 9 / 5 + 32
    return temp_f


#konvertera fahrenheit till celsius
def f2c(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c

if __name__ == '__main__':
    c = 85
    f = c2f(c)
    c2 = f2c(f)
    print(f'{c} grader Celsius -> {c2} grader Celsius')