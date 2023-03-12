from replit import db

# Тут будем объявлять нужные данные, чтобы названия столбцов были четкие.
# class Student(db):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     surname = db.Column(db.String(100))
#     room = db.Column(db.Integer)
#     debt = db.Column(db.Integer)
#     admin = db.Column(db.Boolean(create_constraint=False))
#     register = db.Column(db.Boolean(create_constraint=False))
#     clown = db.Column(db.Boolean(create_constraint=False))
#     problem = db.Column(db.Boolean(create_constraint=False))
#     give_check = db.Column(db.Boolean(create_constraint=False))
#     status = db.Column(db.Boolean(create_constraint=False))
#     count = db.Column(db.Integer)

# def __repr__(self):
#     # данные, которые выдает модель при обращении к объекту
#     # return {
#     #         'id': self.id,
#     #         'name': self.name,
#     #         'surname': self.surname,
#     #         'room': self.room,
#     #         'dept': self.dept,
#     #         'admin': self.admin,
#     #         'register': self.register,
#     #         'clown': self.clown,
#     #         'problem': self.problem,
#     #         'give_check': self.give_check,
#     #         'status': self.status,
#     #         }
#     return f'<Student {self.name}>'

# def get_status(id_s):
#   base = db[id_s]
#   return base

# Функция, которая изменяет имя и фамилию или меняет их принимает id и сообщение, которое нужно обработать.
# Возвращает соообщение об успешной регистрации или ошибке


def start_register(id):
  db[int(id)] = {
    'name': False,
    'surname': False,
    'room': False,
    'debt': 0,
    'admin': False,
    'register': False,
    'clown': False,
    'problem': False,
    'give_check': False,
    'status': False,
  }


def registration(id, message):
  # base = get_status(id)
  try:
    name, surname, room = message.split()

    room = int(room)
    if 201 <= room <= 232 or 300 <= room <= 332 or 400 <= room <= 430 or 500 <= room <= 532 or room in [
        235, 335, 435, 535
    ]:
      print(f'This is my id:{db[id]}')
      db[id]['name'] = name
      db[id]['surname'] = surname
      db[id]['room'] = room
      db[id]['register'] = False
    else:
      return ValueError  # 'Ты шо дурачек? \nНапиши данные, в формате Александр Смирнов 228'
  except ValueError:
    return 'Ты шо дурачек?'

  return 'Данные успешно обновлены'
