class Bot:
    name = "Harley"
    emotions = {
        "positive": ["surprised", "excited",  # :["what to say when here"]????
                     "proud", "grateful",
                     "impressed", "hopeful",
                     "confident", "joyful",
                     "content", "caring",
                     "trusting", "faithful",
                     "prepared", "sentimental",
                     "anticipating"],
        "negative": ["angry", "sad",
                     "annoyed", "lonely",
                     "afraid", "terrified",
                     "guilty", 'disgusted',
                     "furious", "anxious",
                     "nostalgic", "disappointed",
                     "jealous", "devastated",
                     'embarrassed', "ashamed",
                     "apprehensive"
                     ]
    }
    chat = {}

    def save_chat(self, user_input):
        self.chat[user_input] = self.speak(self, user_input)
        return self.chat[user_input]

    def speak(self, user_input):
        words = user_input.split()
        positive_words = []
        negative_words = []
        neutral_words = []
        print(words)
        for word in words:
            if word in self.emotions["positive"]:
                positive_words.append(word)
            elif word in self.emotions["negative"]:
                negative_words.append(word)
            else:
                neutral_words.append(word)
        response = "you got "+str(len(positive_words)) + " pos words and " + str(len(negative_words)) + " neg words"
        # put a response for every word or smth
        print(positive_words, negative_words)
        # TODO: to see how many positive/... words are (firstly) to get a positive or negative response
        #  then see what words are and if there are any expressions or special words (start with big letter)
        #  get simple conversational things, like a list of I am, you are etc
        #  a list of basic conversations for the beginning and the end of the conversation
        #  get a strategy of how to respond with empathy - get a list of examples of a daily conv
        #  be careful with , and .
        return response
