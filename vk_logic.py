import vk_api
import random
import settings
import keyboards

# Вся логика получения и отправки сообщений

vk_session = vk_api.VkApi(token=settings.token)


def send_some_msg(id, some_text, keyboard):
    if keyboard:
        # keyboard_base.add_callback_button(
        #                             'Сообщить о проблеме',
        #                              color='positive',
        #                              payload={"type": "open_link", "link": 'https://forms.gle/ojeK7QU2aYzuUZq27'}
        #                              )

        vk_session.method("messages.send", {"user_id": id, "message": some_text,
                                            "random_id": 0,
                                            "keyboard": keyboards.base()})
    else:
        vk_session.method("messages.send", {"user_id": id, "message": some_text, "random_id": 0})

# keyboard_2 = VkKeyboard(one_time=True)
# # кнопка переключения назад, на 1ое меню.
# keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})
