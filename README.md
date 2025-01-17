# Feedback Management System

A simple Feedback Management System built with FastAPI for the backend and HTML/CSS/JavaScript for the frontend. This application allows users to create surveys and submit responses, providing a platform for collecting and managing feedback.

## Features
- Create surveys with multiple questions.
- Submit responses to surveys.
- View success messages upon submission.
- Simple and user-friendly interface.

## Technologies Used
- **Backend**: FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB
- **Deployment**: Uvicorn (for local development)

## Installation

### Prerequisites
- Python 3.7 or higher
- MongoDB installed and running

### Steps to run:

-Set Up the Backend: Navigate to the Main directory and install the required Python packages:

### pip install -r requirements.txt

-Start the MongoDB Server: Ensure that your MongoDB server is running. You can start it using the following command (if you have MongoDB installed locally)

### mongod

-Run the FastAPI Backend: Start the FastAPI server using Uvicorn

### uvicorn main:app --reload

-Open the Frontend:
Open your web browser and navigate to the following URL to access the frontend
### http://localhost:8000/frontend/index.html

