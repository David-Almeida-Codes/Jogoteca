from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'koala'

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


game1 = Game('Super Mario', 'Ação', 'Super nintendo')
game2 = Game('Pokemon Gold', 'RPG', 'Game Boy')
game3 = Game('Mortal Kombat', 'Luta', 'Super nintendo')
list = [game1, game2, game3]


@app.route('/')
def index():
    return render_template('list.html', title='Jogos', games=list)


@app.route('/new')
def new():
    return render_template('new.html', title='Novo Jogo')


@app.route('/create', methods=['POST',])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    list.append(game)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/auth', methods=['POST'])
def auth():
    if 'mestra' == request.form['password']:
        session['logged_user'] = request.form['user']
        flash(request.form['user'] + ' Logou com sucesso!')
        return redirect('/')
    else:
        flash('Usuario ou senha invalido tente novamente')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Nenhum usuario logado!')
    return redirect('/')


app.run(debug=True)
