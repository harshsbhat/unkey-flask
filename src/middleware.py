from flask import request, jsonify
import requests
import os


def verify_key(api_id, key, permission):
    url = "https://api.unkey.dev/v1/keys.verifyKey"

    payload = {
        "apiId": api_id,
        "key": key,
        "authorization": {"permissions": permission}
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.json())
    return response.json()

def with_auth(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            api_key = request.headers.get("Authorization")
            if not api_key:
                return jsonify({"message": "Unauthorized"}), 401

            key = api_key.split(" ")[1] if " " in api_key else api_key

            result = verify_key(os.environ.get("UNKEY_API_ID"), key, permission)
            print(result)
            if not result.get("valid"):
                return jsonify({"message": "Forbidden"}), 403

            return func(*args, **kwargs)

        wrapper.__name__ = func.__name__  
        return wrapper
    return decorator
