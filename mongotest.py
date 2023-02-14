import pymongo
# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb1234.lgeu361.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb1234@cluster0.lgeu361.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
print(db)

d = {
    "name":"elden",
    "key":"eldenelliot@gmail.com",
    "surname":"elliot"
}

db1 = client['mongotest']
# print(db1)
coll = db1['test']
# print(coll)
coll.insert_one(d )