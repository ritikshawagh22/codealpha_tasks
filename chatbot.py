import datetime

def chatbot():
    print("🤖 ChatBot: Hello! I'm your virtual assistant.")
    print("Type 'bye' to end the chat.\n")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hey"]:
        print("🤖 ChatBot: Hello! How can I help you today?")

        elif "how are you" in user:
            print("🤖 ChatBot: I'm doing great! Thanks for asking.")

        elif "your name" in user:
            print("🤖 ChatBot: My name is ChatBot.")

        elif "who created you" in user:
            print("🤖 ChatBot: I was created using Python programming.")

        elif "time" in user:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("🤖 ChatBot: The current time is", current_time)

        elif "date" in user:
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print("🤖 ChatBot: Today's date is", current_date)

        elif "joke" in user:
            print("🤖 ChatBot: Why do Python programmers wear glasses? Because they can't C!")

        elif "thank you" in user or "thanks" in user:
            print("🤖 ChatBot: You're welcome!")

        elif "help" in user:
            print("🤖 ChatBot: I can tell the time, date, jokes, and answer simple questions.")

        elif user in ["bye", "exit", "quit"]:
            print("🤖 ChatBot: Goodbye! Have a wonderful day.")
            break

        else:
            print("🤖 ChatBot: Sorry, I don't understand that. Can you rephrase?")

chatbot()