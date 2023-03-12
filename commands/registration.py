import command_system
import models


def registration(st):

  keyboard = False
  # Тут мы обнулим все остальные статусы
  print(st['name'])
  if st['name']:
    message = '''
Начинаем регистрацию
Напиши следующим сообщением свою фамилию, имя и номер комнаты
Напирмер: Павел Пилип 418
              '''
    st['register'] = True
  else:
    message = '''
Изменяем данные
Напиши следующим сообщением свою фамилию, имя и номер комнаты
Напирмер: Антон Кожевников 418
              '''
    st['register'] = True

  return message, keyboard


registration_command = command_system.Command()

registration_command.keys = ['зарегистрироваться', 'обновить данные']
registration_command.description = 'Кнопка с регистрацией'
registration_command.process = registration
