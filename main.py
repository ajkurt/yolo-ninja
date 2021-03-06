from flask import Flask, render_template, redirect, url_for, request
from time import sleep
import datetime
import RPi.GPIO as GPIO ### Oly works on Raspi
import serial
app = Flask(__name__)
ser=serial.Serial('/dev/ttyACM0', 9600, timeout=1)

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route('/help')
def help():
	return render_template('help.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
	led = ser.write('read-13\n')
	led13 = ser.readline(1)
	led13_2 = ser.readline(1)
	if led13 == '0':
		led13 = 'Ligar'
	elif led13 == '1':
		led13 = 'Desligar'
	else:
		pass

	error = None
	if request.method == 'POST':
		if request.form['submit'] == "Led Placa":
			ser.write('change-13\n')
		elif request.form['submit'] == "Rele 02":
			ser.write('pinRele2-\n')
		else:
			error = 'Invalid command. Please try again.'
			return render_template('inputSerial.html', error=error)
	return render_template('home.html', led13=led13, led13_2=led13_2)

@app.route('/inputSerial', methods=['GET', 'POST'])
def inputSerial():	
	return render_template('inputSerial.html', error=error)
	

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug=True)
