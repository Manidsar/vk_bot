import command_system
import keyboards

def back(st):
    message = 'Возвращаюсь в главное меню'
    if st.name == None:
        keyboard = keyboards.base()
    else:
        keyboard = keyboards.base_reg()
    return message, keyboard


back_command = command_system.Command()

back_command.keys = ['назад']
back_command.description = 'Возврат назад'
back_command.process = back
