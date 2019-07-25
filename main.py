#!/usr/bin/env python

from flask import Flask, render_template, redirect, request, current_app, jsonify
app = Flask(__name__)

from functools import wraps
import json

from Adafruit_DHT import DHT11, read_retry

def raw_dht():
    sensor = DHT11
    pin = 21
    return read_retry(sensor, pin)

#def support_jsonp(f):
#    """Wraps JSONified output for JSONP"""
#    @wraps(f)
#    def decorated_function(*args, **kwargs):
#        callback = request.args.get("callback", False)
#        if callback:
#            content = str(callback) + "(" + str(f(*args,**kwargs)) + ")"
#            return current_app.response_class(content, mimetype="application/javascript")
#        else:
#            return f(*args, **kwargs)
#    return decorated_function


#@support_jsonp
#def api_dht():
#    humidity, temperature = raw_dht()
#    if humidity is not None and temperature is not None:
#        return "{ temperature: '" + "{0:0.0f}".format(temperature) +  "', humidity: '" + "{0:0.0f}".format(humidity) + "' }"
#    else:
#        return "Failed to get reading. Try again!", 500
    
#@support_jsonp
@app.route("/api/humidity")
def humidity():
    humidity_reading, temperature_reading = raw_dht()
    
    if humidity_reading is not None:
        return jsonify(humidity=humidity_reading)
    else:
        return jsonify(noreponse="")
    
#@support_jsonp
@app.route("/api/temperature")
def temperature():
    humidity_reading, temperature_reading = raw_dht()
    
    if temperature_reading is not None:
        return jsonify(temperature=temperature_reading)
    else:
        return jsonify(noreponse="")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
