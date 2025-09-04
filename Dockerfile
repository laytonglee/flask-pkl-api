# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port (Railway reads env PORT anyway)
EXPOSE 5000

# Run Flask app using dynamic PORT
CMD ["python", "app_flask.py"]
