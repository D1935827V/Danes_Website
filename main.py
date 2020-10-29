from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutdane')
def aboutdane():
    return render_template('aboutdane.html')

@app.route('/abouteva')
def abouteva():
    return render_template('abouteva.html')

@app.route('/aboutida')
def aboutida():
    return render_template('aboutida.html')

@app.route('/aboutcrystal')
def aboutcrystal():
    return render_template('aboutcrystal.html')

@app.route('/aboutnivu')
def aboutnivu():
    return render_template('aboutnivu.html')

if __name__ == '__main__':
    app.run(debug=True, port='3000')
