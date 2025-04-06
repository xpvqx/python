def c2f(temp_c):
    if temp_c < -273.15:
        raise ValueError('temperatur under absoluta nollpunkten. ')
    temp_f = temp_c * 5 / 9 + 32
    return temp_f

#konvertera från fahrenheit till celsius
def f2c(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    if temp_c < -273.15:
        raise ValueError('Tempature under absouluta ooga booga punkten. ')
    return temp_c

if __name__ == '__main__':
    c = 85 
    f = c2f(c)
    c2 = f2c(f)
    print (f'{c} grader Celsius -> {c2} grader Celsius')

