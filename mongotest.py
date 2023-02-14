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

d_1 = {
    "name":"peter",
    "key":"notTheRealSpidey@gmail.com",
    "surname":"parker"
}

db1 = client['mongotest']
# print(db1)
coll = db1['test']
# print(coll)
coll.insert_one(d )
coll_1 = db1['test_1']
coll_1.insert_one(d_1 )