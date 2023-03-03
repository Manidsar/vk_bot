import command_system


def studsovet():
    message = '''
            Тут будет большой и длинный текст про студсовет, который я хочу получить
            '''
    return message


studsovet_command = command_system.Command()

studsovet_command.keys = ['студсовет']
studsovet_command.description = 'Расскажу тебе о студсовете'
studsovet_command.process = studsovet
