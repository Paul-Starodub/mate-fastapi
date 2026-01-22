import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
DATABASE_URL = settings.DATABASE_URL
ECHO = os.getenv("ECHO")

engine = create_engine(DATABASE_URL, echo=ECHO)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()
