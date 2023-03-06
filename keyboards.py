from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton


def base():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Оплата общежития', color=VkKeyboardColor.POSITIVE)
    # keyboard_base.add_callback_button(label='Добавить красного ', color=VkKeyboardColor.PRIMARY,
    #                                   payload={"type": "pay_dormitory"})

    keyboard.add_line()

    keyboard.add_button('Графики работ', color='secondary')
    keyboard.add_button('Комендант', color=VkKeyboardColor.SECONDARY)

    keyboard.add_line()
    keyboard.add_button('Студсовет', color=VkKeyboardColor.PRIMARY, payload={'type': '1'})
    keyboard.add_button('Сообщить о проблеме', color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button('Отключить бота', color=VkKeyboardColor.POSITIVE)
    return keyboard.get_keyboard()