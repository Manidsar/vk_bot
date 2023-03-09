import command_system


def studsovet(st):
    message = '''
            Тут будет большой и длинный текст про студсовет, который я хочу получить
            '''
    keyboard = False
    return message, keyboard


studsovet_command = command_system.Command()

studsovet_command.keys = ['студсовет']
studsovet_command.description = 'Расскажу тебе о студсовете'
studsovet_command.process = studsovet
