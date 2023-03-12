import vk_logic
import importlib
import os
from command_system import command_list
import models
import keyboards


def load_modules():
  # путь от рабочей директории, ее можно изменить в настройках приложения
  files = os.listdir("./commands")
  modules = filter(lambda x: x.endswith('.py'), files)
  for m in modules:
    importlib.import_module("commands." + m[0:-3])


def get_answer(body):
  # Подгружаем базу данных
  student = models.db[str(body["from_id"])]
  # student = models.get_status(body["from_id"])
  # Сообщение по умолчанию если распознать не удастся
  data = body["text"]
  message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
  keyboard = False
  for c in command_list:
    if data.lower() in c.keys:
      message, keyboard = c.process(student)
  if message == "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды":
    if student['register']:
      message = models.registration(str(body["from_id"]), data)
      keyboard = keyboards.base_reg()
  return message, keyboard


# Прикрепляем нужную клавиатуру, если новая не нужна, то False
def create_answer(data):
  print(data['from_id'])
  print(models.db.keys())
  if not str(data['from_id']) in models.db.keys():
    # if not models.db.session.query(models.Student).filter_by(id=data["from_id"]).first():
    print('Регистрируем пользователя скрытно')
    models.start_register(id=data['from_id'])
  print('Мы что-то получили по крайне мере вышил из ифа')
  load_modules()
  user_id = data['from_id']
  message, keyboard = get_answer(data)
  vk_logic.send_some_msg(user_id, message, keyboard)
