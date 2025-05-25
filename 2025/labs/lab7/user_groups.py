import json

användardata_fil = input("Fil att läsa användardata från: ")

try:
    with open(användardata_fil, 'r') as f:
        användardata = json.load(f)
    print("Användardata läst från fil.")
except:
    användardata = {}
    print("Ingen användardata tillgänglig.")

grupper_fil = input("Fil att läsa grupper från: ")
try:
    with open(grupper_fil, 'r') as f:
        grupper = json.load(f)
except FileNotFoundError:
    print("Fil saknas")
    exit()
except json.JSONDecodeError:
    print("Felaktigt filformat")
    exit()

print("Grupper:")
for gruppnamn in grupper:
    print(f"* {gruppnamn}")

vald_grupp = input("Välj en grupp: ")
if vald_grupp not in grupper:
    print("Felaktig grupp")
    exit()

for användar_id in grupper[vald_grupp]:
    namn = användardata.get(användar_id, användar_id)
    print(namn)
