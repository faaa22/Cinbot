from flask import Flask, render_template, request, jsonify
from ollama import chat
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chatbot():
    user_message = request.form.get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "Tolong isi pesannya dulu ya 😅"})

    time.sleep(0.5)

    try:
        response = chat(
            model="mistral",
            messages=[
                {"role": "system", "content": "Kamu adalah Cinbot 🐰, chatbot yang ramah dan lucu, menjawab dengan bahasa Indonesia."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response["message"]["content"].strip()
    except Exception as e:
        reply = f"Maaf yaa, Cinbot lagi lelah 😢 ({e})"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
