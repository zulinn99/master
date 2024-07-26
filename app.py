from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('chat message')
def handle_chat_message(data):
    data['timestamp'] = int(time.time() * 1000)
    emit('chat message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
