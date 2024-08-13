# Use a Python image with Gunicorn installed
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app/

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "meeting_planner.wsgi:application"]
