import mysql.connector
from werkzeug.security import generate_password_hash

conn = mysql.connector.connect(
    host="localhost",
    database="farmacia",
    user="root",
    password=""  # Altere para a sua senha do MySQL, se houver
)
cur = conn.cursor()

nome = "Administrador"
email = "admin@farmacia.com"
senha_hash = generate_password_hash("admin123")
perfil = "Administrador"

sql = """
    INSERT INTO usuarios (nome, email, senha_hash, perfil) 
    VALUES (%s, %s, %s, %s) 
    ON DUPLICATE KEY UPDATE senha_hash = VALUES(senha_hash);
"""

cur.execute(sql, (nome, email, senha_hash, perfil))
conn.commit()

print("Usuário Administrador cadastrado com sucesso!")

cur.close()
conn.close()