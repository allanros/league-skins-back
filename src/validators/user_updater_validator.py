from cerberus import Validator

def user_updater_validator(body: any):
    body_validator = Validator({
        "user": {
            "type": "dict",
            "schema" : {
                "username": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                },
                "hashed_password": {
                    "type": "string"
                }
            }
        }
    })

    response = body_validator.validate(body)
    if response is False:
        raise Exception(body_validator.errors)
