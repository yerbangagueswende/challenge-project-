import json

class Logic(): 
    def __init__(self):
        pass

    def get_name(self, name: str) -> str:
        with open('names.json') as f:
            data = json.load(f)
        return data[name]
