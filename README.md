## API Connect

API REST desenvolvida em Python e Flask para gerenciamento de usuários, como parte da Experiência Prática II de Desenvolvimento Back-end.

## Objetivo

A API Connect é um MVP (Produto Mínimo Viável) desenvolvido com o objetivo de demonstrar a construção de uma API RESTful para cadastro e gerenciamento de usuários.

A aplicação permite realizar as principais operações de um CRUD:

- Criar usuários;
- Listar usuários;
- Buscar usuários por ID;
- Atualizar usuários;
- Remover usuários.

Os dados são armazenados temporariamente em memória por meio de uma lista Python, simulando uma camada de persistência durante o desenvolvimento do MVP.

## Tecnologias utilizadas

- Python 3.14
- Flask 3.1.3
- Git
- GitHub
- Thunder Client para testes dos endpoints
- Ambiente virtual Python (`venv`)

## Estrutura do projeto

```text
Projeto Nexus/
│
├── controllers/
│   └── user_controller.py
│
├── data/
│   └── users.py
│
├── routes/
│   └── user_routes.py
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## Responsabilidade dos principais arquivos

- app.py: ponto de entrada da aplicação Flask e configuração inicial do servidor.
- routes/user_routes.py: definição das rotas HTTP relacionadas aos usuários.
- controllers/user_controller.py: implementação das regras de negócio e manipulação das requisições.
- data/users.py: armazenamento temporário dos usuários em memória e controle da geração dos IDs.
- requirements.txt: relação das dependências necessárias para execução da aplicação.
- .gitignore: definição dos arquivos e diretórios que não devem ser versionados pelo Git.

## Pré-requisitos

Para executar o projeto localmente, é necessário ter instalado:

- Python 3.14 ou superior;
- Git.

## Instalação e execução

1. Clone o repositório
    git clone https://github.com/Gulu93/api-connect-gustavo-esteves.git

2. Acesse a pasta do projeto
    cd api-connect-gustavo-esteves

3. Crie o ambiente virtual

    No Windows:
        python -m venv .venv

4. Ative o ambiente virtual

    No PowerShell:
        .\.venv\Scripts\Activate.ps1

5. Instale as dependências
    pip install -r requirements.txt

6. Execute a aplicação
    python app.py

Após a inicialização, a API estará disponível localmente em:
    http://127.0.0.1:5000

## Endpoints

A API disponibiliza os seguintes endpoints:

| Método | Endpoint | Descrição | Status de sucesso |
|---|---|---|---|
| POST | /users | Cadastra um novo usuário | 201 / 400 |
| GET | /users | Lista todos os usuários | 200 |
| GET | /users/<id> | Busca um usuário pelo ID | 200 / 404 |
| PUT | /users/<id> | Atualiza um usuário | 200 / 400 / 404 |
| DELETE | /users/<id> | Remove um usuário | 204 / 404 |

## Exemplos de utilização

1. Criar usuário
    
    **POST /users**

    * Corpo da requisição:

        ```json
        {
            "nome": "Gustavo",
            "email": "gustavo@email.com"
        }
        ```

    * Resposta de sucesso:
        ```json
        {
            "data": {
                "id": 1,
                "nome": "Gustavo",
                "email": "gustavo@email.com"
            }
        }
        ```
    * Status:
        201 Created

2. Validação no cadastro

    * Caso o campo nome não seja informado:
        ```json
        {
            "error": "O campo nome é obrigatório"
        }
        ```

    * Caso o campo email não seja informado:
        ```json
        {
            "error": "O campo email é obrigatório"
        }
        ```
    * Status:
        400 Bad Request

3. Listar usuários
    
    **GET /users**

    * Resposta:
        ```json
        [
            {
                "id": 1,
                "nome": "Gustavo",
                "email": "gustavo@email.com"
            }
        ]
        ```
    * Status:
        200 OK

4. Buscar usuário por ID
   
    **GET /users/1**

    * Resposta de sucesso:
        ```json
        {
            "id": 1,
            "nome": "Gustavo",
            "email": "gustavo@email.com"
        }
        ```
    * Status:
        200 OK

    * Caso o ID não exista:
        ```json
        {
            "error": "Usuário não encontrado"
        }
        ```
    * Status:
        404 Not Found

5. Atualizar usuário
    
    **PUT /users/1**

    * Corpo da requisição:
        ```json
        {
            "nome": "Gustavo Esteves",
            "email": "gustavo.esteves@email.com"
        }
        ```
    * Resposta de sucesso:
        ```json
        {
            "data": {
                "id": 1,
                "nome": "Gustavo Esteves",
                "email": "gustavo.esteves@email.com"
            }
        }
        ```
    * Status:
        200 OK

    * Caso algum campo obrigatório não seja informado:
        ```json
        {
            "error": "O campo email é obrigatório"
        }
        ```
    * Status:
        400 Bad Request

    * Caso o ID não exista:
        ```json
        {
            "error": "Usuário não encontrado"
        }
        ```
    * Status:
        404 Not Found

6. Remover usuário
    
    **DELETE /users/1**

    * Resposta de sucesso:
        204 No Content

    * Caso o ID não exista:
        ```json
        {
            "error": "Usuário não encontrado"
        }
        ```
    * Status:
        404 Not Found

## Validações

As operações de cadastro e atualização realizam validações dos dados enviados pelo cliente.

Os campos nome e email são obrigatórios. Caso algum deles não seja informado, a API interrompe a operação e retorna uma resposta de erro em formato JSON com status 400 Bad Request.

As operações de criação e atualização utilizam a chave data nas respostas de sucesso, enquanto as situações de erro utilizam a chave error.

## Persistência de dados

Para este MVP, os usuários são armazenados temporariamente em uma lista em memória.

Essa abordagem foi adotada para manter o foco na implementação da API e das operações CRUD, sem a necessidade de configurar um banco de dados durante esta etapa do projeto.

Os dados permanecem disponíveis enquanto o servidor estiver em execução. Ao reiniciar a aplicação, a estrutura em memória é reinicializada.

Os IDs são gerados de forma incremental por meio de um contador mantido na estrutura de dados da aplicação.

## Testes

Os endpoints foram testados manualmente utilizando o Thunder Client, extensão integrada ao Visual Studio Code.

Foram realizados testes de:

- Cadastro de usuário com sucesso;
- Cadastro sem o campo email;
- Listagem de usuários;
- Busca de usuário existente;
- Busca de usuário inexistente;
- Atualização de usuário;
- Remoção de usuário.

Os testes verificaram tanto o conteúdo das respostas quanto os respectivos códigos de status HTTP.

## Versionamento

O projeto utiliza Git para controle de versão e está disponível publicamente no GitHub.

## Repositório:

https://github.com/Gulu93/api-connect-gustavo-esteves