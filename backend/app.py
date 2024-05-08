from flask import Flask, jsonify, request
from flask_cors import CORS
from connect4 import *
app = Flask(__name__)
cors = CORS(app, origins="*")


@app.route('/api/board', methods=['GET'])
def board():
    return jsonify(
        {
            'status': 200,
            'board': game.board.board
        }
    )


@app.route('/api/reset', methods=['GET'])
def reset():
    game.reset()
    return jsonify(
        {
            'status': 200,
            'board': game.board.board,
            'turn': game.turn,
        }
    )


@app.route('/api/move', methods=['POST'])
def move():
    data = request.get_json()
    column = data.get('column')
    playerID = data.get('playerID')
    status = game.move(column, playerID)
    return jsonify(
        {
            'status': status,
            'board': game.board.board,
            'turn': game.turn,
            'column': data.get('column'),
            'winner': game.winner,
        }
    )


if __name__ == '__main__':
    game = Game()
    print("Game started")
    app.run(debug=True, port=8080)
