import command_system


def sched():
    message = '''
              Тут вы можете видеть полное расписание всех отделов в нашей общеге
              зал
              учебная комната и еще если что-то остается  
              '''
    return message


sched_command = command_system.Command()

sched_command.keys = ['графики работ']
sched_command.description = 'Расскажу тебе о расписании'
sched_command.process = sched
