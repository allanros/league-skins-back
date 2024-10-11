import requests

def get_version_comparision(version_on_cache: str = "") -> dict:
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    last_version = requests.get(url, timeout=5).json()[0]

    if last_version != version_on_cache:
        return {
            "status": False,
            "last_version": last_version
        }

    return {
        "status": True,
        "last_version": last_version
    }
