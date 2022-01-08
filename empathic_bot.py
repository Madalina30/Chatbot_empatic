import Bot
from Bot import *




def create_empathic_bot():
    bot = Bot
    # print(bot.name)
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


# def trial():
#     conversational_pipeline = pipeline("conversational")
#     conv1_start = "Let's watch a movie tonight - any recommendations?"
#     conv2_start = "What's your favorite book?"
#
#     conv1 = Conversation(conv1_start)
#     conv2 = Conversation(conv2_start)
#
#     print(conversational_pipeline([conv1, conv2]))
