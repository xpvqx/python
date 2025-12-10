# read user ipint
nr_cups = int(input('Number of cups per serving: '))
nr_oz = int(input('Number of ounces per serving: '))
nr_servings = int(input('Number of servings: '))

# calculate total_oz, new_cups, new_oz
total_oz = nr_servings * (nr_cups * 8 + nr_oz)
new_cups = total_oz // 8
new_oz = total_oz % 8

# print converted result
print(f'{new_cups} c {new_oz} oz')
