import command_system
import time
import keyboards

def pay_dorm(id):
    message = 'Переходим в раздел (хз, но мне кажется, тут нужно еще что-то написать)'
    keyboard = keyboards.pay()
    return message, keyboard


pay_dorm_command = command_system.Command()

pay_dorm_command.keys = ['оплата общежития']
pay_dorm_command.description = 'Расскажу тебе что где и как по оплате общежития'
pay_dorm_command.process = pay_dorm
