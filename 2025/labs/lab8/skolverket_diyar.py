import requests

def hitta_kommunkod(kommunnamn):
    url = "https://api.skolverket.se/skolenhetsregistret/v1/kommun"
    r = requests.get(url)
    data = r.json()
    kommuner = data["Kommuner"]
    for k in kommuner:
        if k["Namn"].lower() == kommunnamn.lower():
            return k["Kommunkod"]
    raise ValueError("Felaktigt kommunnamn.")

def hitta_skolor(kommunkod):
    url = "https://api.skolverket.se/skolenhetsregistret/v1/skolenhet"
    r = requests.get(url)
    data = r.json()
    skolor = data["Skolenheter"]
    namn_lista = []
    for skola in skolor:
        if skola["Kommunkod"] == kommunkod:
            namn_lista.append(skola["Skolenhetsnamn"])
    return namn_lista

if __name__ == "__main__":
    kommun = input("Ange kommun: ")
    try:
        kod = hitta_kommunkod(kommun)
        skolor = hitta_skolor(kod)
        for namn in skolor:
            print(namn)
    except:
        print("Felaktigt kommunnamn.")
