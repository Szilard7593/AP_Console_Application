# Use Python 3.12 (matches your project settings)
FROM python:3.12-slim

# Set environment variables to show output immediately (unbuffered)
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . /app

# Run the app (main.py)
CMD ["python", "main.py"]