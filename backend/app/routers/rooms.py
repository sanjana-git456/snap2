from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas, crud, dependencies

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.get("/", response_model=List[schemas.JamRoom])
def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_jam_rooms(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.JamRoom)
def create_room(room: schemas.JamRoomCreate, db: Session = Depends(get_db), current_user = Depends(dependencies.get_current_user)):
    return crud.create_jam_room(db, room, current_user.id)