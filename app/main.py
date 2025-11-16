from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.database import Base, engine  # importa o Base e engine do SQLAlchemy

app = FastAPI(title="ImuneTrack Auth Service")

# Cria todas as tabelas que ainda não existem
Base.metadata.create_all(bind=engine)

# Inclui os routers
app.include_router(auth_router)
