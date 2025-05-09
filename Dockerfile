# Use an official Python base image
FROM python:3.11-slim

# Metadata
LABEL maintainer="sakshi.sirsat777@gmail.com"
LABEL author="sakshi sirsat"
LABEL version="1.0"
LABEL description="Dockerfile for the Book Management application using FastAPI and PostgreSQL"

# Set working directory inside the container
WORKDIR /app

# Copy dependency list and install Python packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the working directory
COPY . .

# Expose port for FastAPI (default: 8000)
EXPOSE 8000

# Start the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

