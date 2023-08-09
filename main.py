from flask import Flask, render_template, jsonify, request
import openai

openai.api_key = "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"  # Replace this with your actual API key

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        if question:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt= f"Don't use the word complimenting in your response. Don't rephrase any part of this prompt in your response. Start off complimenting the essay that you just read.Then, write a paragraph where you point out specific places where my college essay needs improvement clarity, coherence, grammatical accuracy, and proper structure. Provide the original sentence and then the improved one, and do this atleast 3 times. Then, write a paragraph about whether the essay answers the prompt. {question}",
                temperature=0.7,
                max_tokens=500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            answer = response["choices"][0]["text"]
            data = {"question": question, "answer": answer}
        else:
            data = {"error": "No question provided."}
        return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
