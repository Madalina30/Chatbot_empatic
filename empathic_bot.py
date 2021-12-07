import Bot
from Bot import *


def create_empathic_bot():
    bot = Bot
    print(bot.name)
    return bot


def start_chatbot(bot):
    print("Hello, I am Harley. How can I help you today?")
    bye_list = ["bye harley", "bye", "good bye"]

    while True:
        user_input = input(">>User: ")
        if user_input.lower() in bye_list:
            print("Jordan: Good bye and have a blessed day!")
            break
        response = bot.save_chat(bot, user_input)
        print("Jordan:", response)
