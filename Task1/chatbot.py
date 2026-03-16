# Simple Rule-Based Chatbot

print("Chatbot: Hello! I am a simple chatbot.")
print("Type 'bye' to exit the chat.")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Chatbot: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Chatbot: I am doing great. Thanks for asking!")

    elif "name" in user:
        print("Chatbot: My name is CodSoft Chatbot.")

    elif "creator" in user or "who made you" in user:
        print("Chatbot: I was created as part of a CodSoft internship project.")

    elif "time" in user:
        import datetime
        print("Chatbot: Current time is", datetime.datetime.now().strftime("%H:%M:%S"))

    elif "date" in user:
        import datetime
        print("Chatbot: Today's date is", datetime.date.today())

    elif "help" in user:
        print("Chatbot: You can ask me about my name, time, date, or say hello.")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I didn't understand that.")
