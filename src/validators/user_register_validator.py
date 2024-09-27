from cerberus import Validator

def user_register_validator(body: any):
    body_validator = Validator({
        "user": {
            "type": "dict",
            "schema" : {
                "username": {
                    "type": "string",
                    "required": True
                },
                "email": {
                    "type": "string",
                    "required": True
                },
                "hashed_password": {
                    "type": "string",
                    "required": True
                }
            }
        }
    })

    response = body_validator.validate(body)
    if response is False:
        raise Exception(body_validator.errors)
