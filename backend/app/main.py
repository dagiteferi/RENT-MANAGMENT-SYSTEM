# Entry point for FastAPI app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.routers import auth, users
from app.database import Base, engine

app = FastAPI()

# Add Session middleware
# Replace "your-secret-key" with a real secret key in a production environment
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)