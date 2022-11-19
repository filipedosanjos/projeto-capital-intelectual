import json

def carregar():
    with open("data.json") as data:
        return json.load(data)

def salvar(new_data):
    current_data = carregar()
    current_data.append(new_data)

    with open("data.json", "w") as data:
        json.dump(current_data, data) 
    
