from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        database="farmacia",
        user="root",
        password="" # Mude para a sua senha do MySQL se você tiver configurado uma
    )
    return conn

# Rota principal: exibe a página com a tabela preenchida
@app.route("/")
def pagina_inicial():
    conn = get_db_connection()
    cur = conn.cursor(buffered=True)
    
    cur.execute("SELECT nome, lote, quantidade_atual, validade FROM medicamentos;")
    medicamentos = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return render_template("index.html", lista_medicamentos=medicamentos)

# Nova rota: recebe os dados do formulário e insere no MySQL
@app.route("/adicionar", methods=["POST"])
def adicionar_medicamento():
    # Coleta os dados enviados pelo formulário HTML
    codigo = request.form["codigo_barras"]
    nome = request.form["nome"]
    lote = request.form["lote"]
    quantidade = request.form["quantidade_atual"]
    validade = request.form["validade"]
    laboratorio = request.form["laboratorio"]
    
    # Conecta no banco e insere os dados
    conn = get_db_connection()
    cur = conn.cursor()
    
    sql = """
        INSERT INTO medicamentos (codigo_barras, nome, lote, quantidade_atual, validade, laboratorio) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (codigo, nome, lote, quantidade, validade, laboratorio)
    
    cur.execute(sql, valores)
    conn.commit() # Comando essencial para salvar as alterações de forma definitiva no MySQL
    
    cur.close()
    conn.close()
    
    # Redireciona o usuário de volta para a página inicial atualizada
    return redirect(url_for("pagina_inicial"))

if __name__ == "__main__":
    app.run(debug=True)