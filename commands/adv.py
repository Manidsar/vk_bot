import command_system
import keyboards

def adv(st):
    message = 'Сказать что-то про рекламу в нашей группе общежития или тут можно добавить про отряды и про плакаты, хз'
    keyboard = False
    return message, keyboard


adv_command = command_system.Command()

adv_command.keys = ['вопросы рекламы']
adv_command.description = 'Тут посылают нахер все рекламные предложения'
adv_command.process = adv