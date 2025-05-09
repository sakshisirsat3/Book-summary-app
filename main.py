from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from . import models, schemas, repository
from .database import SessionLocal, engine

# Create database tables on startup (only for dev/local use)
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Book Summary API",
    description="A RESTful API to manage and summarize books.",
    version="1.0.0"
)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book entry in the database.
    """
    return repository.add_book(db=db, book=book)


@app.get("/books/", response_model=list[schemas.Book])
def list_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a paginated list of all books.
    """
    return repository.get_all_books(db=db, skip=skip, limit=limit)


@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a book by its unique ID.
    """
    book = repository.get_book_by_id(db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    """
    Update an existing book by ID.
    """
    updated_book = repository.update_existing_book(db=db, book_id=book_id, book=book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book from the database by its ID.
    """
    deleted_book = repository.delete_book(db=db, book_id=book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book
