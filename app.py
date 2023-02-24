from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# configure a chave de API da OpenAI
openai.api_key = "cole sua api key aqui"

# rota principal da aplicação
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # obter a pergunta digitada pelo usuário
        question = request.form["question"]
        
        # chamar a API do GPT-3 para obter a resposta
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Q: {question}\nA:",
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None,
            timeout=10
        )
        
        # obter a resposta gerada pela API
        answer = response.choices[0].text
        
        # exibir a resposta para o usuário
        return render_template("answer.html", question=question, answer=answer)
        
    # exibir a página inicial com o formulário
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
