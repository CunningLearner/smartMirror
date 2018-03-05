from flask import Flask, render_template
from darksky import forecast
INDIA = 28.6139, 77.2090
from flask_socketio import SocketIO, send, emit

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

message='coming from raspberrypi flask web socket'

with forecast('989a02fffdf1a8f6c8e20530e3ca7f11', *INDIA) as india:
    weather=round((india.temperature - 32) * (.5556),2) 
    wsum= (india.daily.icon)

@socketio.on('connect')
def handle_message(message):
    send(message)

# @socketio.on('message')
# def handle_message(message):
#     print('received message: ' + message)
# weather = 'dog'
@app.route("/")
def main():
	return render_template('untrodden_backup.html', value=weather , summary= wsum)

# @app.route("/data")
# def data():
#       #return render_template('indexcardio.html')
#       return message

if __name__=="__main__":
       socketio.run(app,host='127.0.0.1',debug=True,port=5019)
 

