from cerberus import Validator

def user_add_skin_validator(body: dict) -> None:
    body_validator = Validator({
        "skin": {
            "type": "string",
            "required": True
        }
    })

    response = body_validator.validate(body)
    if not response:
        raise Exception(body_validator.errors)
