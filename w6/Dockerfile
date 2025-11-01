# Use an official Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy app files from your local machine to the container
COPY . /app

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for web access
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
