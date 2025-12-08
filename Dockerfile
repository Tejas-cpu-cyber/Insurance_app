# Base Image
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Copy dependency file first (if exists)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

# Expose Flask port
EXPOSE 5000

# Run flask app
CMD ["python", "app.py"]
