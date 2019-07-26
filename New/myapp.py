from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


#def get_data():
 #   return request.get('http://192.168.43.231:5000/api/humidity').content
    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    temp = ""
    humid = ""
    if request.method == 'POST':
        if request.form.get('temperature')=='temperature':

            temp = requests.get('http://192.168.43.231:5000/api/temperature').json()['temperature']


        if request.form.get('humidity')=='humidity':

            humid = requests.get('http://192.168.43.231:5000/api/humidity').json()['humidity']
    return render_template('index.html', temperature = temp, humidity = humid)
#def get_data():
    #return requests.get('http://192.168.43.231:5000/api/humidity').content
    




#@app.route('/', methods=['GET', 'POST'])
#def index():
#    humidity_response = ""
#    if request.method == 'POST':
#        if request.form.get('temperature')=='temperature':
#            def get_data():
#                humidity_response = request.get('http://192.168.43.231:5000/api/humidity').content
#
##    humidity_json = json.loads(humidity_response)
#    #print(humidity_json)
#            return render_template('index.html')

#@app.route('/temperature/', methods=['POST'])
#def temperature():
#    print("10")
#    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
