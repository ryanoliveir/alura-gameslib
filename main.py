from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt  

class Game():
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

game1 = Game('Tetris', 'Puzzle', 'Atari')
game2 = Game('God of War', 'Rack n Slash', 'PS2')
game3 = Game('CSGO', 'FPS', 'PC')
game4 = Game('Mortal Combat', 'Fight', 'PS2')

games = [game1, game2, game3, game4]


app = Flask(__name__)
app.secret_key = 'flaks_secret_key'
bcrypt = Bcrypt(app)

USER = 'ryan'
PASSWORD = '123456'
PASSWORD_HASH = bcrypt.generate_password_hash(PASSWORD)


@app.route('/authentication', methods=['POST'])
def authentication():
    user = request.form['user']
    password = request.form['password']

    if user == USER and bcrypt.check_password_hash(PASSWORD_HASH, password):
        session['user'] = user
        return redirect('/')

    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    print(name, category, console)
    new_game = Game(name, category, console)
    games.append(new_game)
    

    # return render_template('list.html', titles='Games', games=games)
    return redirect('/')

@app.route('/register-game')
def register_game():
    return render_template('game-form.html', title='Novo Jogo')

@app.route('/')
def index():
    if 'user' in session:
        print(session)
        return render_template('list.html', title='Games', games=games)
    
    return redirect('/login')


if(__name__ == '__main__'):
    app.run(debug=True)
