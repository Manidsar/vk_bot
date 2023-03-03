from flask import Flask, request, json
import messageHandler
import vk_logic

app = Flask(__name__)


@app.route("/bots", methods=["POST"])
def main():
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 0

    if data['type'] == 'confirmation':
        return 'token'
    elif data['type'] == "message_allow":
        user_id = data['object']['message']['from_id']
        message_text = 'Это кнопка Начало'

        vk_logic.send_some_msg(user_id, message_text)

        # Сообщение о том, что обработка прошла успешно
        return 'ok'
    elif data['type'] == 'message_new':

        messageHandler.create_answer(data['object']['message'])

        # Сообщение о том, что обработка прошла успешно
        return 'ok'


@app.route('/login', methods=['GET'])
def login():
    return 'This is login'
