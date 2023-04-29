from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    data = {'login': 'password'}
    au = ''
    if request.method == 'POST':
        log = str(request.form.get('login').strip())
        pas = str(request.form.get('password').strip())
        if data.get(log):
            pa = data[log]
            if pa==pas:
                au = 'Авторизация выполнена успешно'
            else:
                au = 'Пароль введён неверно'
        else:
            au = 'Логин отсутствует/введён неверно'
    return render_template('index.html', auth=au)