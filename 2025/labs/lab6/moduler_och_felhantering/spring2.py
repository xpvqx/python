from season_tools2 import spring_start_date

def main():
    try:
        user_input = input('Ange dygnsmedeltemperaturer: ')
        # list comprehension
        temperatures = [float(temp) for temp in user_input.split()]
        # räkna ut vårens ankomst
        spring_date = spring_start_date(temperatures)
        # returnera svaret
        return spring_date
    # fel meddelande
    except ValueError as e:
        return e
