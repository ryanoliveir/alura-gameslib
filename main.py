from flask import Flask, render_template, request, redirect


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
    return render_template('list.html', title='Games', games=games)


if(__name__ == '__main__'):
    app.run(debug=True)
