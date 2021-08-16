import json
def write_json(data):
    with open('database.json', 'w') as f:
        json.dump(data, f, indent=4)

def check(id):
    with open('database.json') as f:
        data = json.load(f)
        usersId = str(id)
        tempData = []
        for i in data['users']:
            tempData.append(i['_id'])
    if usersId in tempData:
        return "Already There (≧‿≦ ✿)"
    else:
        data['users'].append({"_id": usersId})
        write_json(data)
        return data['users'], "Added (>_<)"

def idIndexFinder(id):
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        userId = []
        for i in temp:
            userId.append(i['_id'])
        if str(id) in userId:
            for i, dic in enumerate(temp):
                if dic['_id'] == str(id):
                    realId = i
            return realId

def inserting(id, name=None, value=None):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        if name != None:
            tempData[name] = value
            write_json(data)

def getDataValue(id, name):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        if name in tempData:
            print(tempData[name])
        else:
            print(None)
inserting(288623940404772865, 'power', '1')
getDataValue(288623940404772865, 'power')
    





