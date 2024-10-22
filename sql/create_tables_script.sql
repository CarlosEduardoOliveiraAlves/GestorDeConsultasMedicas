
    USE consultas_medicas;

    CREATE TABLE Medico (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        especialidade VARCHAR(255) NOT NULL,
        telefone VARCHAR(20)
    );
    
    CREATE TABLE Paciente (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        data_nascimento DATE,
        telefone VARCHAR(20)
    );
    
    CREATE TABLE Consulta (
        id INT AUTO_INCREMENT PRIMARY KEY,
        medico_id INT,
        paciente_id INT,
        data_consulta DATE,
        hora_consulta TIME,
        status VARCHAR(50),
        FOREIGN KEY (medico_id) REFERENCES Medico (id),
        FOREIGN KEY (paciente_id) REFERENCES Paciente (id)
    );

