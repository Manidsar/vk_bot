
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


def get_status(id_s):
    # Потом идет обращение через точечную нотацию
    # print(db.session.query(Student).filter_by(id=id_s).first().name)
    base = db.session.query(Student).filter_by(id=id_s).first()
    return base
    # None


    # print(db.session.query(Student.id, Student.name).all())
    # [(137650711, None), (251669630, None), (284583957, None)]

    # Функция, которая изменяет имя и фамилию или меняет их принимает id и сообщение, которое нужно обработать.
    # Возвращает соообщение об успешной регистрации или ошибке

def start_register(id):
  db[id] = {
    'name': False
  }
  
def registration(id, message):
    base = get_status(id)
    try:
        name, surname, room = message.split()
        base.name = name
        base.surname = surname
        base.room = int(room)
        room = int(room)
        if 201 <= room <= 232 or 300 <= room <= 332 or 400 <= room <= 430 or 500 <= room <= 532 or room in [235, 335, 435, 535]:
            base.register = False
            db.session.add(base)
            db.session.commit()
        else:
            return ValueError # 'Ты шо дурачек? \nНапиши данные, в формате Александр Смирнов 228'
    except ValueError:
        return 'Ты шо дурачек?'

    return 'Данные успешно обновлены'


