print("Hello! I am your Rule-Based Chatbot.")
print("Type 'exit' to end the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi there! How can I help you?")
    
    elif user_input == "how are you":
        print("Bot: I'm just a program, but I'm doing great!")
    
    elif user_input == "your name":
        print("Bot: I am a simple rule-based chatbot.")
    
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
    
    elif user_input == "exit":
        print("Bot: Chat ended.")
        break
    
    else:
        print("Bot: Sorry, I don't understand that.")
