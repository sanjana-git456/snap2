from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    bio = Column(Text, nullable=True)
    reputation_score = Column(Integer, default=0)
    is_artist = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    rooms = relationship("JamRoom", back_populates="host")
    events = relationship("Event", back_populates="artist")

class JamRoom(Base):
    __tablename__ = "jam_rooms"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    genre = Column(String)
    is_live = Column(Boolean, default=True)
    host_id = Column(Integer, ForeignKey("users.id"))
    listener_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    host = relationship("User", back_populates="rooms")

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    ticket_price = Column(Float, default=0.0)
    start_time = Column(DateTime)
    artist_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    artist = relationship("User", back_populates="events")