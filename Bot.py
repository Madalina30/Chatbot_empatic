import random

import nltk
import re, string

from nltk import WordNetLemmatizer
from nltk.corpus import stopwords


class Bot:
    name = "Harley"
    person_of_interest = ""
    books = {
        "sad": [
            "I would recommend you ‘Everything happens for a reason’ by Kate Bowler.Read a little resume about it.You will love it!",
            "I would really like for you to read ‘The book thief’ by Markus Zusak if you haven’t done it already! The action happens in a time of war in Germany, when bombs stroke when you would expect the least.It is about a young girl that really likes to read, but does not have the possibility to buy them.She finds a way to read the books, alongside with a young boy.You need to read it to find out more, I don’t want to spoiler it!",
            "You need to read ‘Wonder’ by R.J.Palacio! It is a story told from the perspective of a ten-year-old with jarring facial anomalies and his various family members and friends."],
        "romance": [
            "‘To all the boys I loved before’ by Jenny Han is a beautiful romance book! Read it before seeing the movie!",
            "‘After’ by Anna Todd (4 books actually) is a really nice book that first appeared on wattpad, the most popular platform where you can read tons of books, paid or not, made by a lot of people of different ages and nationalities.",
            "‘The hating game’ by Sally Thorne is about 2 co - workers that have a rivalry as bitter as they come, especially as they compete for the same promotion.At least, it starts out that way!"],
        "mystery": [
            "‘Gone girl’ by Gillian Flyn is the best mystery book. It is about a wife that has gone missing and her husband that starts searching for her by looking through their anniversary gift messages.If I haven’t convinced you, the husband also has a mistress! Enjoy!",
            "‘Da vinci code’ by Dan Brown is a must read mystery book.Discover it!",
            "I would recommend you ‘Big little lies’ by Liane Moriarty.It is about a single mom that sends her son to kindergarten and befriends 2 mothers.Along with their friendships is an array of family dramas, from ex- or abusive husbands of dark pasts.More you will discover by reading it!"],
        "horror": ["‘Bird box’ by Josh Maler is a very good horror book! Read it and you won’t regret it!",
                   "‘You need to read ‘The shinning’ by Stephen King! It will the skin out of you!"],
        "fantasy": [
            "I would really recommend you the books ‘Witch and wizard’ by James Patterson.It is a wonderful collection that will send you in a different world, where magic gets punished and you will discover the life of magicians",
            "‘Beautiful creatures’ by Kami Garcia is a romance fantasy with lots of adventures of a beginning witch that is haunted by an old curse, as it was supposed to be.As it is a 5-book-series, the story changes as you advance in the book and the magic gets stronger, but the love too."]
    }
    movies = {
        "sad": [
            "‘The boy in stripped pants’ is a movie based on the book with the same name that will surely make you cry… It sure wanted me to cry and I am just an AI system!",
            "‘The theory of everything’ is an amazing, but sad movie.It is about Stephen Hawking and I think the name just says it all, if you heard about his story."],
        "romance": [
            "‘Love and monsters’ is a romantic sci-fi movie about a boy that searches for his lover in a world with a lot of dangerous lovers! He won’t do it alone, as some people he meets help him in his journey",
            "‘Space between us’ is truly a wonderful romantic movie about a boy that lives in a space sheep that talks to an earth girl and falls in love with her.He tries to be close to her, but when he does arrive on Earth, he almost dies.See more by watching the movie!"
        ],
        "mystery": [
            "‘Escape room’ (2019, 2021) is a horror-mystery movie that makes you enter in an escape room game among the players and live as they do and try to get out of there alive",
            "I would recommend you ‘Murder on the Orient Express’ from 2017 if you love a good kinda Sherlock Holmes movie! The name says all the description that is needed!"],
        "horror": [
            "‘The conjuring’ is the best horror movie - series of all times! I won’t tell you what are they about, just that everywhere is at least a ghost!",
            "‘The curse of La Llorona’ is an amazing horror movie, that tells the story of La Llorona and the curse that she put upon her.",
            "‘Before I wake’ is a lighter horror movie, with a very nice story of a young boy whose dreams become reality"],
        "fantasy": [
            "Even if you are not a kid anymore, ‘Nightbook’ is a great fantasy movie that will make you not take your eyes of it",
            "‘Avengers’ and all the other movies in this series are really worth a try as they welcome you in a world where all Marvel superheroes work together against a worldwide threat"
        ]
    }
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
                           "You are my favorite person, I will never do something to disappoint you!"],
        "jealous": ["", ],
        "lonely": ["I am here for you! You will never be lonely!"],
        "sentimental": ["It is a natural thing for a person, being sentimental!",
                        "You don't need to be afraid by it, it is something normal!"],
        "anxious": ["You do not need to feel like this!", "We need to do something about it!"],
        "grateful": ["That is very good!"],
        "afraid": ["You don't need to be afraid!", "I am here for you!", "You really don't need to be afraid about x!"],
        "confident": ["Being confident is the right way to be! It will help you be successful!",
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
