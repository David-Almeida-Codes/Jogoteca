from flask import Flask, render_template, request, redirect, session, flash,url_for

app = Flask(__name__)
app.secret_key = 'koala'


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password


user1 = User('david', 'David Almeida', '2742')
user2 = User('fulano', 'Fulano da Silva', 'xablau')
user3 = User('cicrano', 'Cicrano barusks', 'buia')

users = {user1.id: user1,
         user2.id: user2,
         user3.id: user3}

game1 = Game('Super Mario', 'Ação', 'Super nintendo')
game2 = Game('Pokemon Gold', 'RPG', 'Game Boy')
game3 = Game('Mortal Kombat', 'Luta', 'Super nintendo')
list = [game1, game2, game3]


@app.route('/')
def index():
    return render_template('list.html', title='Jogos', games=list)


@app.route('/new')
def new():
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('new')))
    return render_template('new.html', title='Novo Jogo')


@app.route('/create', methods=['POST',])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    list.append(game)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)


@app.route('/auth', methods=['POST',])
def auth():

    if request.form['user'] in users:
        user = users[request.form['user']]
        if user.password == request.form['password']:
            session['logged_user'] = user.id
            flash(user.name + ' Logou com sucesso!')
            next_page = request.form['next']
            return redirect(next_page)
    else:
        flash('Usuario ou senha invalido tente novamente')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Nenhum usuario logado!')
    return redirect(url_for('index'))


app.run(debug=True)
