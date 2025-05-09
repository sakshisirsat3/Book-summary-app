from sqlalchemy import Column, Integer, String, Text, DateTime, func
from .database import Base

class Book(Base):
    """
    SQLAlchemy model for the 'books' table.

    The table stores book information, including:
    - Title
    - Author
    - Genre
    - Summary
    - Timestamps (created_at, updated_at)
    """
    __tablename__ = "books"  # Name of the table in the database

    # Defining columns for the 'books' table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    genre = Column(String, index=True, nullable=True)  # Optional field
    summary = Column(Text, nullable=True)  # Optional field for book summary
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Auto-generates on create
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())  # Auto-generates on update

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, author={self.author})>"


