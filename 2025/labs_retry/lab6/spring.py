from season_tools import spring_start_date

def main():
    try:
        user_input = input('Ange dygnsmedeltemperatur: ')
        temperatures = [float(temp) for temp in user_input.split()]
        spring_date = spring_start_date(temperatures)
        return spring_date
    except ValueError as e:
        return e
