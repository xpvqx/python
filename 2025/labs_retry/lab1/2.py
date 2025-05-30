# 1 cup = 8 oz
# räkna ut antal cups of ounces för givna antalet portioner

cups = int(input('How many cups? (per serving): '))
ounces = int(input('How many ounces? (per serving): '))
servings = int(input('How many servings?: '))

# konvertera alla cups till ounces
total_ounces = servings * (cups * 8 + ounces)

new_cups = total_ounces // 8
new_ounces = total_ounces % 8

print(f'{new_cups} c {new_ounces} oz')
