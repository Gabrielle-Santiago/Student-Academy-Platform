import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Criar a tabela 'users' se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    last_name TEXT,
                    email TEXT,
                    password TEXT
                  )''')

# Commit e fechar a conexão
conn.commit()
conn.close()