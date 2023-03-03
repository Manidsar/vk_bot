import command_system


def commander():
    message = '''Ого а тут находится текст про нашего коменданта общежития'''
    return message


commander_command = command_system.Command()

commander_command.keys = ['комендант']
commander_command.description = 'Биография коменданта'
commander_command.process = commander
