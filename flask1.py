from flask import Flask, render_template

#creating instance
app=Flask(__name__)
#normal route
@app.route("/")
def sample():
    return '<i><h1> This is Web page</h1></i>'
#Dynamic routing
@app.route("/<name>")
def sample2(name):
    return f'Hello {name}'

#Flask-Template rendering
@app.route("/template")
def sample3():
    return render_template('index.html')

if __name__== "__main__":
    app.run()