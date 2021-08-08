from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-bad-secret-key'
socketio = SocketIO(app)


@app.route('/')
def home():
    return render_template('index.html')


@socketio.on('message')
def message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


@socketio.on('connect')
def connect():
    print('New user connected: ' + request.sid)


@socketio.on('disconnect')
def disconnect():
    print('User ' + request.sid + ' has disconnected.')


if __name__ == '__main__':
    socketio.run(app)
