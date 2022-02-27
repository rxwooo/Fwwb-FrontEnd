import time, json, copy
from flask import jsonify
from application.models import Image, Result, Class

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

def dbAddImage(imageName, database, savePath):
    image = Image(imagename = imageName, path = savePath)
    database.session.add(image)
    database.session.commit()
    return image.id
    
def process(imageId, database):
    path = Image.query.get_or_404(imageId).path
    print(path)
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

