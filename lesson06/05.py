import json

invalid_json = "{'key':value}"

try:
    data = json.loads(invalid_json)
    print(data)

except json.decoder.JSONDecodeError as e:
    print(f"Exception occured: {e}")