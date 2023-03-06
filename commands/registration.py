import command_system


def registration():
    message = '''
              Начинаем регистрацию, сюда нужно будет далее добавть кнопки какие-то 
              '''
    return message


registration_command = command_system.Command()

registration_command.keys = ['графики работ']
registration_command.description = 'Расскажу тебе о расписании'
registration_command.process = registration
