# Läs in ett positivt heltal från användaren
tal = int(input('Ange ett positivt heltal: '))

# Ange om talet är jämnt eller udda.
if tal % 2 == 0:
        print('Talet är jämnt')
# Om talet är negativt ska användaren istället upplysas om detta.
else:
    print('Talet är udda!')