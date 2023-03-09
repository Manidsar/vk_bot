import vk_logic
import importlib
import os
from command_system import command_list
import models
import keyboards

def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("mysite/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])


def get_answer(body):
    # Подгружаем базу данных
    student = models.get_status(body["from_id"])
    # Сообщение по умолчанию если распознать не удастся
    data = body["text"]
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    keyboard = False
    for c in command_list:
        if data.lower() in c.keys:
            message, keyboard = c.process(student)
    if message == "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды":
        if student.register:
            message = models.registration(body["from_id"], data)
            keyboard = keyboards.base_reg()
    return message, keyboard


# Прикрепляем нужную клавиатуру, если новая не нужна, то False
def create_answer(data):
    if not models.db.session.query(models.Student).filter_by(id=data["from_id"]).first():
        print('Регистрируем пользователя скрытно')
        new_st = models.Student(id=data["from_id"])
        models.db.session.add(new_st)
        models.db.session.commit()
    load_modules()
    user_id = data['from_id']
    message, keyboard = get_answer(data)
    vk_logic.send_some_msg(user_id, message, keyboard)


