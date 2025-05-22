from datetime import date, timedelta

# ta en lista med dygnsmedeltemperaturer
# börja med 15 februari 2024
# returnera datum får vårens ankomst
def spring_start_date(temperatures):
    # kollar om 7 temperaturer har angetts
    if len(temperatures) < 7:
        raise ValueError('Minst sju dygnsmedeltemperaturer behövs')
    # start datum och sista tillåtet datum
    start_date = date(2025, 2, 15)
    last_allowed = date(2025, 7, 31)
    
    for i in range(len(temperatures) - 6):
        # tar sju dagar i rad, börjar på position i
        seven_days = temperatures[i:i+7]
        # kolla om alla 7 dagar är varmare än 0.0C, om ja har vi hittat vårens start
        if all (temp > 0.0 for temp in seven_days):
            # räkna ut vilket datum den första av dessa 7 dagar är, genom att lägga till i till startdatumet
            spring_date = start_date + timedelta(days=i)
            # om spring_date är efter 31 juli -> ogiligt (ERROR)
            if spring_date > last_allowed:
                raise ValueError('Vårens ankomst kan inte vara senare än 31 juli')
            # returnera vårens datum
            return spring_date
    # om loopen aldrig hittar 7 varma dagar i rad = inget vårdatum ännu
    raise ValueError('Våren är inte här än')
