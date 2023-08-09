from tinytuya import * 
import  json
#from getmac import get_mac_address as gma
from pymongo import MongoClient, InsertOne
import subprocess
import os

host = 'localhost'
port = 27017
documment = 'LUPS'
deviceInfo = {'objeto':[]}
usuario = '****'
senha = '****'

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

def startServiceMongo():
        command = "systemctl start mongod"
        command_credential = f'echo {senha} | sudo -S {command}'
        try:
        # Executa o comando e captura a saída
                resultado = subprocess.check_output(command_credential, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                return resultado
        except subprocess.CalledProcessError as e:
                return f"Erro ao executar o comando: {e.output}"

def verifyStatusMongo():
        commandVerify = "systemctl is-active mongod"
        try:
        # Executa o comando e captura a saída
                resultado = subprocess.check_output(commandVerify, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                return resultado
        except subprocess.CalledProcessError as e:
                return f"Erro ao executar o comando: {e.output}"

def main():
        verify = 1
        while verify == 1:
                result = verifyStatusMongo()
                status = result.strip()
                print(status)
                if(status != 'active'):
                        print(status)
                        startServiceMongo()
                        print(status)
                db = connectMongo()
                scanObject()
                importDataBase(db)
                time.sleep(240)

                
        
main()
	

