from sqlalchemy.orm import Session
from . import models, schemas, security

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_artist=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_jam_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.JamRoom).filter(models.JamRoom.is_live == True).offset(skip).limit(limit).all()

def create_jam_room(db: Session, room: schemas.JamRoomCreate, user_id: int):
    db_room = models.JamRoom(**room.model_dump(), host_id=user_id)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate, user_id: int):
    db_event = models.Event(**event.model_dump(), artist_id=user_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event