from flask import Flask, request, json
# from pip._internal.vcs import git

import messageHandler
import vk_logic
from multiprocessing import Process
import settings
from exts import db
from flask_migrate import Migrate
import git


def register_extensions(app):
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config)
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

    register_extensions(app)

    return app


app = create_app()
migrate = Migrate(app, db)


@app.route("/test", methods=["POST"])
def nnd():
    return 'ok'


@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/maniswear/mysite')
        origin = repo.remotes.origin
        repo.create_head('master',
        origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


@app.route("/bots", methods=["POST"])
def main():
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 0

    if data['type'] == 'confirmation':
        return 'f99e17cd'
    elif data['type'] == "message_allow":
        print('Мы обрабатываем наш запрос и что-то идет не так...')
        user_id = data['object']['message']['from_id']
        message_text = 'Это кнопка Начало'

        vk_logic.send_some_msg(user_id, message_text)

        return 'ok'
    elif data['type'] == 'message_new':
        # p = Process(target=messageHandler.create_answer, args=(data['object']['message'],))
        messageHandler.create_answer(data['object']['message'])

        print('Сообщение о том, что обработка прошла успешно')
        return 'ok'
    elif data['type'] == 'message_reply':
        return 'ok'
    return 'ok'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'This is new login'
