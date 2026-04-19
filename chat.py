import json
import random
import difflib
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

# -------- Load intents --------
with open("responses.json") as file:
    data = json.load(file)

# -------- Load memory --------
try:
    with open("memory.json") as f:
        memory = json.load(f)
except:
    memory = {}

# -------- Save memory function --------
def save_memory():
    with open("memory.json", "w") as f:
        json.dump(memory, f)

# -------- AI function --------
def ask_ai(prompt):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=data, timeout=10)
        result = response.json()

        if "choices" in result:
          return result["choices"][0]["message"]["content"]
        else:
          print("DEBUG ERROR RESPONSE:", result)
          return "AI error 😅"

    except Exception as e:
        print("Error:", e)
        return "AI not responding 😅"

# -------- Chat loop --------
while True:
    user_input = input("You: ").lower()
    # print("DEBUG INPUT:", user_input)

    # -------- Exit --------
    if user_input == "quit":
        print("Chandu: Goodbye! 👋")
        break

    # -------- Store name --------
    if "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        memory["name"] = name
        save_memory()
        print(f"Chandu: Nice to meet you {name}!")
        continue

    # -------- Store location --------
    if "i live in" in user_input:
        location = user_input.replace("i live in", "").strip().title()
        memory["location"] = location
        save_memory()
        print(f"Chandu: {location} is a beautiful place!")
        continue

    elif "i am from" in user_input:
        location = user_input.replace("i am from", "").strip().title()
        memory["location"] = location
        save_memory()
        print(f"Chandu: {location} is a beautiful place!")
        continue

    # -------- Recall name --------
    if "what is my name" in user_input:
        if "name" in memory:
            print(f"Chandu: Your name is {memory['name']}")
        else:
            print("Chandu: I don't know your name yet 😅")
        continue

    # -------- Matching --------
    best_match = None
    best_score = 0

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            score = difflib.SequenceMatcher(None, user_input, pattern).ratio()

            if score > best_score:
                best_score = score
                best_match = intent

    # -------- Response --------
    if best_score > 0.85:
        response = random.choice(best_match["responses"])

        if "name" in memory:
            response = f"{memory['name']}, {response}"

        print("Chandu:", response)

    else:
        # print("DEBUG: going to AI")

        ai_response = ask_ai(user_input)

        if not ai_response:
            ai_response = "Something went wrong 😅"

        if "name" in memory:
            ai_response = f"{memory['name']}, here’s what I think:\n{ai_response}"

        print("Chandu:", ai_response)