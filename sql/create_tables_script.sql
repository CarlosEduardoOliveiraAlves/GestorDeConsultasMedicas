CREATE TABLE Medico (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    especialidade TEXT NOT NULL,
    telefone TEXT
);

CREATE TABLE Paciente (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    data_nascimento DATE,
    telefone TEXT
);

CREATE TABLE Consulta (
    id INTEGER PRIMARY KEY,
    medico_id INTEGER,
    paciente_id INTEGER,
    data_consulta DATE,
    hora_consulta TEXT,
    status TEXT,
    FOREIGN KEY (medico_id) REFERENCES Medico (id),
    FOREIGN KEY (paciente_id) REFERENCES Paciente (id)
);
