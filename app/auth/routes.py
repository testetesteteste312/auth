from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import UserCreate, Token
from app.auth.controller import register_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=Token)
def register(data: UserCreate, db: Session = Depends(get_db)):
    user = register_user(db, data.email, data.password)
    return authenticate_user(db, data.email, data.password)

@router.post("/login", response_model=Token)
def login(data: UserCreate, db: Session = Depends(get_db)):
    return authenticate_user(db, data.email, data.password)
