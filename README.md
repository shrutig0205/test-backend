# test-backend
# FastAPI Project

This project is a simple REST API built with FastAPI, Dockerized for easy deployment.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running with Docker](#running-with-docker)
- [Testing the API](#testing-the-api)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project provides a simple REST API to create items. It's built using FastAPI and can be easily deployed using Docker.

## Requirements

- Python 3.8+
- Docker
- Docker Compose (optional, for multi-container setups)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/shrutig0205/test-backend.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the FastAPI application locally:

1. Start the FastAPI server:

    ```sh
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to see the API documentation automatically generated by FastAPI.

## API Endpoints

### POST /items/

Create a new item.

- **URL**: `/items/`
- **Method**: `POST`
- **Headers**: 
  - `Content-Type`: `application/json`
- **Body**:
  ```json
  {
    "name": "Sample Item",
    "description": "A sample item description",
    "price": 25.5,
    "tax": 1.5
  }

Docker
1. Build the Docker image:
docker build -t yourdockerhubusername/myfastapi .

2. Run the Docker container:
docker run -d -p 80:80 yourdockerhubusername/myfastapi
Access the application at http://0.0.0.0:8000

Postman

Create a new POST request to http://0.0.0.0:8000/items/.

Set the Content-Type header to application/json.

Add the request body:
{
  "name": "Sample Item",
  "description": "A sample item description",
  "price": 25.5,
  "tax": 1.5
}


### Step 3: Push the README.md to Your Git Repository

1. **Add the README.md to Your Git Repository**:

    ```sh
    git add README.md
    ```

2. **Commit Your Changes**:

    ```sh
    git commit -m "Add API documentation"
    ```

3. **Push to Remote Repository**:

    ```sh
    git push origin main
    ```

