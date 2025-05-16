def med_eftertryck(ordet):
    res = ''
    for i in range(len(ordet)):
        res += ordet[i] + '*'
    return res

ett_ord = 'kanon'
nytt_ord = med_eftertryck(ett_ord) #k*a*n*o*n
print(nytt_ord)

annat_ord = 'perfekt'
nyare_ord = med_eftertryck(annat_ord) #p*e*r*f*e*k*t
print(nyare_ord)
