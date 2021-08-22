from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=ccca0349afeef656e2f71584d24fcf54')
    json_object = r.json()
    coord_l=float(json_object['coord']['lon'])
    coord_la=float(json_object['coord']['lat'])
    temp_k = float(json_object['main']['temp'])
    description= json_object["weather"][0]["description"]
    feels_like=float(json_object['main']['feels_like'])
    pressure= float(json_object['main']['pressure'])
    humidity=float(json_object['main']['humidity'])
    sunrise =float(json_object['sys']['sunrise'])
    sunset =float(json_object['sys']['sunset'])

    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('temperature.html', temp=temp_f,description=description,feels_like=feels_like,pressure=pressure,humidity=humidity,sunrise=sunrise,sunset=sunset,coord_l=coord_l,coord_la=coord_la)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
