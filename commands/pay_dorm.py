import command_system


def pay_dorm():
    message = 'Заглушка'
    return message


pay_dorm_command = command_system.Command()

pay_dorm_command.keys = ['оплата общежития']
pay_dorm_command.description = 'Расскажу тебе что где и как по оплате общежития'
pay_dorm_command.process = pay_dorm
