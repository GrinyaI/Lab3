from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/authorization', methods=['post'])
def authoriz():
    data = {}
    au = ''
    with open('Bd.txt', 'r') as file:
        for line in file:
            key, *value = line.split()
            data[key] = value
    if request.method == 'POST':
        log = str(request.form.get('login').strip())
        pas = str(request.form.get('password').strip())
        if data.get(log):
            if data[log][0]==pas:
                au = 'Авторизация выполнена успешно'
            else:
                au = 'Пароль введён неверно'
        else:
            au = 'Логин отсутствует/введён неверно'
    return render_template('authorization.html', ath=au)

@app.route('/registration', methods=['post'])
def registr():
    data = {}
    reg = ''
    if request.method == 'POST':
        log = str(request.form.get('login').strip())
        pas = str(request.form.get('password').strip())
        with open('Bd.txt', 'r') as file:
            for line in file:
                key, *value = line.split()
                data[key] = value
            if data.get(log):
                reg = 'Данный логин занят'
            else:
                with open('Bd.txt', 'a') as writ:
                    try:
                        writ.write(log + ' ' + pas + '\n')
                        reg = 'Регистрация выполнена'
                    except:
                        reg = 'Регистрация не выполнена'
    return render_template('registration.html', regis=reg)
