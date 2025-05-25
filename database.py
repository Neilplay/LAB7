import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Using environment variable for database URL
database_url = os.getenv(
    "DATABASE_URL",
    "postgresql://db_qtui_user:kTcS8SVLjEA5bLnTaiHPagxaQKXio9UD@dpg-d0papggdl3ps73ak05tg-a.singapore-postgres.render.com/db_qtui"
)
engine = create_engine(database_url, echo=True)

# Creating a session local class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False,
bind=engine)

# Base class to create tables
Base = declarative_base()
