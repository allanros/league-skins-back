import requests

def get_champion_skins(champion_name: str, version: str) -> dict:
    url_skin = (f"https://ddragon.leagueoflegends.com/cdn/{version}"
                f"/data/pt_BR/champion/{champion_name}.json")
    champion_skin_data = requests.get(url_skin, timeout=5).json()["data"]

    response = {
        "data": {
            "champion": champion_skin_data[champion_name]["name"],
            "niceName": champion_name,
            "skins": []
        },
        "version": version
    }

    for skin in champion_skin_data[champion_name]["skins"]:
        response["data"]["skins"].append(
            {
                "skin_id": f"{champion_name}_{skin['num']}",
                "name": skin["name"],
                "image": (f"https://ddragon.leagueoflegends.com/cdn/img/champion"
                          f"/loading/{champion_name}_{skin['num']}.jpg")
            }
        )

    return response

# print(get_champion_skins("Anivia", "14.20.1"))
