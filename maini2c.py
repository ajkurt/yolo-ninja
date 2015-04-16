from flask import Flask, render_template, redirect, url_for, request
from time import sleep
import datetime
import RPi.GPIO as GPIO ### Oly works on Raspi
import serial
import smbus
led13 = 0
bus = smbus.SMBus(1) # for RPI version 1, use "bus = smbus.SMBus(0)"
address = 0x04 # This is the address we setup in the Arduino Program
app = Flask(__name__)


def writeNumber(value):
	bus.write_byte(address, value)
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	# number = bus.read_byte_data(address, 1)
	return number

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
	global led13
	error = None
	if request.method == 'POST':
		if request.form['submit'] == "Led Placa":
			writeNumber(13)
			#sleep(1)
			led13 = readNumber()
		elif request.form['submit'] == "Rele 02":
			pass
		else:
			error = 'Invalid command. Please try again.'
			return render_template('inputSerial.html', error=error)
	return render_template('home.html', led13=led13)

@app.route('/inputSerial', methods=['GET', 'POST'])
def inputSerial():	
	return render_template('inputSerial.html', error=error)
	

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug=True)
