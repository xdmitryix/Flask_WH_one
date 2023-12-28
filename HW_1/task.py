from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html/')
def index():
    return render_template('index.html')

@app.route('/hats.html/')
def hats():
    return render_template('hats.html')

@app.route('/clothes.html/')
def clothes():
    return render_template('clothes.html')

@app.route('/shoes.html/')
def shoes():
    return render_template('shoes.html')


if __name__ == '__main__':
    app.run(debug=True)
