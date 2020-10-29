from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutdane')
def aboutdane():
    return render_template('aboutdane.html')

if __name__ == '__main__':
    app.run(debug=True, port='3000')
