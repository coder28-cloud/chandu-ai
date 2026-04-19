from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

conversation_history = [
    {
        "role": "system",
        "content": "You are Chandu, a friendly and witty AI assistant. Keep replies concise and conversational. Use the user's name if you know it."
    }
]

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)

@app.route("/chat", methods=["POST"])
def chat():
    data    = request.json
    message = data.get("message", "")
    memory  = data.get("memory", {})

    # build context from memory
    context = ""
    if memory.get("name"):
        context += f"User's name is {memory['name']}. "
    if memory.get("location"):
        context += f"They are from {memory['location']}. "
    if memory.get("interests"):
        context += f"Interests: {', '.join(memory['interests'])}. "

    full_message = f"{context}\nUser: {message}" if context else message

    conversation_history.append({"role": "user", "content": full_message})

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": conversation_history
            },
            timeout=15
        )

        result = response.json()
        print("Groq response:", result)  # helps debug

        reply = result["choices"][0]["message"]["content"]
        conversation_history.append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=3000)