# 1 c = 8 oz

# läs in antal cups per portion
# läs in ounces per portion
# läs in antal portioner

cups = int(input('Number of cups (per serving): '))
ounces = int(input('Number of  ounces (per serving): '))
servings = int(input('Number of servings: '))

# räkna ut antalet cups och ounces för antal givna portioner

# konvertera alla cups till ounces, addera extra ounces
# multiplicera med antal portioner = ger totala mängden oz
total_ounces = servings * (cups * 8 + ounces)

# // = heltalsdivision - hur många koppar det blir totalt
new_cups = total_ounces // 8

# % = resten av heltalsdivision - hur många oz blir över efter
# man har tagit ut alla hela koppar
new_ounces = total_ounces % 8

print(f'{new_cups} c {new_ounces} oz')
