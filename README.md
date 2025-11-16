# 🛡️ ImuneTrack Auth

Microserviço de autenticação e gerenciamento de usuários do sistema **ImuneTrack**.

Ele é responsável por:
- Cadastro e autenticação de usuários;
- Geração e validação de tokens JWT;
- Gerenciamento de permissões e refresh tokens;
- Integração com o microserviço principal (`imunetrack-backend`).

---

## 🚀 Tecnologias

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Alembic** (migrations)
- **Docker & Docker Compose**
- **Pytest** (testes automatizados)

---

## ⚙️ Estrutura do Projeto

```
imunetrack-auth/
│
├── app/
│   ├── main.py               # Ponto de entrada FastAPI
│   ├── auth/                 # Rotas e lógica de autenticação
│   ├── database.py           # Conexão com o banco
│   ├── models/               # Modelos SQLAlchemy
│   ├── schemas/              # Schemas Pydantic
│   └── tests/                # Testes unitários e de integração
│
├── alembic/                  # Migrations do banco
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🧪 Executando o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://gitlab.com/imunetrack/imunetrack-auth.git
cd imunetrack-auth
```

### 2️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` com os seguintes valores:

```
DATABASE_URL=postgresql+psycopg2://user:password@db:5432/imunetrack_auth
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3️⃣ Subir o container

```bash
docker-compose up --build
```

O serviço estará disponível em:  
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔑 Endpoints Principais

| Método | Rota | Descrição |
|--------|------|------------|
| `POST` | `/auth/register` | Cadastra um novo usuário |
| `POST` | `/auth/login` | Realiza login e retorna JWT |
| `POST` | `/auth/refresh` | Gera novo token de acesso |
| `GET` | `/auth/me` | Retorna informações do usuário logado |

---

## 🧰 Testes

Para executar os testes localmente:

```bash
docker-compose run --rm tests
```

---

## 📦 Deploy

O `imunetrack-auth` é publicado no GitLab Container Registry e utilizado em produção via `docker-compose` do sistema completo.

---
