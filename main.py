from flask import Flask, render_template, request
from ai import gpt, memory
app = Flask(__name__)
spisok = [4, 65, 90, 12]
@app.route("/")
def hello_world():
    return render_template("index.html", spisok=spisok)

@app.route("/request", methods=["POST"])
def requested():
    user_question = request.form["input-request"]
    ai_answer = gpt(user_question)

    return render_template("index.html", ai_answer=ai_answer, memory=memory)

app.run(debug=True)