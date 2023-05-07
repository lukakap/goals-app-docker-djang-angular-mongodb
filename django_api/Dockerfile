# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV MONGODB_HOST=host.docker.internal

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Start the application
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_api.wsgi"]

# Django Development Server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]