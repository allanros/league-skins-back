import requests

def get_champions_from_riot_api(version: str) -> dict:
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/pt_BR/champion.json"
    champions_response = requests.get(url, timeout=5).json().get("data")

    champion_names = []

    for key, values in champions_response.items(): # pylint: disable=unused-variable
        champion_names.append(key)

    return champion_names
