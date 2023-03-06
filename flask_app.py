from flask import Flask, request, json
import messageHandler
import vk_logic
from multiprocessing import Process
import settings
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=settings.username,
    password=settings.psw,
    hostname=settings.hostname,
    databasename=settings.databasename,
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Запуск потока для каждого нового обращения к боту
# def hub():
#     p = Process(target=main, args=(request.data,))
#     p.start()
#
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
        # p = Process(target=messageHandler.create_answer, args=(data['object']['message'],))
        messageHandler.create_answer(data['object']['message'])

        # Сообщение о том, что обработка прошла успешно
        return 'ok'
    elif data['type'] == 'message_reply':
        return 'ok'


@app.route('/login', methods=['GET'])
def login():
    return 'This is login'
