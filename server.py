from flask import Flask, render_template, request
from weather import get_current_weather # file we made !
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city) # our function! 
    try:
        return render_template(
            "weather.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
            # (f)ormatted to the nearest (:.1) 10th place digit
        )
    except Exception as e:
        #print(e, "nooo") # when error occurs with getting city
        return render_template('city-not-found.html')

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 8000)