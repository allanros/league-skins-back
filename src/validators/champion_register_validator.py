from cerberus import Validator

def champion_register_validator(body: dict) -> None:
    validator_body = Validator({
        "data": {
            "type": "dict",
            "required": True,
            "schema": {
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
                                "type": "string",
                                "required": True
                            },
                            "name": {
                                "type": "string",
                                "required": True
                            },
                            "image": {
                                "type": "string",
                                "required": True
                            }
                        }
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
