# Simple chatbot

def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["hi", "hello"]:
            print("Chatbot: Hello there!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that.")

chatbot()
