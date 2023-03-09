import command_system
import keyboards


def hello(st):
    message = 'Привет, друг!\nЯ новый чат-бот для общежития 14Б.'
    keyboard = keyboards.base()
    return message, keyboard


hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте', 'салам', 'салам аллейкум', 'начать', 'начало']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello
