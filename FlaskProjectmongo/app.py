from flask import Flask,render_template,request
import sqlite3
from pymongo import MongoClient

app = Flask(__name__)
@app.route('/')
def Index():
    name = "Travel Tourisim And Hospitality"
    return render_template('index.html', data = name)
@app.route('/contact')
def Contact():
    return render_template('contact.html')
@app.route('/about')
def About():
    return render_template('about.html')
@app.route("/newuser")
def my_new_register_page():
    return render_template("newuserregister.html")
@app.route("/login")
def my_new_login_page():
    return render_template("newuserlogin.html")

@app.route("/registeruser", methods=['POST','GET'])
def my_register_user():
    entered_username=request.form.get("username")
    entered_password=request.form.get("password")
    entered_password=entered_password.lower()
    entered_email=request.form.get("email")
    entered_mobileno=request.form.get("mobileno")
    print(entered_username,entered_password,entered_email,entered_mobileno)
    client = MongoClient('mongodb://localhost:27017/')
    db = client['SDP']  # database name
    info = db.SDP
    n={"usernamer":entered_username,
       "password":entered_password,
       "email":entered_email,
       "mobile_mno":entered_mobileno}

    tofind1 = {"email":entered_email}
    user = db.user
    c=0
    for x in tofind1:
        if (user.find_one(tofind1)):
          c=1
    if(c==1):
        return "Email Already Exists...... Try again"
    else:
       user.insert_one(n)
       return "User Registered Successfully"
    # con=sqlite3.connect("my_database.sqlite3")
    # cur=con.cursor()
    # my_table_query="create table if not exists userstable(name varchar(20),password varchar(15),email varchar(30),mobileno varchar(10))"
    # cur.execute(my_table_query)
    # cur.execute(f"select email from userstable where email='{entered_email}'")
    # result=cur.fetchone()
    # if result!=None:
    #     return "Email Already Exists...... Try again"
    # else:
    #     my_insert_query=f"insert into userstable values('{entered_username}','{entered_password}','{entered_email}','{entered_mobileno}')"
    #     cur.execute(my_insert_query)
    #     con.commit()
    #     return "User Registered Successfully"
@app.route("/loginuser",methods=['POST','GET'])
def my_login():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    client = MongoClient('mongodb://localhost:27017/')
    db = client['SDP']  # database name
    info = db.SDP
    user = db.user
    c=0
    tofind1 = {"username":entered_username }
    for x in tofind1:
        if(user.find_one(tofind1)):
            c=1
    tofind2={"password":entered_password}
    for x in tofind2:
        if (user.find_one(tofind2)):
            c = 2
    # con=sqlite3.connect("my_database.sqlite3")
    # cur=con.cursor()
    # cur.execute(f"select * from userstable where name='{entered_username}' and password='{entered_password}'")
    # result=cur.fetchone()
    if (c!=2):
        return "Invalid User Credentials... try again"
    else:
        return "Success"

if __name__ == "__main__":
    app.run(debug=True)