from datetime import date, timedelta

def spring_start_date(temperature):
    if len(temperature) < 7:
        raise ValueError('Minst sju dygnsmedeltemperaturer behövs')

    start_date = date(2025, 2, 15)
    end_date = date(2025, 7, 31)

    for i in range(len(temperature) - 6):
        seven_days = temperature[i:i+7]
        if all (temp > 0.0 for temp in seven_days):
            spring_date = start_date + timedelta(days=i)
            if spring_date > end_date:
                raise ValueError('Vårens ankomst kan inte\
                        vara senare än 31 juli')
            return spring_date
    raise ValueError('Våren är inte här än')
