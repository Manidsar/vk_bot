import command_system


def commander(id):
    message = '''Ого а тут находится текст про нашего коменданта общежития'''
    keyboard = False
    return message, keyboard


commander_command = command_system.Command()

commander_command.keys = ['комендант']
commander_command.description = 'Биография коменданта'
commander_command.process = commander
