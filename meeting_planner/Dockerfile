# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Verify Django installation (optional)
RUN pip show django

# Copy the rest of the application code into the container
COPY . /app/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create a non-root user and switch to it
RUN useradd -ms /bin/sh appuser
USER appuser

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "meeting_planner.wsgi:application"]
