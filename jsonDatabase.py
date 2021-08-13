import json
def write_json(data):
    with open('database.json', 'w') as f:
        json.dump(data, f, indent=4)
def check(id):
    with open('database.json') as f:
        data = json.load(f)
        usersId = str(id)
    if usersId in data['users']:
        return "Already There (≧‿≦ ✿)"
    else:
        data['users'].append(usersId)
        write_json(data)
        return data['users'], "Added (>_<)"

with open('database.json') as f:
    data = json.load(f)
    temp = data['users']
    

    





