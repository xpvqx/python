import requests


def hitta_kommunkod(kommun_namn):
    url = f"https://api.skolverket.se/skolenhetsregistret/v1/kommun"
    response = requests.get(url)
    response.raise_for_status()
    content = response.json()
    kommuner = content["Kommuner"]
    for kommun in kommuner:
        namn = kommun["Namn"]
        kod = kommun["Kommunkod"]
        if kommun_namn == namn:
            return str(kod)
    raise ValueError

def hitta_skolor(kommunnr):
    url = f"https://api.skolverket.se/skolenhetsregistret/v1/kommun/{kommunnr}"
    response = requests.get(url)
    response.raise_for_status()
    content = response.json()
    skolenheter = content["Skolenheter"]
    skolor = []
    for enhet in skolenheter:
        skola = enhet["Skolenhetsnamn"]
        skolor.append(skola)
    return skolor



if __name__ == "__main__":
    ange_kommun = input("Ange kommun: ")
    try:
        kommun_kod = hitta_kommunkod(ange_kommun)
    except ValueError:
        print("Felaktigt kommunnamn.")
        exit()
    skolor = hitta_skolor(kommun_kod)
    for skola in skolor:
        print(f'{skola}')
