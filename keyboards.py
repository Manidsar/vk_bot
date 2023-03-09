from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton


def base():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Зарегистрироваться', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Оплата общежития', color=VkKeyboardColor.POSITIVE,
    payload={"type":"pay"})


    keyboard.add_line()
    keyboard.add_button('Графики работ', color='secondary')
    keyboard.add_button('Комендант', color=VkKeyboardColor.SECONDARY)

    keyboard.add_line()
    keyboard.add_button('Студсовет', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Сообщить о проблеме', color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button('Вопросы рекламы', color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()

def pay():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Отправить чек', color=VkKeyboardColor.SECONDARY)

    keyboard.add_line()
    keyboard.add_button('Посмотреть свой долг', color=VkKeyboardColor.SECONDARY)

    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.SECONDARY,
    payload={"type":"base"})
    return keyboard.get_keyboard()

def base_reg():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Обновить данные', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Оплата общежития', color=VkKeyboardColor.POSITIVE,
    payload={"type":"pay"})


    keyboard.add_line()
    keyboard.add_button('Графики работ', color='secondary')
    keyboard.add_button('Комендант', color=VkKeyboardColor.SECONDARY)

    keyboard.add_line()
    keyboard.add_button('Студсовет', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Сообщить о проблеме', color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button('Вопросы рекламы', color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()

