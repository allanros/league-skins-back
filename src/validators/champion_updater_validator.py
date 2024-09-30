from cerberus import Validator

def champion_updater_validator(body: dict) -> None:
    validator_body = Validator({
        "champion": {
            "type": "string",
            "required": True
        },
        "skins": {
            "type": "list",
            "required": True,
            "schema": {
                "type": "dict",
                "required": True,
                "schema": {
                    "skin_id": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "image": {
                        "type": "string"
                    }
                }
            }
        },
        "version": {
            "type": "string",
            "required": True
        }
    })

    response = validator_body.validate(body)
    if not response:
        raise Exception(validator_body.errors)
