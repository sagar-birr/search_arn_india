# Use an official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application files
COPY . /app

# Copy the SQLite database
COPY database.db /app/database.db

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt