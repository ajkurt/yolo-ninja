from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO ### Oly works on Raspi

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/help')
def help():
    return render_template('help.html')


#@app.route("/readPin/<pin>")
#def readPin(pin):
    # try:
    # GPIO.setup(int(pin), GPIO.IN)
    #	if GPIO.input(int(pin)) == True:
    #		response = "Pin number " + pin + " is high!"
    #	else:
    #		response = "Pin number " + pin + " is low!"
    # except:
        #	response = "There was an error reading pin " + pin + "."
        #
        # templateData = {
        #	'title': 'Status of Pin' + pin,
        #	'response': response
        #}
        # return render_template('pin.html', **templateData)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
