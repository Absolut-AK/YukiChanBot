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
        print("Already There (≧‿≦ ✿)")
    else:
        data['users'].append({"_id": usersId})
        write_json(data)
        print(data['users'], "Added (>_<)")

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
            return tempData[name]
        elif name not in tempData:
            return None
            
def getDataKey(id, name):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        if name in tempData:
            return True
        elif name not in tempData:
            return False

def getInvKey(id, name):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        invData = tempData['inventory']
        if name in invData:
            return True
        elif name not in invData:
            return False

def getInvValue(id, name):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        invData = tempData['inventory']
        if name != None:
            return invData[name]

def invInsert(id, name, value):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        invData = tempData['inventory']
        if name != None:
            invData[name] = value
            write_json(data)

def getInvData(id):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        invArray = tempData['inventory']
        return invArray

def insertingDic(id, name):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        tempData[name] = {}
        write_json(data)

def openNewDic(id, name):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        return tempData[name]

def insertInDic(id, dicName, key, value):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        insideDic = tempData[dicName]
        insideDic[key] = value
        write_json(data)

def isNewDic(id, name):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        if name in tempData:
            return True
        else:
            return False
def getDicValue(id, dicName, name):
    realId = idIndexFinder(id)
    with open('database.json') as f:
        data = json.load(f)
        temp = data['users']
        tempData = temp[realId]
        insideDic = tempData[dicName]
        return insideDic[name]

