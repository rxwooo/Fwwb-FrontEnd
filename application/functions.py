from msilib.schema import tables
import time, json, copy
from unicodedata import name

from flask import redirect
from application.models import Image, Result, Class, User

testJson = {
    "len": 2,
    "result": [
        {
            "class_id": 1,
            "score": 0.888,
            "x_min": 50,
            "x_max": 100,
            "y_min": 50,
            "y_max": 10
        },
        {
            "class_id": 2,
            "score": 0.999,
            "x_min": 150,
            "x_max": 200,
            "y_min": 150,
            "y_max": 20
        }
    ]
}
def change_type(byte):    
    if isinstance(byte,bytes):
        return str(byte,encoding="utf-8")  
    return json.JSONEncoder.default(byte)

def generateTimeName():
    timeStamp = int(time.time())
    timeArray = time.localtime(timeStamp)
    styleTime = time.strftime("%Y_%m_%d_%H_%M_%S", timeArray)
    return styleTime

def dbAddImage(imageName, database, savePath, user):
    image = Image(imagename = imageName, path = savePath, userid = user)
    database.session.add(image)
    database.session.commit()
    return image.id
    
def process(imageId, database):
    path = Image.query.get_or_404(int(imageId)).path
    reJson = copy.deepcopy(testJson)
    reJson["imageSrc"] = path
    for re in reJson["result"]:
        result = Result(
            imageid = imageId,
            classid = re["class_id"],
            score = re["score"],
            min_x = re["x_min"],
            max_x = re["x_max"],
            min_y = re["y_min"],
            max_y = re["y_max"]
        )
        database.session.add(result)
        classid = re["class_id"]
        re["class_name"] = Class.query.get_or_404(classid).classname
        re.pop("class_id")
    database.session.commit()
    return json.dumps(reJson)

def detailReTab(userid, database):
    
    queryid = [userid]
    if(userid == 1):
        queryid = database.session.query(User.id)
    
    results = []
    images = database.session.query(Image.id, Image.path, Image.userid).filter(Image.userid.in_(queryid))
    tableData = [0, 0, 0, 0]
    for img in images:
        imgResult = {}
        reQuery = database.session.query(Result.classid, Result.min_x, Result.max_x, Result.min_y, Result.max_y).filter(Result.id == img[0])
        imgResult["len"] = reQuery.count()
        imgResult["src"] = img[1];
        imgResult["user"] = database.session.query(User.name).filter(User.id == img[2]).first()[0]
        result = []
        for re in reQuery:
            tableData[re[0] - 1] += 1
            reObj = {}
            reObj["class_name"] = Class.query.get_or_404(re[0]).classname
            reObj["min_x"] = re[1]
            reObj["max_x"] = re[2]
            reObj["min_y"] = re[3]
            reObj["max_y"] = re[4]
            result.append(reObj)
        imgResult["result"] = copy.deepcopy(result)
        results.append(imgResult)
    
    length = len(results)
    reTab = {}
    reTab["length"] = length
    reTab["results"] = results
    reTab["data"] = tableData
    
    return reTab
    
    
def getUserList(userid, database):
    queryid = [userid]
    if(userid == 1):
        queryid = database.session.query(User.id)
    
    names = database.session.query(User.name).filter(User.id.in_(queryid)).all()
    namelist = []
    for i in names:
        namelist.append(i[0])
    
    return {'namelist': namelist}

def getDataAndDate(uname, database):
    names = []
    if(uname == "Select ALL"):
        names = database.session.query(User.id).all()
    else:
        names = database.session.query(User.id).filter(User.name == uname)
    uid = []
    for i in names:
        uid.append(i[0]);
    
    dateDict = {}
    images = database.session.query(Image.imagename, Image.id).filter(Image.userid.in_(uid))
    for i in images:
        date = i[0];
        dateArr = date.split('_')
        dateStr = dateArr[0] + '/' + dateArr[1] + '/' + dateArr[2]
        dateDict.setdefault(dateStr, [0, 0, 0, 0])
        results = database.session.query(Result.classid).filter(Result.imageid == i[1])
        for re in results:
            dateDict[dateStr][re[0] - 1] += 1
        
   
    reDict = {} 
    reDict['date'] = list(dateDict.keys())
    reDict["data"] = [[], [], [], []]
    tempList = list(dateDict.values())
    for i in tempList:
        reDict["data"][0].append(i[0])
        reDict["data"][1].append(i[1])
        reDict["data"][2].append(i[2])
        reDict["data"][3].append(i[3])
    return reDict

    
    