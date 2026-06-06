from pickle import APPEND
from bson import encode,decode_all
from bson.objectid import ObjectId
import pathlib


# A sample Python dictionary, which is converted to BSON
document = {
    "name": "Mongo's burger Place",
    "restaurant_id": 12346,
    "rating": 4.5,
    "_id": ObjectId()
}

# Encode the dictionary to a BSON byte strin

name=input()
local=pathlib.Path.cwd()/name
def reader(local):
    if not pathlib.Path.exists(local):
        print("File Not Found")
        return
    with open(local,"rb") as file:
        docu = decode_all(file.read())
    print(docu)
    
def appender(local):
    if not pathlib.Path.exists(local):
        print("File Not Found")
        return
    with open(local,"ab") as file:
        binary_data = encode(document)
        file.write(binary_data)
    print(f"Path:- {local} \n✅ Wrote document with ID: {document['_id']}")
    
def writer(local):
    with open(local,"wb") as file:
        binary_data = encode(document)
        file.write(binary_data)
    print(f"Path:- {local} \n✅ Make document with ID: {document['_id']}")
appender(local)




