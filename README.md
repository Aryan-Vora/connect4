# Connect4 Game

This repository contains a Connect4 game implementation with React as the frontend and Flask as the backend. This is for sure not the best way to make this but I was doing this just to learn.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Node.js and npm](https://nodejs.org/en/download/) (Node Package Manager)
- [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/)

## Installation

### Frontend

Navigate to the `frontend` directory:

```bash
cd frontend
```

Install the necessary npm packages:

```bash
npm install
```

### Backend

Navigate to the `backend` directory:

```bash
cd backend
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Application

### Running the Frontend

From the `frontend` directory, start the React development server by running:

```bash
npm run dev
```

This will launch the frontend on [http://localhost:5173](http://localhost:5173).

### Running the Backend

From the `backend` directory, start the Flask application by running:

```bash
python app.py
```

This will start the backend server, typically on [http://localhost:8080/](http://localhost:8080/).

## Usage

After starting both the frontend and backend servers, you can play the Connect4 game by navigating to [http://localhost:5173](http://localhost:5173) in your web browser.
