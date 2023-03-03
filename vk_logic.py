import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton
import random
import settings

# Вся логика получения и отправки сообщений

vk_session = vk_api.VkApi(token=settings.token)


def send_some_msg(id, some_text, keyboard):
    if keyboard:

        keyboard_base = VkKeyboard(one_time=False)

        # keyboard_base.add_callback_button('Сбор чеков', color=VkKeyboardColor.POSITIVE, )

        keyboard_base.add_button('Оплата общежития', color=VkKeyboardColor.POSITIVE)
        keyboard_base.add_line()

        keyboard_base.add_button('Графики работ', color='secondary')
        keyboard_base.add_button('Комендант', color=VkKeyboardColor.SECONDARY)

        keyboard_base.add_line()  # Переход на вторую строку
        keyboard_base.add_button('Студсовет', color=VkKeyboardColor.PRIMARY, payload={'type': '1'})
        keyboard_base.add_button('Сообщить о проблеме', color=VkKeyboardColor.NEGATIVE)

        keyboard_base.add_line()  # Переход на вторую строку
        keyboard_base.add_button('Отключить бота', color=VkKeyboardColor.POSITIVE)


    # keyboard_base.add_callback_button(
    #                             'Сообщить о проблеме',
    #                              color='positive',
    #                              payload={"type": "open_link", "link": 'https://forms.gle/ojeK7QU2aYzuUZq27'}
    #                              )

    #
    # if msg == "начало":
    #     send_some_msg(id, "Hi friend!", keyboard_base.get_keyboard())
    #
    # if msg == "сообщить о проблеме":
    #     send_some_msg(id, 'Шо случилось??', keyboard_base.get_keyboard())

        vk_session.method("messages.send", {"user_id": id, "message": some_text,
                                            "random_id": 0,
                                            "keyboard": keyboard_base.get_keyboard()})
    else:
        vk_session.method("messages.send", {"user_id": id, "message": some_text, "random_id": 0})


# keyboard_2 = VkKeyboard(one_time=True)
# # кнопка переключения назад, на 1ое меню.
# keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})