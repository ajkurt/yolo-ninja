from flask import Flask, render_template, redirect, url_for, request
import datetime
import RPi.GPIO as GPIO ### Oly works on Raspi
import serial

app = Flask(__name__)
loged = False

@app.route('/')
def home():
	if loged == True:
		return render_template('home.html')
	else:
		return redirect(url_for('login'))

@app.route('/help')
def help():
	return render_template('help.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			loged = True
			return redirect(url_for('home'))
	return render_template('login.html', error=error)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug=True)
