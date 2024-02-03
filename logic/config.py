import json

class config():
    def __init__(self):
        pass

    def get_name(self, name: str):
        with open('names.json') as f:
            data = json.load(f)
        return data[name]
    
    def get_names(self):
        with open('names.json') as f:
            data = json.load(f)
        return data.values()

    def get_names_sorted(self):
        with open('names.json') as f:
            data = json.load(f)
        return sorted(data.keys())
    
    def get_names_sorted_by_length():
        with open('names.json') as f:
            data = json.load(f)
        return sorted(data.values(), key=len)

    def get_names_sorted_by_length_desc():
        with open('names.json') as f:
            data = json.load(f)
        return sorted(data.values(), key=len, reverse=True)
     
    def reverse_names(self):
        with open('names.json') as f:
            data = json.load(f)
        return data.values()[::-1]
    
    def get_names_sorted_by_length_desc_and_reverse():
        with open('names.json') as f:
            data = json.load(f)
        return sorted(data.values(), key=len, reverse=True)[::-1]
