from flask import Flask, render_template


class Game():
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


app = Flask(__name__)


@app.route('/home')
def home():

    game1 = Game('Tetris', 'Puzzle', 'Atari')
    game2 = Game('God of War', 'Rack n Slash', 'PS2')
    game3 = Game('CSGO', 'FPS', 'PC')
    game4 = Game('Mortal Combat', 'Fight', 'PS2')

    games = [game1, game2, game3, game4]
    return render_template('list.html', title='Games', games=games)


if(__name__ == '__main__'):
    app.run(debug=True)
