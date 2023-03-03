import command_system


def problem():
    message = 'Ля ты крыса...'
    return message


problem_command = command_system.Command()

problem_command.keys = ['соообщить о проблеме']
problem_command.description = 'Ля ты крыса'
problem_command.process = problem
