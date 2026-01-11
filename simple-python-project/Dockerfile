# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the required Python packages
RUN pip install flask

# Expose port 8080 for the Flask app
EXPOSE 8080

# Command to run the Flask app
CMD ["python", "app.py"]