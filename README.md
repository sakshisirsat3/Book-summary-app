# Book Management App

This is a containerized web app for managing books — you can create, read, update, and delete book records, and it’s ready to run either locally with Docker or deployed on a cloud VM like AWS EC2. It’s built with FastAPI for the backend and uses PostgreSQL as the database.

## What does the app do?

The app exposes a RESTful API where you can:
- Add a new book with title, author, year, and summary
- Get all books in the system
- View a single book by its ID
- Edit/update a book
- Delete a book from the list


## What technologies are used?

- FastAPI (Python backend)
- PostgreSQL database
- Docker & Docker Compose for containerization
- dotenv for managing environment variables
- Hosted using Docker on any VM (tested on AWS EC2)


