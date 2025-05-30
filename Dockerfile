# Use Python base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Set PYTHONPATH so Python can find model and app modules
ENV PYTHONPATH=/app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app/app.py"]

