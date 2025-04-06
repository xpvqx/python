dat = input("Skriv in en serie datum: ").split()

månader = ["januari","februari","mars","april","maj","juni","juli","augusti","september","oktober","november","december"]
#Jan = 0. feb = 1. mars = 2. april = 3. maj = 4. juni = 5. juli = 6. augusti = 7. 
# september = 8. oktober = 9. november = 10. december = 11.

#input xxxxxx total är 6 siffror, första två är år, andra två är månad, sista två är dag!

for i in dat:
    fdag = int(i[4:6])
    cmånad = int(i[2:4]) - 1
    fmånad = månader[cmånad]
    år = "20" + i[0:2]
    print(fdag,fmånad,år)