class Bot:
    name = "Harley"
    person_of_interest = ""
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

    def save_chat(self, user_input):
        self.chat[user_input] = self.speak(self, user_input)
        return self.chat[user_input]

    def speak(self, user_input):
        words = user_input.split()
        positive_words = []
        negative_words = []
        neutral_words = []
        print(words)
        response = ""
        if "your" in words and "name" in words:
            response = "I'm Harley, glad to meet you! What is your name?"
        elif "i'm" in words or "i am" in words:
            self.person_of_interest = words[-1]
        elif "my" in words and "name" in words:
            self.person_of_interest = words[-1]
        else:
            for word in words:
                if word in self.emotions["positive"]:
                    positive_words.append(word)
                elif word in self.emotions["negative"]:
                    negative_words.append(word)
                elif word in self.emotions["greetings"]:
                    response = "Hello there, how are you today?"
                    break
                else:
                    # neutral_words.append(word)
                    response = "I'm sorry, I did not quite understand that."
            # response = "you got " + str(len(positive_words)) + " pos words and " + str(len(negative_words)) + " neg words"
            # put a response for every word or smth
        print(positive_words, negative_words)
        if len(positive_words) > len(negative_words):
            pass
        # TODO: to see how many positive/... words are (firstly) to get a positive or negative response
        #  then see what words are and if there are any expressions or special words (start with big letter)
        #  get simple conversational things, like a list of I am, you are etc
        #  a list of basic conversations for the beginning and the end of the conversation
        #  get a strategy of how to respond with empathy - get a list of examples of a daily conv
        #  be careful with , and .
        return response
