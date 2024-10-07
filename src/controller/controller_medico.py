from model.medicos import Medico

class MedicoController:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def inserir_medico(self, nome, especialidade, telefone):
        try:
            self.cursor.execute("""
                INSERT INTO Medico (nome, especialidade, telefone) 
                VALUES (?, ?, ?)
            """, (nome, especialidade, telefone))
            self.conn.commit()
            print("Médico inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir médico: {e}")

    def remover_medico(self, medico_id):
        try:
            self.cursor.execute("DELETE FROM Medico WHERE id = ?", (medico_id,))
            self.conn.commit()
            print("Médico removido com sucesso!")
        except Exception as e:
            print(f"Erro ao remover médico: {e}")

    def atualizar_medico(self, medico_id, nome=None, especialidade=None, telefone=None):
        updates = []
        params = []
        
        if nome:
            updates.append("nome = ?")
            params.append(nome)
        if especialidade:
            updates.append("especialidade = ?")
            params.append(especialidade)
        if telefone:
            updates.append("telefone = ?")
            params.append(telefone)
        
        params.append(medico_id)
        
        query = f"UPDATE Medico SET {', '.join(updates)} WHERE id = ?"
        
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            print("Médico atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar médico: {e}")

    def listar_medicos(self):
        try:
            self.cursor.execute("SELECT * FROM Medico")
            medicos = self.cursor.fetchall()
            for medico in medicos:
                print(f"ID: {medico[0]}, Nome: {medico[1]}, Especialidade: {medico[2]}, Telefone: {medico[3]}")
        except Exception as e:
            print(f"Erro ao listar médicos: {e}")
