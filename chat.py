import nltk
from nltk.chat.util import Chat, reflections

# Read patterns and responses from the single text file
def read_patterns_responses(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        patterns, responses = [], []
        for line in lines:
            line = line.strip()
            if "==" in line:
                pattern, response = line.split("==")
                patterns.append(pattern)
                responses.append(eval(response))  # Using eval to parse the response as a list
            else:
                print(f"Skipping invalid line: {line}")
        return patterns, responses

def update_patterns_responses(filename, new_pattern, new_response):
    patterns, responses = read_patterns_responses(filename)
    if new_pattern not in patterns:
        with open(filename, 'a') as file:
            file.write("\n" + new_pattern + "==" + str(new_response))

chatbot_data_file = "chatbot_data.txt"

patterns, responses = read_patterns_responses(chatbot_data_file)

# Pair patterns and responses
pairs = list(zip(patterns, responses))

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hello! How can I assist you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot.respond(user_input)
    print("Chatbot:", response)

    if response == chatbot.respond("I don't know the answer."):
        new_response = input("Chatbot: I'm not sure about that. Please provide a response: ")
        update_patterns_responses(chatbot_data_file, user_input, [new_response])
        print("Chatbot: Thanks for teaching me!")