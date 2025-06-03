import json
import sys

def main():
    filename = input("Läs lagerstatus från fil: ")

    # Läs in lagret från filen
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lager = json.load(f)
    except FileNotFoundError:
        print("Fil saknas")
        sys.exit()

    # Läs in varor att lägga till
    nya_varor_str = input("Lägg till: ")
    nya_varor = nya_varor_str.split()

    # Uppdatera lagret
    for vara in nya_varor:
        if vara in lager:
            lager[vara] += 1
        else:
            lager[vara] = 1

    # Beräkna totalt antal varor
    totalt = sum(lager.values())
    print(f"Totalt antal varor: {totalt}")

    # Skriv tillbaka till fil
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(lager, f, ensure_ascii=False)

if __name__ == "__main__":
    main()
