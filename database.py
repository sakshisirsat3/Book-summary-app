from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration for PostgreSQL
DATABASE_USER = "bookuser"
DATABASE_PASSWORD = "bookpass"
DATABASE_HOST = "db"  # Docker Compose service name
DATABASE_PORT = "5432"
DATABASE_NAME = "bookdb"

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session factory bound to engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
