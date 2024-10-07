from model.consulta import Consulta

class ConsultaController:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def inserir_consulta(self, medico_id, paciente_id, data_consulta, hora_consulta, status):
        try:
            self.cursor.execute("""
                INSERT INTO Consulta (medico_id, paciente_id, data_consulta, hora_consulta, status) 
                VALUES (?, ?, ?, ?, ?)
            """, (medico_id, paciente_id, data_consulta, hora_consulta, status))
            self.conn.commit()
            print("Consulta marcada com sucesso!")
        except Exception as e:
            print(f"Erro ao marcar consulta: {e}")

    def remover_consulta(self, consulta_id):
        try:
            self.cursor.execute("DELETE FROM Consulta WHERE id = ?", (consulta_id,))
            self.conn.commit()
            print("Consulta removida com sucesso!")
        except Exception as e:
            print(f"Erro ao remover consulta: {e}")

    def atualizar_consulta(self, consulta_id, data_consulta=None, hora_consulta=None, status=None):
        updates = []
        params = []
        
        if data_consulta:
            updates.append("data_consulta = ?")
            params.append(data_consulta)
        if hora_consulta:
            updates.append("hora_consulta = ?")
            params.append(hora_consulta)
        if status:
            updates.append("status = ?")
            params.append(status)
        
        params.append(consulta_id)
        
        query = f"UPDATE Consulta SET {', '.join(updates)} WHERE id = ?"
        
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            print("Consulta atualizada com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar consulta: {e}")

    def listar_consultas(self):
        try:
            self.cursor.execute("""
                SELECT Medico.nome, Paciente.nome, Consulta.data_consulta, Consulta.hora_consulta, Consulta.status
                FROM Consulta
                JOIN Medico ON Consulta.medico_id = Medico.id
                JOIN Paciente ON Consulta.paciente_id = Paciente.id
            """)
            consultas = self.cursor.fetchall()
            for consulta in consultas:
                print(f"Médico: {consulta[0]}, Paciente: {consulta[1]}, Data: {consulta[2]}, Hora: {consulta[3]}, Status: {consulta[4]}")
        except Exception as e:
            print(f"Erro ao listar consultas: {e}")
