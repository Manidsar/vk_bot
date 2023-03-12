from flask import Flask, request, json
from threading import Thread

import messageHandler

app = Flask('')


@app.route('/')
def home():
  return "I'm alive"


def run():
  app.run(host='0.0.0.0', port=80)


def keep_alive():
  t = Thread(target=run)
  t.start()

keep_alive()

@app.route("/test", methods=["POST"])
def nnd():
  return 'ok', 200


@app.route("/bots", methods=["POST"])
def main():
  data = json.loads(request.data)

  if 'type' not in data.keys():
    return 0

  if data['type'] == 'confirmation':
    return '39ff8c66'
  elif data['type'] == "message_allow":
    return 'ok'
  elif data['type'] == 'message_new':
    # t = Thread(targer=messageHandler.create_answer, args=(data['object']['message'],))
    messageHandler.create_answer(data['object']['message'])

    print('Обработка прошла успешно')
    return 'ok'
  elif data['type'] == 'message_reply':
    return 'ok'
  return 'ok'


@app.route('/login', methods=['GET', 'POST'])
def login():
  return 'This is new login', 200
