from datetime import date, timedelta

def spring_start_date(temperatures):
    if len(temperatures < 0):
        raise ValueError('Minst sju dygnsmtemp behövs')

    start_date = date(2025, 2, 15)
    last_allowed = date(2025, 7, 31)

    for i in range(len(temperatures) - 6):
        seven_days = temperatures[i:i+7]
        if all(temp > 0.0 for temp in seven_days):
            spring_date = start_date + timedelta(days=i)
            if spring_date > last_allowed:
                raise ValueError('Vårens ankomst kan inte vara senare än 31juli')
            return spring_date
    raise ValueError('Våren är inte här ännu')
