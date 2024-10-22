from datetime import date

class Consulta:
    def __init__(self, 
                 id:int=None,
                 medico_ID:int=None,
                 paciente_ID:int=None,  
                 data_consulta:date=None,
                 hora_consulta:str=None,
                 status:str=None
                ):
        
        self.set_ID(id)
        self.set_medico_ID(medico_ID)
        self.set_paciente_ID(paciente_ID)
        self.set_data_consulta(data_consulta)
        self.set_hora_consulta(hora_consulta)
        self.set_status(status)

    def set_ID(self, id:int):
        self.id = id

    def get_ID(self) -> int:
        return self.id

    def set_medico_ID(self, medico_ID: int):
        self.medico_ID = medico_ID

    def get_medico_ID(self) -> int:
        return self.medico_ID
    
    def set_paciente_ID(self, paciente_ID: int):
        self.paciente_ID = paciente_ID

    def get_paciente_ID(self) -> int:
        return self.paciente_ID

    def set_data_consulta(self, data_consulta: date):
        self.data_consulta = data_consulta

    def get_data_consulta(self) -> date:
        return self.data_consulta
    
    def set_hora_consulta(self, hora_consulta: str):
        self.hora_consulta = hora_consulta

    def get_hora_consulta(self) -> str:
        return self.hora_consulta
    
    def set_status(self, status: str):
        self.status = status

    def get_status(self) -> str:
        return self.status

    def to_string(self) -> str:
        return f"ID: {self.get_ID()} | Medico ID: {self.get_medico_ID()} | Paciente ID: {self.get_paciente_ID()} | Data Consulta: {self.get_data_consulta()} | Hora Consulta: {self.get_hora_consulta} | Status: {self.get_status()}"