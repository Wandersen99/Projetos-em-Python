#Importar o framework para fazer a ligação entre o front e o back end
from flask import Flask, render_template
from flask_socketio import SocketIO,send

#Criar o app/site
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#Funcionalidade de enviar mensagem 
@socketio.on("message")
def gerenciar_messagem(mensagem):
    send(mensagem, broadcast = True)
    

# Criar a primeira página = 1°rota
@app.route("/") #decorator
def homepage():
    return render_template("index.html")

# Rodar o aplicativo
socketio.run(app, host = "localhost")