import random

import nltk
import re, string

from nltk import WordNetLemmatizer
from nltk.corpus import stopwords


class Bot:
    name = "Harley"
    person_of_interest = ""
    predefined_answers = {
        "sad": ["You need to be cheered up!", ],
        "bad mood": ["Maybe I can help you turn your bad mood into a good one!", ],
        "here for me": [
            " I will be here for you, as there can be jokes that can trigger even bad emotions for you. We will try one kind of meditation. Think that you are in the clouds where it is all quite and the only thing that you can hear are some birds that are flying close to you. From there, you can see some kind of paradise with candies, palms, beaches and also hear from far the waves that are crushing. You are flying to that paradise as the clouds are taking you there and you can touch the sea and the warm sand with your feets. Beside you, there is a sand castle the size of your home and you explore it. How do you feel now?", ],
        "joke": ["", ],
        "thank": ["It is my pleasure to help you!", "You're welcome!", "You can count anytime for me!",
                  "No need to thank me, it is my job!", ],
        "happy": ["I am glad you feel this way!", "You make me happy!", ],
        "will not judge": ["I will never judge you!",
                           "You are my favorite person, I will never do something to disapoint you!"],
        "jealous": ["", ],
        "lonely": ["I am here for you! You will never be lonely!"],
        "sentimental": ["It is a natural thing for a person, being sentimental!",
                        "You don't need to be afraid by it, it is something normal!"],
        "anxious": ["You do not need to feel like this!", "We need to do something about it!"],
        "grateful": ["That is very good!"],
        "afraid": ["You don't need to be afraid!", "I am here for you!", "You really don't need to be afraid about x!"],
        "confident": ["Being confident is the right way to be! It will help you be successfull!",
                      "That is no other way to feel than confident! It will help you everytime you feel like you can't do something!"],
        "impressed": [""],
        "embarrassed": ["It happens! You can get through this and I will be here for you!"],
        "angry": ["Being angry is not a good thing! You need to start thinking positive!",
                  "Anger will make you do bad things. Try to think at something positive!"]
    }
    emotions = {
        "positive": ["surprised", "excited",  # :["what to say when here"]????
                     "proud", "grateful",
                     "impressed", "hopeful",
                     "confident", "joyful",
                     "content", "caring",
                     "trusting", "faithful",
                     "prepared", "sentimental",
                     "anticipating", "happy"],
        "negative": ["angry", "sad",
                     "annoyed", "lonely",
                     "afraid", "terrified",
                     "guilty", 'disgusted',
                     "furious", "anxious",
                     "nostalgic", "disappointed",
                     "jealous", "devastated",
                     'embarrassed', "ashamed",
                     "apprehensive"
                     ],
        "greetings": ["Hi", "Hello there", "hi", "hello", "Hello", "hi there", "greetings", "Greetings"],
        "personification": ["i'm", "i am"]
    }

    chat = {}

    def lemmatizer(text):
        text = re.sub('[' + string.punctuation + ']', '', text)
        text = re.sub(r"[-()\"#/@’;:<>{}`+=~|.!?,]", '', text)
        text = text.lower().split()

        stops = set(stopwords.words("english"))
        text = [word for word in text if word not in stops]
        text = " ".join(text)
        text = re.sub(r'[^a-zA-Z\s]', u'', text, flags=re.UNICODE)

        text = text.split()
        lemm = WordNetLemmatizer()
        lemmatized = [lemm.lemmatize(word) for word in text if len(word) > 2]
        text = " ".join(lemmatized)

        return text

    def save_chat(self, user_input):
        self.chat[user_input] = self.speak(self, user_input)
        return self.chat[user_input]

    def speak(self, user_input):
        words = nltk.word_tokenize(user_input)
        print(words)
        pos_tag_words = nltk.pos_tag(words)
        if not self.person_of_interest:
            if len(pos_tag_words) == 1:
                self.person_of_interest = pos_tag_words[0]
            else:
                for word in pos_tag_words:
                    if "JJ" in word[1]:
                        self.person_of_interest = word[0]
                        return "Hi " + self.person_of_interest + "! How may I help you today?"
        # positive_words = []
        # negative_words = []
        # neutral_words = []
        # print(words)
        response = ""
        for word in self.predefined_answers:
            # print(word)
            if word in user_input:
                # print("ok")
                rnd = random.randint(0, len(self.predefined_answers[word]) - 1)
                response += self.predefined_answers[word][rnd] + " "

        # if "your" in words and "name" in words:
        #     response = "I'm Harley, glad to meet you! What is your name?"
        # elif "i'm" in words or "i am" in words:
        #     self.person_of_interest = words[-1]
        # elif "my" in words and "name" in words:
        #     self.person_of_interest = words[-1]
        #     response = "Hi " + self.person_of_interest + "!"
        # else:
        #     for word in words:
        #         if word in self.emotions["positive"]:
        #             positive_words.append(word)
        #         elif word in self.emotions["negative"]:
        #             negative_words.append(word)
        #         elif word in self.emotions["greetings"]:
        #             response = "Hello there, how are you today?"
        #             break
        #         else:
        #             # neutral_words.append(word)
        #             response = "I'm sorry, I did not quite understand that."
        #     # response = "you got " + str(len(positive_words)) + " pos words and " + str(len(negative_words)) + " neg words"
        #     # put a response for every word or smth
        # print(positive_words, negative_words)
        # if len(positive_words) > len(negative_words):
        #     pass
        # # TODO: to see how many positive/... words are (firstly) to get a positive or negative response
        # #  then see what words are and if there are any expressions or special words (start with big letter)
        # #  get simple conversational things, like a list of I am, you are etc
        # #  a list of basic conversations for the beginning and the end of the conversation
        # #  get a strategy of how to respond with empathy - get a list of examples of a daily conv
        # #  be careful with , and .
        # return response
        return response
