import Bot
from Bot import *


def create_empathic_bot():
    bot = Bot
    return bot


def start_chatbot(bot):
    set_name = 0
    print("Harley: Hello, I am Harley. What is your name?")
    bye_list = ["bye harley", "bye", "good bye"]
    while True:
        user_input = input(">>User: ")
        if user_input.lower() in bye_list:
            print("Harley: Good bye and have a blessed day!")
            break
        response = bot.save_chat(bot, user_input)
        print(response)
