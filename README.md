
# 🧑‍💻 Portfólio Pessoal – Vitorvzp

Este é o repositório do meu portfólio pessoal, desenvolvido com Python e Flask, com o objetivo de apresentar meus projetos, habilidades e experiências de forma interativa e responsiva.

## 🚀 Funcionalidades

- Página inicial com apresentação pessoal e navegação amigável.
- Página de FAQ com respostas automáticas baseadas em um arquivo JSON.
- Rota de chat com integração à IA para respostas personalizadas e inteligentes.
- Design responsivo com HTML e CSS.
- Integração com a API Gemini da Google para geração de respostas personalizadas.

## 💬 Sobre a rota `/chat`

A aplicação oferece uma rota especial chamada `/chat`, que permite ao visitante interagir com um chatbot que simula a personalidade e a forma de comunicação do próprio Vitor Emanuel.

Essa funcionalidade opera da seguinte forma:

- A rota `/chat` (GET) renderiza um template HTML interativo com campo de mensagem.
- Ao enviar uma pergunta (POST), a aplicação:
  - Verifica se há uma resposta no arquivo `faq.json`.
  - Caso exista, a resposta é reescrita com mais clareza e naturalidade, respeitando a personalidade do Vitor.
  - Caso não exista, a pergunta é respondida com base em um prompt de apresentação e valores pessoais de Vitor Emanuel, usando a IA da Gemini.
- O retorno é entregue em formato JSON para ser exibido dinamicamente na interface do chat.

Essa abordagem permite respostas informativas, coerentes, com personalidade e linguagem acessível.

## 🛠️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [Google Generative AI (Gemini)](https://ai.google.dev/)

## 📁 Estrutura do Projeto

```
Port-folio/
├── static/             # Arquivos estáticos (CSS, imagens)
├── templates/          # Templates HTML (home, chat)
├── app.py              # Aplicação Flask principal
├── faq.json            # Base de conhecimento para o FAQ
├── requirements.txt    # Dependências do projeto
└── .gitignore          # Padrões de exclusão do Git
```

## ⚙️ Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/Vitorvzp/Port-folio.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd Port-folio
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate   # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute a aplicação:
   ```bash
   python app.py
   ```

6. Acesse no navegador:
   ```
   http://127.0.0.1:5000/
   ```

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Se você quer saber mais sobre como a rota `/chat` foi construída ou deseja adaptar algo semelhante, sinta-se à vontade para explorar o código ou entrar em contato.
