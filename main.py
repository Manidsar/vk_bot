from flask import Flask, request, json
import messageHandler

app = Flask(__name__)


# def run():
#   app.run(host='0.0.0.0', port=80)
  
# def keep_alive():
#   t = Thread(target=run)
#   t.start()

app.run(host='0.0.0.0', port=80)

@app.route("/test", methods=["POST"])
def nnd():
    return 'ok'


@app.route("/bots", methods=["POST"])
def main():
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 0

    if data['type'] == 'confirmation':
        return 'f99e17cd'
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
    return 'This is new login'

