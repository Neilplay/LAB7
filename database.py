import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Using environment variable for database URL
database_url = os.getenv(
    "DATABASE_URL",
    "postgresql://todo_app_render_database_user:s58imWEroNCc141heiJgsblFbwpfD2e1@dpg-cvn5p524d50c73ftpg3g-a.singapore-postgres.render.com/todo_app_render_database"
)
engine = create_engine(database_url, echo=True)

# Creating a session local class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False,
bind=engine)

# Base class to create tables
Base = declarative_base()