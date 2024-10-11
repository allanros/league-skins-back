def body_parser(body: dict) -> dict:
    parsed_body = {
        "data": {
            "champion": body["name"],
            "niceName": body["niceName"],
            "skins": []
        },
        "version": body["version"]
    }

    for value in body["skins"]:
        parsed_body["data"]["skins"].append({
            "skin_id": f"{body['niceName']}_{value['num']}",
            "name": value["name"],
            "image": f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{body['niceName']}_{value['num']}.jpg"
        })

    return parsed_body
