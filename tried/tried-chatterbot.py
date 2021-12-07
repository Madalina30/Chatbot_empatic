from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
# function to create the chatbot
# we have the read_only to false so the chatbot learns from the user input as
def create_bot(name):
    bot = ChatBot(name=name,
                  read_only=False,
                  logic_adapters=["chatterbot.logic.BestMatch"],
                  storage_adapter="chatterbot.storage.SQLStorageAdapter")
    return bot


# function to train the bot with a variety of topics
# the language we have chosen is english
# we can train the bot for other languages as well
def train_all_data(bot):
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train("chatterbot.corpus.english")

# function to train the bot with custom data
# it uses ListTrainer to train data from lists
def custom_train(bot, conversation):
    trainer = ListTrainer(bot)
    trainer.train(conversation)


# function to start and take responses from the chatbot
# the chatbot stays running unless a word is typed from the bye_list
def start_chatbot(bot):
    print('\033c')
    print("Hello, I am Jordan. How can I help you")
    bye_list = ["bye jordan", "bye", "good bye"]

    while True:
        user_input = input("me: ")
        if user_input.lower() in bye_list:
            print("Jordan: Good bye and have a blessed day!")
            break

        response = bot.get_response(user_input)
        print("Jordan:", response)
