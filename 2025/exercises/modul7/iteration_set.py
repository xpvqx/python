# Vi itererar över ett set eller ett frozenset på precis
# samma sätt som en str, en tuple eller en list.
# Notera dock att eftersom elementen i ett set inte är ordnade, så kan vi inte använda for i in range-versionen.
# Använd iteration för att skriva ut elever som är frånvarande, respektive som har ogiltig frånvaro (varken ledig eller sjuk).

elever = {'Ali', 'Bo', 'Carl', 'David', 'Emma', 'Frida'}
närvarande = {'Carl', 'David'}
ledig = {'Ali', 'Emma'}
sjuk = {'Frida'}

frånvarande = elever - närvarande
for elev in frånvarande:
    print(elev)

ogiltig_frånvaro = frånvarande - (ledig | sjuk)
for elev in ogiltig_frånvaro:
    print(elev)
