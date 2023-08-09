from tinytuya import * 
import  json
#from getmac import get_mac_address as gma
from pymongo import MongoClient, InsertOne


host = 'localhost'
port = 27017
documment = 'LUPS'
deviceInfo = {'objeto':[]}

c = Cloud(
        apiRegion="us", 
        apiKey="wxeysjyjpxjkafykqc38", 
        apiSecret="045a8788c670454f990c91a2102d8c09")

def scanObject():
        devices = c.getdevices()
        for i in range(0, len(devices)):
	        deviceInfo['objeto'].append({       
                                'id': devices[i]['id'],
                                'status': c.getstatus(devices[i]['id'])
                        })


def connectMongo():
        try:
                client = MongoClient(host, port)
                db = client[documment]
                return db
        except Exception as e:
                print("Is not possible connect in database\n Error:", e)

def importDataBase(db):
        try:
 	        collection = db['Objeto']
 	        result = collection.insert_many(deviceInfo['objeto'])
 	        print(result)
        except Exception as e:
 	        print("Is not possible connect in database\n Error:", e)

def main():
        verify = 1
        while verify == 1:
                db = connectMongo()
                scanObject()
                importDataBase(db)
                time(240)
        
main()
	

