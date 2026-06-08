def chatbot():
    print("Welcome to Basic Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Heyy!")

        elif user == "how are you":
            print("Bot: I'm good, thanks!")

        elif user == "bye":
            print("Bot:bye!")
            break

        else:
            print("Bot: Sorry, I don't got you.")

chatbot()