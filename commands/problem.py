import command_system
import time

def problem(id):
    message = 'Ля ты крыса...'
    keyboard = False
    return message, keyboard


problem_command = command_system.Command()

problem_command.keys = ['сообщить о проблеме']
problem_command.description = 'Ля ты крыса'
problem_command.process = problem
