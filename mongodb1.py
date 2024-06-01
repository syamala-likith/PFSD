from pymongo import MongoClient # import mongo client to connect
# Creating instance of mongoclient
client = MongoClient('mongodb://localhost:27017/')
# Creating database
db = client['li']
info = db.li
student1 = {"Reg Num":"2100030008","Name": "MANIKANTH"}
student2 = [
    {"Reg Num":"2100030000","Name": "DEEPAK"},
    {"Reg Num":"2100030199","Name": "MANISH"},
    {"Reg Num":"2100030261","Name": "PAVANI"}
]
# Creating document
studentdata = db.student
# Inserting data
#studentdata.insert_one(student1)
# Inserting Many Data
studentdata.insert_many(student2)
# Fetching one data
#print(studentdata.find_one())
# Fetching specific data
tofind1 = {"Reg Num":"2100030261"}
for x in tofind1:
    print(studentdata.find_one(tofind1))
# Delete one data
#todelete1 = {"Reg Num":"2100030199"}
#studentdata.delete_one(todelete1)
#print(todelete1.deleted_count, "documents deleted")
# Delete Many Data
todelete2 = {"Reg Num":"2100030008"}
studentdata.delete_many(todelete2)
#print(len(todelete2.), "documents deleted")