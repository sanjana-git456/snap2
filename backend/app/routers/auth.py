from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud, security, dependencies

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_obj = crud.create_user(db, user)
    access_token = security.create_access_token(subject=user_obj.username)
    return {"access_token": access_token, "token_type": "bearer", "user": user_obj}

@router.post("/login", response_model=schemas.Token)
def login(login_data: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=login_data.username)
    if not user or not security.verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = security.create_access_token(subject=user.username)
    return {"access_token": access_token, "token_type": "bearer", "user": user}

@router.get("/me", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(dependencies.get_current_user)):
    return current_user