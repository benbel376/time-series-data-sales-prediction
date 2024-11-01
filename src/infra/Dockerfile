# src/infra/Dockerfile

# Start with an official Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the application's port (optional, e.g., if running FastAPI or Flask)
EXPOSE 8000

# Define the command to start the app
CMD ["python", "src/apps/main.py"]
