#Tar 3 timmar att köra ett program, minsta värdet att börja i listan och tre värden framåt
def cheapest_3h(elec):
     
    
    biggie = 100000000000

    for i in range(0, len(elec) - 2):
          
            
            
            nuvarande = elec[i] + elec[i + 1] + elec[i + 2]
            if nuvarande < biggie:
                biggie = nuvarande
                timme = i
    #print (biggie)            
    #print (timme)
    return timme

print(cheapest_3h([143, 167, 124, 112, 96, 102, 129, 190]))
print(cheapest_3h([142, 295, 226, 299, 194, 107, 139]))
print(cheapest_3h([128.33, 285.05, 92.6, 288.16, 211.68, 32.33]))
