import vk_api
import random
import settings

# Вся логика получения и отправки сообщений
# Тут будет отправка проблем в группы и Саше
# И отправка анекдотов
vk_session = vk_api.VkApi(token=settings.token)


def send_some_msg(id, some_text, keyboard):
    print(some_text)
    if keyboard:
        vk_session.method("messages.send", {"user_id": id, "message": some_text,
                                            "random_id": random.randrange(1, 1000000),
                                            "keyboard": keyboard})
                                            # "keyboard": keyboards.base(key)})

    else:

        vk_session.method("messages.send", {"user_id": id, "message": some_text, "random_id": 0})

# keyboard_2 = VkKeyboard(one_time=True)
# # кнопка переключения назад, на 1ое меню.
# keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})
