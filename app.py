from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os
import json
import re


load_dotenv()
API_KEY = os.getenv("TOKEN")


client = genai.Client(api_key=API_KEY)

app = Flask(__name__)


with open("faq.json", "r", encoding="utf-8") as f:
    faq = json.load(f)

def clean_text(text):
    return re.sub(r"[*_]", "", text)

def find_best_answer(user_input):
    user_input_lower = user_input.lower()
    for item in faq:
        if item["question"].lower() in user_input_lower:
            return item["answer"]
    return None

@app.route("/")
def sobre():
    return render_template("home.html")

@app.route("/chat")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.get_json().get("message")
    if not user_message:
        return jsonify({"reply": "Por favor, envie uma mensagem válida."})

    base_answer = find_best_answer(user_message)

    if base_answer:
        prompt = f"""
Aja como Vitor Emanuel, um jovem de 15 anos, apaixonado por tecnologia, ambicioso, que gosta de trabalhar em equipe e está em constante evolução na linguagem Python, sempre buscando desenvolver novos projetos.

Reescreva o texto abaixo com mais clareza, correção ortográfica e estilo natural, mantendo o conteúdo fiel e ampliando com leveza o que já foi dito, mas sem inventar informações fora do original, naõ fescreva muito texto ao ponto da leitura ser cansativa, também não resuma muito para não ser uma resposta vazia, acho o ponto idela para convencer uma pessoa de que sou uma boa pessoa da área e talvez um ótimo funcionário:

\"\"\"{base_answer}\"\"\"
"""
    else:
        prompt = f"""
Você é Vitor Emanuel, um jovem de 15 anos, apaixonado por tecnologia, ambicioso, comunicativo, curioso e em constante evolução como programador Python. Responda à pergunta abaixo com naturalidade, clareza, correção ortográfica e mantendo a personalidade do Vitor — um jovem dedicado, autodidata, que valoriza desafios, trabalho em equipe e ama transformar ideias em projetos reais.

Pergunta do usuário:
\"\"\"{user_message}\"\"\"
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    reply = clean_text(response.text)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)