from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<a>')
def index(a):
    return render_template('base.html',
                           a=a)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')