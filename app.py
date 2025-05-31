from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os
import json
import re

# Carregar variável de ambiente
load_dotenv()
API_KEY = os.getenv("TOKEN")

# Configurar autenticação
client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

# Carregar FAQ
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
Use a seguinte base para responder à pergunta abaixo com mais riqueza de vocabulário, correções gramaticais e uma linguagem natural, fiel ao estilo de Vitor.
Base de conhecimento (não invente nada fora disso, Não repita respostas, e apresente-se apenas uma vez):
\"\"\"{base_answer}\"\"\"

Pergunta do usuário:
{user_message}

⚠️ Regras:
- NÃO invente informações
- Responda SOMENTE com base no conteúdo fornecido
- Amplie, melhore e reescreva com naturalidade como se fosse o Vitor falando
- Inclua características do Vitor: ambicioso, gosta de trabalhar em equipe, busca constante evolução com Python, sempre criando projetos novos
"""
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        reply = clean_text(response.text)
    else:
        reply = "Desculpa, não encontrei uma resposta pronta para isso. Pode tentar perguntar de outra forma?"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
