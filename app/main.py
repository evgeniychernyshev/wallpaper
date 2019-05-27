import os

import waitress

from app.lib import calculate_rolls_count
from flask import Flask, render_template, request


def start():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/calc', methods=['POST'])
    def calc():
        roll_length = float(request.form['roll_length'])
        roll_width = float(request.form['roll_width'])
        room_length = float(request.form['room_length'])
        room_width = float(request.form['room_width'])
        ceiling_height = float(request.form['ceiling_height'])
        result = calculate_rolls_count(roll_length, roll_width, room_length, room_width, ceiling_height)
        return render_template('index.html',
                               rolls_count=result,
                               roll_length=roll_length,
                               roll_width=roll_width,
                               room_length=room_length,
                               room_width=room_width,
                               ceiling_height=ceiling_height)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9878, debug=True)


if __name__ == '__main__':
    start()
