import flask
import sqlite3

my_website = flask.Flask(__name__)

@my_website.route("/")
def my_index_page():
    return flask.render_template("login.html")

@my_website.route("/newuser")
def my_newuser_register_page():
    return flask.render_template("newuserregister.html")

@my_website.route("/registeruser", methods=['post'])
def my_regiser_user():
    entered_username = flask.request.form.get("username")
    entered_password = flask.request.form.get("password")
    entered_password = entered_password.lower()
    entered_email = flask.request.form.get("email")
    entered_mobileno = flask.request.form.get("mobileno")

    print(entered_username, entered_password, entered_email, entered_mobileno)

    con = sqlite3.connect("my_database.sqlite3")

    cur = con.cursor()

    my_table_query = "create table if not exists userstable(name varchar(20),password varchar(15),email varchar(30),mobileno varchar(10))"
    cur.execute(my_table_query)

    cur.execute(f"select email from userstable where email='{entered_email}'")
    result = cur.fetchone()
    if result != None:
        return "Email Already Exists....Try again"
    else:
        my_insert_query = f"insert into userstable values('{entered_username}','{entered_password}','{entered_email}','{entered_mobileno}')"
        cur.execute(my_insert_query)
        con.commit()
        return "User Registered Successfully"


@my_website.route("/loginuser", methods=['post'])
def my_login():
    entered_username = flask.request.form.get("username")
    entered_password = flask.request.form.get("password")
    con = sqlite3.connect("my_database.sqlite3")
    cur = con.cursor()
    cur.execute(f"select * from userstable where name='{entered_username}' and password='{entered_password}'")

    result = cur.fetchone()
    if result is None:
        return "Invalid User Credentials....try again"
    else:
        return "Login Success"


if __name__ == "__main__":
    my_website.run(debug=True)
