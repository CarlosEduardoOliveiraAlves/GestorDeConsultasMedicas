class Paciente:
    def __init__(self, 
                 id:int=None, 
                 nome:str=None,
                 telefone:str=None
                ):
        
        self.set_ID(id)
        self.set_Nome(nome)
        self.set_Telefone(telefone)

    def set_ID(self, id:int):
        self.id = id

    def get_ID(self) -> int:
        return self.id

    def set_Nome(self, nome:str):
        self.nome = nome

    def get_Nome(self) -> str:
        return self.nome

    def set_Telefone(self, telefone:str):
        self.telefone = telefone

    def get_Telefone(self) -> str:
        return self.telefone

    def to_string(self) -> str:
        return f"ID: {self.get_ID()} | Nome: {self.get_Nome()} | Telefone: {self.get_Telefone}"