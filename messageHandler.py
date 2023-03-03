import vk_logic
import importlib
import os
from command_system import command_list


def load_modules():
    # путь от рабочей директории, ее можно изменить в настройках приложения
    files = os.listdir("mysite/commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def get_answer(body):
    # Сообщение по умолчанию если распознать не удастся
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    for c in command_list:
        if body in c.keys:
            message = c.process()
    return message


def create_answer(data):
    load_modules()
    user_id = data['from_id']
    message = get_answer(data['text'].lower())
    keyboard = True
    vk_logic.send_some_msg(user_id, message, keyboard)
