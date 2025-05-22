from season_tools import spring_start_date

def main():
    try:
        user_input = input('Ange dygnsmedelstemperaturer: ')
        temperatures = [float(temp) for temp in user_input.split()]
        spring_date = spring_start_date(temperatures)
        print(f'Vårens ankomst: {spring_date}')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
