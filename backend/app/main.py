from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base, SessionLocal
from .routers import auth, rooms, events
from . import models
import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SnapStage API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def seed_data():
    db = SessionLocal()
    if db.query(models.User).count() == 0:
        from .security import get_password_hash
        # Create a sample artist
        artist = models.User(
            username="jazz_master",
            email="jazz@example.com",
            hashed_password=get_password_hash("password123"),
            bio="Late night jazz sessions and smooth vibes.",
            is_artist=True,
            reputation_score=150
        )
        db.add(artist)
        db.commit()
        db.refresh(artist)

        # Create sample room
        room = models.JamRoom(
            title="Midnight Jazz Jam",
            description="Join us for an improvisational jazz session.",
            genre="Jazz",
            host_id=artist.id,
            listener_count=42
        )
        db.add(room)

        # Create sample event
        event = models.Event(
            title="Summer Solstice Concert",
            description="An exclusive virtual performance to celebrate the longest day.",
            ticket_price=5.0,
            start_time=datetime.datetime.now() + datetime.timedelta(days=2),
            artist_id=artist.id
        )
        db.add(event)
        db.commit()
    db.close()

app.include_router(auth.router, prefix="/api")
app.include_router(rooms.router, prefix="/api")
app.include_router(events.router, prefix="/api")

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}