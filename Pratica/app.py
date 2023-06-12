from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Armazenamento de dados
funcionarios = []

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/funcionarios')
def show_all():
    return render_template('show_all.html', funcionarios=funcionarios)

# Página de cadastro de funcionários
@app.route('/cadastrar-funcionario', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereço']
        telefone = request.form['telefone']
        dados = {"nome": nome, "telefone": telefone, "endereco": endereco}
        funcionarios.append(dados)
        return redirect('/funcionarios')
    return render_template('cadastro.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    funcionario = next((funcionario for funcionario in funcionarios if funcionario.get('id') == id), None)
    if funcionario is not None:
        if request.method == 'POST':
            funcionario['nome'] = request.form['nome']
            funcionario['endereço'] = request.form['endereço']
            funcionario['telefone'] = request.form['telefone']
            return redirect('funcionarios')
    else:
        return render_template('edicao.html', funcionario=funcionario)

# Rota para exclusão de funcionários
@app.route('/excluir-funcionario/<int:id>', methods=['GET', 'POST'])
def exclusao(id):
    del funcionarios[id]
    return redirect('/funcionarios')

if __name__ == '__main__':
    app.run(debug=True)

