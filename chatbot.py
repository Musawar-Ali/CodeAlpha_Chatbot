#!/usr/bin/env python3
"""
chatbot.py
A simple rule-based chatbot for internship project.

Features:
- Responds to greetings, feelings, farewells
- Tells jokes when asked
- Case-insensitive input
- Exits when user types "bye"
- Saves transcript to a text file (optional)

Author: Musawar Ali
"""

import datetime
import random

RESPONSES = {
    "hello": "Hi there! 👋",
    "hi": "Hello! How are you?",
    "hey": "Hey! Nice to see you.",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "how are you doing": "I'm doing well, thank you for asking!", # Added response for "how are you doing"
    "i'm fine": "Glad to hear that! 😃",
    "good": "Awesome! Keep it up.",
    "what's up": "nothing much, what's up with you?", # Changed key to lowercase
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "bye": "Goodbye! Have a great day 🌟",
    "ok": "Alright! 👍"
}

# 🔧 New: joke list
JOKES = [
    "Why don’t skeletons fight each other? Because they don’t have the guts!",
    "Why did the computer go to the doctor? Because it caught a virus!",
    "I told my computer I needed a break… and it said 'No problem, I’ll go to sleep!'",
    "Why was the math book sad? Because it had too many problems.",
    "Why don’t programmers like nature? Too many bugs."
]

def tell_jokes():
    """Joke loop: keep asking until user says no, without repeating jokes"""
    available_jokes = list(JOKES)  # Create a mutable copy
    if not available_jokes:
        print("Bot: I've told you all the jokes I know! 😅")
        return

    while available_jokes:
        joke = random.choice(available_jokes)
        print("Bot:", joke)
        available_jokes.remove(joke)  # Remove the told joke

        if not available_jokes:
            print("Bot: That's all the jokes I have for now! 😅")
            break

        # In Google Colab, input() will display a prompt below the cell.
        # You need to type your response there and press Enter.
        # To stop the execution, you can click the square stop button next to the cell.
        choice = input("Bot: Wanna hear another one? (yes/no) ").strip().lower()
        if choice != "yes":
            print("Bot: Okay, no more jokes for now 😅")
            break


def chatbot(save_log=False, logfile="chat_log.txt"):
    print("🤖 Simple Chatbot: type 'bye' to end the chat.")
    log = []
    while True:
        # In Google Colab, input() will display a prompt below the cell.
        # You need to type your response there and press Enter.
        # To stop the execution, you can click the square stop button next to the cell.
        user = input("You: ").strip().lower() # Added .strip() here
        if not user:
            continue

        # 🔧 special handling for jokes
        if "joke" in user:
            tell_jokes()
            reply = "(That was fun 🤭)"
        else:
            reply = RESPONSES.get(user, "I'm not sure how to respond to that.")
            print("Bot:", reply)

        # log conversation
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log.append(f"[{timestamp}] You: {user}
[{timestamp}] Bot: {reply}
")

        if user == "bye":
            break

    if save_log and log:
        with open(logfile, "w", encoding="utf-8") as f:
            f.writelines(log)
        print(f"
(Chat transcript saved to {logfile})")

if __name__ == "__main__":
    chatbot(save_log=True)
