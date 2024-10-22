from controller.controller_medico import MedicoController
from controller.controller_paciente import PacienteController
from controller.controller_consulta import ConsultaController
import os
from dotenv import load_dotenv
import mysql.connector

def main():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Conectar ao banco de dados
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    cursor = conn.cursor()

    # Inicializando os controllers
    medico_controller = MedicoController(cursor, conn)
    paciente_controller = PacienteController(cursor, conn)
    consulta_controller = ConsultaController(cursor, conn)

    while True:
        print("\n----- Sistema de Controle de Consultas Médicas -----")
        print("1. Relatórios")
        print("2. Inserir registros")
        print("3. Remover registros")
        print("4. Atualizar registros")
        print("5. Listar registros")
        print("6. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            gerar_relatorios(consulta_controller)
        elif choice == '2':
            inserir_registros(medico_controller, paciente_controller, consulta_controller)
        elif choice == '3':
            remover_registros(medico_controller, paciente_controller, consulta_controller)
        elif choice == '4':
            atualizar_registros(medico_controller, paciente_controller, consulta_controller)
        elif choice == '5':
            listar_registros(medico_controller, paciente_controller, consulta_controller)
        elif choice == '6':
            break
        else:
            print("Opção inválida.")

    conn.close()

def gerar_relatorios(consulta_controller):
    print("\n--- Relatórios ---")
    print("1. Consultas por médico")
    print("2. Consultas por especialidade")
    choice = input("Escolha um relatório: ")
    
    if choice == '1':
        consulta_controller.listar_consultas()
    elif choice == '2':
        consulta_controller.listar_consultas_por_especialidade()

def inserir_registros(medico_controller, paciente_controller, consulta_controller):
    print("\n--- Inserir Registros ---")
    print("1. Inserir Médico")
    print("2. Inserir Paciente")
    print("3. Inserir Consulta")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        nome = input("Nome do Médico: ")
        especialidade = input("Especialidade: ")
        telefone = input("Telefone: ")
        medico_controller.inserir_medico(nome, especialidade, telefone)
    
    elif choice == '2':
        nome = input("Nome do Paciente: ")
        data_nascimento = input("Data de Nascimento (YYYY-MM-DD): ")
        telefone = input("Telefone: ")
        paciente_controller.inserir_paciente(nome, data_nascimento, telefone)
    
    elif choice == '3':
        medico_id = int(input("ID do Médico: "))
        paciente_id = int(input("ID do Paciente: "))
        data_consulta = input("Data da Consulta (YYYY-MM-DD): ")
        hora_consulta = input("Hora da Consulta (HH:MM): ")
        status = input("Status da Consulta: ")
        consulta_controller.inserir_consulta(medico_id, paciente_id, data_consulta, hora_consulta, status)

def remover_registros(medico_controller, paciente_controller, consulta_controller):
    print("\n--- Remover Registros ---")
    print("1. Remover Médico")
    print("2. Remover Paciente")
    print("3. Remover Consulta")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        medico_id = int(input("ID do Médico a ser removido: "))
        medico_controller.remover_medico(medico_id)
    
    elif choice == '2':
        paciente_id = int(input("ID do Paciente a ser removido: "))
        paciente_controller.remover_paciente(paciente_id)
    
    elif choice == '3':
        consulta_id = int(input("ID da Consulta a ser removida: "))
        consulta_controller.remover_consulta(consulta_id)

def atualizar_registros(medico_controller, paciente_controller, consulta_controller):
    print("\n--- Atualizar Registros ---")
    print("1. Atualizar Médico")
    print("2. Atualizar Paciente")
    print("3. Atualizar Consulta")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        medico_id = int(input("ID do Médico a ser atualizado: "))
        nome = input("Novo nome (ou pressione Enter para manter o atual): ")
        especialidade = input("Nova especialidade (ou pressione Enter para manter a atual): ")
        telefone = input("Novo telefone (ou pressione Enter para manter o atual): ")
        medico_controller.atualizar_medico(medico_id, nome, especialidade, telefone)
    
    elif choice == '2':
        paciente_id = int(input("ID do Paciente a ser atualizado: "))
        nome = input("Novo nome (ou pressione Enter para manter o atual): ")
        data_nascimento = input("Nova data de nascimento (YYYY-MM-DD) (ou Enter para manter a atual): ")
        telefone = input("Novo telefone (ou Enter para manter o atual): ")
        paciente_controller.atualizar_paciente(paciente_id, nome, data_nascimento, telefone)
    
    elif choice == '3':
        consulta_id = int(input("ID da Consulta a ser atualizada: "))
        data_consulta = input("Nova data (YYYY-MM-DD) (ou Enter para manter a atual): ")
        hora_consulta = input("Nova hora (HH:MM) (ou Enter para manter a atual): ")
        status = input("Novo status (ou Enter para manter o atual): ")
        consulta_controller.atualizar_consulta(consulta_id, data_consulta, hora_consulta, status)

def listar_registros(medico_controller, paciente_controller, consulta_controller):
    print("\n--- Listar Registros ---")
    print("1. Listar Médicos")
    print("2. Listar Pacientes")
    print("3. Listar Consultas")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        medico_controller.listar_medicos()
    
    elif choice == '2':
        paciente_controller.listar_pacientes()
    
    elif choice == '3':
        consulta_controller.listar_consultas()

if __name__ == '__main__':
    main()
