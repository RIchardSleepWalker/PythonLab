import requests

def pobierz_cene_euro():
    url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json"
    response = requests.get(url)
    response.raise_for_status()

    dane = response.json()
    return dane["rates"][0]["mid"]

print(pobierz_cene_euro())