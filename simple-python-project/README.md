# Simple Python Project

This project is a simple web application built using Flask. It serves a basic "Hello, World!" response and runs on port 8080.

## Project Structure

```
simple-python-project
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Requirements

- Docker
- Python 3.x

## Getting Started

To build and run the Docker container for this application, follow these steps:

1. Clone the repository:

   ```
   git clone <repository-url>
   cd simple-python-project
   ```

2. Build the Docker image:

   ```
   docker build -t simple-python-app .
   ```

3. Run the Docker container:

   ```
   docker run -p 8080:8080 simple-python-app
   ```

4. Access the application:

   Open your web browser and go to `http://localhost:8080`. You should see the message "Hello, World!".
