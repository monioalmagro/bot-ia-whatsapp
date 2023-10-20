
from flask import Flask, request
import sett
import services
from utils import process_message


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/bienvenido', methods=['GET'])
def bienvenido():
    return 'Hola mundo bigdateros, desde Flask'


@app.route('/webhook', methods=['GET'])
def verificar_token():
    try:
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token == sett.token and challenge != None:
            return challenge
        else:
            return 'token incorrecto', 403
    except Exception as e:
        return e, 403


@app.route('/webhook', methods=['POST'])
def recibir_mensajes():
    try:
        body = request.get_json()
        message = process_message(body)
        services.administrar_chatbot(
            message.text,
            message.number,
            message.messageId,
            message.name
        )
        return 'enviado'
    except Exception as e:
        print(e)
        return f'no enviado {str(e)}'


if __name__ == '__main__':
    app.run()
