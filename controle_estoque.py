from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

estoque = {
    "netbooks": 10,
    "tablets": 5,
    "chromebooks": 8,
    "audiovisual": 3
}

itens_alugados = []  # Lista para armazenar os itens alugados

@app.route('/')
def index():
    return render_template('index.html', estoque=estoque)

@app.route('/locacao', methods=['POST'])
def locacao():
    item = request.form['item']
    if estoque[item] > 0:
        estoque[item] -= 1
        itens_alugados.append(item)  # Adiciona o item à lista de itens alugados
        return render_template('reserva_confirmada.html', itens=itens_alugados)
    else:
        return render_template('item_indisponivel.html'), 400

if __name__ == '__main__':
    app.run(debug=True) # Não deixe o modo debug ativo em produção
    #app.run()
