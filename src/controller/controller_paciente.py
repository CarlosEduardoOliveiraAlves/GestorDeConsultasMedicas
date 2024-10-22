from model.paciente import Paciente

class PacienteController:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def inserir_paciente(self, nome, data_nascimento, telefone):
        try:
            self.cursor.execute("""
                INSERT INTO Paciente (nome, data_nascimento, telefone) 
                VALUES (%s, %s, %s)
            """, (nome, data_nascimento, telefone))
            self.conn.commit()
            print("Paciente inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir paciente: {e}")

    def remover_paciente(self, paciente_id):
        try:
            self.cursor.execute("DELETE FROM Paciente WHERE id = %s", (paciente_id,))
            self.conn.commit()
            print("Paciente removido com sucesso!")
        except Exception as e:
            print(f"Erro ao remover paciente: {e}")

    def atualizar_paciente(self, paciente_id, nome=None, data_nascimento=None, telefone=None):
        updates = []
        params = []
        
        if nome:
            updates.append("nome = %s")
            params.append(nome)
        if data_nascimento:
            updates.append("data_nascimento = %s")
            params.append(data_nascimento)
        if telefone:
            updates.append("telefone = %s")
            params.append(telefone)
        
        params.append(paciente_id)
        
        query = f"UPDATE Paciente SET {', '.join(updates)} WHERE id = %s"
        
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            print("Paciente atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar paciente: {e}")

    def listar_pacientes(self):
        try:
            self.cursor.execute("SELECT * FROM Paciente")
            pacientes = self.cursor.fetchall()
            for paciente in pacientes:
                print(f"ID: {paciente[0]}, Nome: {paciente[1]}, Data de Nascimento: {paciente[2]}, Telefone: {paciente[3]}")
        except Exception as e:
            print(f"Erro ao listar pacientes: {e}")
