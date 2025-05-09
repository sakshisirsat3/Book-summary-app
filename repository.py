# repository.py

from sqlalchemy.orm import Session
from . import models, schemas

def get_all_books(db: Session, skip: int = 0, limit: int = 10):
    """
    Fetch a list of books with pagination.

    Args:
        db: SQLAlchemy database session
        skip: Number of books to skip (used for pagination)
        limit: Number of books to return per page

    Returns:
        List of books in the database, paginated by 'skip' and 'limit'
    """
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book_by_id(db: Session, book_id: int):
    """
    Fetch a single book by its ID.

    Args:
        db: SQLAlchemy database session
        book_id: ID of the book to fetch

    Returns:
        Book object if found, None if not found
    """
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def add_book(db: Session, book: schemas.BookCreate):
    """
    Add a new book to the database.

    Args:
        db: SQLAlchemy database session
        book: BookCreate schema containing the data for the new book

    Returns:
        The newly created Book object
    """
    db_book = models.Book(**book.dict())  # Unpacks schema into the model
    db.add(db_book)
    db.commit()  # Commit the transaction to the database
    db.refresh(db_book)  # Refresh the object to get the latest data
    return db_book

def update_existing_book(db: Session, book_id: int, book: schemas.BookUpdate):
    """
    Update an existing book in the database.

    Args:
        db: SQLAlchemy database session
        book_id: ID of the book to update
        book: BookUpdate schema containing the updated book data

    Returns:
        The updated Book object, or None if not found
    """
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        for key, value in book.dict(exclude_unset=True).items():  # Only update fields that are provided
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book
    return None  # Return None if the book is not found

def delete_book(db: Session, book_id: int):
    """
    Delete a book from the database by its ID.

    Args:
        db: SQLAlchemy database session
        book_id: ID of the book to delete

    Returns:
        The deleted Book object, or None if not found
    """
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()  # Commit to delete from the database
        return db_book
    return None  # Return None if the book is not found
