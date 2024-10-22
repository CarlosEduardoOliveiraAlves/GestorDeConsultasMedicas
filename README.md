# Sistema de Controle de Consultas Médicas

Este projeto é um sistema simples de controle de consultas médicas, permitindo o cadastro de médicos, pacientes e consultas. O sistema oferece funcionalidades CRUD (Criar, Ler, Atualizar, Deletar) para os três tipos de registros e utiliza um banco de dados MySQL para a persistência de dados.

## Funcionalidades

- Inserção, remoção e atualização de médicos, pacientes e consultas.
- Listagem de médicos, pacientes e consultas.
- Relatórios de consultas por médico e especialidade.

## Tecnologias Utilizadas

- **Python 3.x**
- **MySQL** (ou outro banco relacional)
- **Bibliotecas**: `mysql-connector-python`, `python-dotenv`
- **Estrutura de Pastas**:
  - `/sql`: contém o script para a criação das tabelas do banco.
  - `/src`: contém os arquivos de código do projeto (controllers, models, conexões).

## Pré-requisitos

Antes de rodar o projeto, você precisará instalar:

1. **Python 3.x**
   - Instale o Python através do [site oficial](https://www.python.org/downloads/).

2. **MySQL**
   - Instale o MySQL Server localmente ou use um banco de dados remoto. Veja o [site oficial](https://dev.mysql.com/downloads/installer/) para detalhes de instalação.

3. **pip**
   - Certifique-se de que o `pip` está instalado para gerenciar pacotes Python:
    ```bash
        python -m ensurepip --upgrade
    ```

## Configuração do Projeto

1. **Clone o Repositório**

```bash
    git clone https://github.com/CarlosEduardoOliveiraAlves/GestorDeConsultasMedicas.git
    cd GestorDeConsultasMedicas
```

2. **Instalar Dependências Python**

    Execute o seguinte comando para instalar as bibliotecas Python necessárias:
    ```bash
        pip install -r requirements.txt

3. **Configuração de Banco de Dados**

    1. Crie um banco de dados `MySQL`:

    ```sql
        CREATE DATABASE consultas_medicas;
    ```

    2. Use o comando `SQL` para criar as tabelas:

    ```sql
    
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


    ```

3. **Configurar Variáveis de Ambiente**

Crie um arquivo `.env` na raiz do projeto com as seguintes informações:

```bash
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=sua_senha
    DB_NAME=consultas_medicas
```
4. **Rodar o Projeto**

Execute o script `main.py` para iniciar o sistema:

```bash
    python src/main.py
```

## Instalação de Dependências

As dependências do projeto podem ser instaladas via o arquivo `requirements.txt`. Se o arquivo ainda não existir, crie um com o seguinte conteúdo:

# `requirements.txt`

```bash
    mysql-connector-python==8.0.33
    python-dotenv==1.0.0
```

Instale as dependências com:

```bash
    pip install -r requirements.txt
```

## Observações

- Certifique-se de configurar corretamente o MySQL antes de rodar o projeto.
- Nunca suba o arquivo .env para o repositório para proteger suas credenciais de banco de dados.
- O projeto foi testado com Python 3.x e MySQL 8.0, outras versões podem funcionar, mas podem exigir ajustes.
