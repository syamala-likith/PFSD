from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

db = client['likith']
info = db.likith
field = {"username", "age", "gamil", "pass"}
data = [
    {"username": "likith",  "age": 19, "gmail": "rockylikith9886@", "pass": "li123"},
    {"username": "sai@", "age": 18, "gmail": "sai@", "pass": "123ed"},
    {"username": "sandeep@",  "age": 18, "gmail": "sandeeep@", "pass": "1rgrbd"}

]
# Creating document
studentdata = db.PFSD
studentdata.insert_many(data)
tofind1={"username":"likith@"}
for x in tofind1:
    print(studentdata.find_one(tofind1))
delete = {"username":"likith@"}
studentdata.delete_many(delete)