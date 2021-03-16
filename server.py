from flask import Flask, render_template, url_for

app = Flask(__name__)

a = {'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
        'profession': 'штурман марсохода', 'sex': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'}
b = ['surname', 'name', 'education', 'profession', 'sex', 'motivation', 'ready']
c = ['Фамилия:', 'Имя:', 'Образование:', 'Профессия:', 'Пол:', 'Мотивация:', 'Готовы остаться на Марсе?']


@app.route('/answer')
@app.route('/auto_answer')
def index():
    return render_template('auto_answer.html',
                           a=a, b=b, c=c)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')