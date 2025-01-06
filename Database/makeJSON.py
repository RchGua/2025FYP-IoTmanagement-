from pymongo import MongoClient
from datetime import datetime

class makeJSON:
    def __init__(self):##defalt
        pass

    def speaker(soundtrack, power):#power should be on and off, TRUE and False
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S") 
        json = {"datetime":current_time,"soundtrack":soundtrack, "power": power}
        return json
    
    def user(ownedCharger, identity, manageCharger):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S") 
        json = {"datetime":current_time,"ownedCharger":ownedCharger, "identity": identity, "power": manageCharger}
        return json
    
    def th(temperature, humidity, power):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S") 
        json = {"datetime":current_time,"temperature":temperature, "humidity": humidity, "power": power}
        return json

    def wl(isleak, waterLevel, power):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S") 
        json = {"datetime":current_time,"isleak":isleak, "waterLevel": waterLevel, "power": power}
        return json
    
    def hm(ispresence, activity, heartRate, power):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S") 
        json = {"datetime":current_time,"ispresence":ispresence, "activity": activity,"heartRate": heartRate, "power": power}
        return json
    
    def charger(chargingStatus, energyConsumption, chargingTime, powerOutput, batteryLevel, gridImpact, power):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S") 
        json = {"datetime":current_time,"chargingStatus":chargingStatus, "energyConsumption": energyConsumption,"chargingTime": chargingTime, "powerOutput": powerOutput, "batteryLevel": batteryLevel,"gridImpact": gridImpact,"power": power}
        return json

    def panel(ischarger, iswlsensor, isthsensor, ishmsensor,isspeaker):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S") 
        json = {"datetime":current_time,"iswlsensor":iswlsensor, "isthsensor": isthsensor,"ishmsensor": ishmsensor, "isspeaker": isspeaker}
        return json
    
    def linkage():
        self.charger

if __name__ ==  "__main__":
    print(makeJSON.speaker("some data",True))
    
    try:
        client = MongoClient("mongodb+srv://IoTadmin:admin888@maincluster.xh201.mongodb.net/")
        database  = client.get_database("TestDatabase")
        collection = database.get_collection("TestCollection")
        print("Connected successfully")

        result = collection.insert_one(makeJSON.speaker("new data",True))
        print(f"speaker inserted with id: {result.inserted_id}")
        print(result.acknowledged)

        client.close()
        print("close connection")

    except Exception as e:
        raise Exception("The following error occurred: ", e)
