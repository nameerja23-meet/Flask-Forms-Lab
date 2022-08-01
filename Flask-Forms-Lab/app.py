from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'shh'


username = "Nameer"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods =['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		inpUsername = request.form['username']
		inpPassword = request.form['password']
		if (inpUsername == username) and (inpPassword == password):
			return redirect(url_for('home'))
		else:
			return render_template('login.html', error = "Invalid username or password, try again.")
	else:
		return render_template('login.html')
	
  
@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html',
		friends=facebook_friends)


@app.route('/friend_exists/<string:friend>', methods=['GET', 'POST'])
def friendExists(friend):
	if friend in facebook_friends:
		friendExists =True
	else:
		friendExists = False
	return render_template('friend_exists.html',
		friend = friend,
		friendExists = friendExists)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)