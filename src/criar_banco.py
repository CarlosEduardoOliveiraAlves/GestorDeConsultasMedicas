import sqlite3

def criar_banco():
    # Conecte ao banco de dados (ou crie-o se não existir)
    conn = sqlite3.connect('consultas_medicas.db')
    cursor = conn.cursor()

    # Criando a tabela Medico
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Medico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            telefone TEXT
        )
    ''')

    # Criando a tabela Paciente
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Paciente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento DATE NOT NULL,
            telefone TEXT
        )
    ''')

    # Criando a tabela Consulta
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Consulta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            medico_id INTEGER,
            paciente_id INTEGER,
            data_consulta DATE NOT NULL,
            hora_consulta TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (medico_id) REFERENCES Medico(id),
            FOREIGN KEY (paciente_id) REFERENCES Paciente(id)
        )
    ''')

    # Confirmar e fechar conexão
    conn.commit()
    conn.close()
    print("Banco de dados e tabelas criados com sucesso!")

if __name__ == '__main__':
    criar_banco()
