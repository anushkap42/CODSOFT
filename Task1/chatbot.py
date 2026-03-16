print("Chatbot: Hello! I am a simple chatbot.")
print("Type 'bye' to exit the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hello! How can I help you?")

    elif "name" in user_input:
        print("Chatbot: I am a rule-based chatbot created for the CodSoft internship.")

    elif "how are you" in user_input:
        print("Chatbot: I am doing well, thank you!")

    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")
