import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from config import *
from refbot import RefBot
import requests


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, GROUP_ID)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            bot = RefBot(vk, event.obj.message['from_id'], event.obj.message)
            try:
                bot.analyse_message()
            except Exception as e:
                print(e)
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message='Что-то пошло не так, попробуйте еще раз',
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
