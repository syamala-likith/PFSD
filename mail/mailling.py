from flask import Flask
from flask_mail import Mail, Message
import csv

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sivamukkala4@gmail.com'
app.config['MAIL_PASSWORD'] = 'snycogwihjlnvfbc' #macblbnicpgyvrjv
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)



#message object mapped to a particular URL '/'
@app.route("/")
def index():
	with open('try.csv','r') as f:
		reader = csv.reader(f)
		next(reader)
		for name, addr in reader:
			msg = Message(f'Hello {name} THIS IS JUST AN PFSD - FLASK MAIL USING CSV',
						sender='sivamukkala4@gmail.com', recipients=[addr])
			msg.body = 'Hi! Ur receiving this mail because u have attended PFSD CLASS ON 14.09.22 -- DO NOT WORRY '\
					'THIS IS JUST A PFSD - FLASK MAIL USING CSV EXAMPLE PROGRAM'
			mail.send(msg)
			print(f'sent to {name}')
			# return  f'Sent to {name}'

if __name__=='__main__':
	app.run(debug=True)