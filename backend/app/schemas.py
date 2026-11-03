from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    bio: Optional[str] = None
    reputation_score: int
    is_artist: bool
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: User

class JamRoomBase(BaseModel):
    title: str
    description: str
    genre: str

class JamRoomCreate(JamRoomBase):
    pass

class JamRoom(JamRoomBase):
    id: int
    is_live: bool
    host_id: int
    listener_count: int
    created_at: datetime
    host: User

    class Config:
        from_attributes = True

class EventBase(BaseModel):
    title: str
    description: str
    ticket_price: float
    start_time: datetime

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    artist_id: int
    artist: User

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    username: str
    password: str