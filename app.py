from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/F/<celsius>')
def celsius_to_fahrenheit(celsius=""):
    fahrenheit = int(celsius) * 9.0 / 5 + 32
    return "{} in Celsius gives {} in Fahrenheit".format(celsius, fahrenheit)


@app.route('/C/<fahrenheit>')
def fahrenheit_to_celsius(fahrenheit=""):
    celsius = 5 / 9 * (int(fahrenheit) - 32)
    return "{} in Fahrenheit gives {} in celsius".format(fahrenheit, celsius)



if __name__ == '__main__':
    app.run()
