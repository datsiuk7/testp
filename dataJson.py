import json

def get_dataJson():
    with open("dataId.json", "r") as f:
        loaded_data = json.load(f)
        # print(loaded_data)
    return loaded_data

def set_dataJson(data):
    with open("dataId.json", "w") as f:
        json.dump(data, f)

