from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    """
    Base schema for request and response data for a book.
    
    This class is used as the base for creating, updating, and viewing book data.
    """
    title: str  # Title of the book (required)
    author: str  # Author of the book (required)
    genre: Optional[str] = None  # Genre of the book (optional)
    summary: Optional[str] = None  # Short summary or description of the book (optional)

class BookCreate(BookBase):
    """
    Schema for creating a new book.

    Inherits from BookBase and doesn't add any new fields but enforces validation rules.
    """
    pass  # No additional fields needed for creation

class BookUpdate(BookBase):
    """
    Schema for updating an existing book.

    Inherits from BookBase and is used for partial updates (only fields provided in the request are updated).
    """
    pass  # No additional fields needed for updating

class Book(BookBase):
    """
    Schema for the response, including the ID and timestamps of a book.

    This class includes the fields for a book's ID and the timestamps for when it was created or updated.
    """
    id: int  # Unique ID of the book (required for responses)
    created_at: Optional[str] = None  # Timestamp when the book was created (optional)
    updated_at: Optional[str] = None  # Timestamp when the book was last updated (optional)

    class Config:
        # Pydantic's orm_mode is required to work seamlessly with SQLAlchemy models.
        # This allows Pydantic to convert ORM models into dictionaries for API responses.
        orm_mode = Tru