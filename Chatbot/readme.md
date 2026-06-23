# Basic Chatbot

## Description
This project is a simple rule-based chatbot built using Python. The chatbot responds to specific user inputs with predefined replies. It demonstrates the use of functions, loops, conditional statements (`if-elif`), and input/output operations.

## Features
- Responds to `"hello"` with `"Hi!"`
- Responds to `"how are you"` with `"I'm fine, thanks!"`
- Responds to `"bye"` with `"Goodbye!"` and exits the program
- Handles unknown inputs with a default response

## Requirements
- Python 3.x

## Code

```python
def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye!")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand.")

# Run the chatbot
chatbot()