# Use an official Python runtime as base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install dependencies (if required)
RUN pip install --no-cache-dir -r requirements.txt || true

# Command to run the application
CMD ["python", "calculator.py"]
