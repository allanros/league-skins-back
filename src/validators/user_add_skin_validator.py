from cerberus import Validator

def user_add_skin_validator(body: dict) -> None:
    body_validator = Validator({
        "skins": {
            "type": "list",
            "required": True
        }
    })

    response = body_validator.validate(body)
    if not response:
        raise Exception("Invalid body")
