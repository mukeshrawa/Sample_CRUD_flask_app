# Sample CRUD Flask App

This project is a simple Flask application for managing transaction records with basic CRUD functionality.

## Features

- View all transactions
- Add a new transaction
- Edit an existing transaction
- Delete a transaction
- Search transactions by amount range

## Tech Stack

- Python
- Flask
- Jinja2 templates
- Bootstrap for styling

## Project Structure

```text
Sample_CRUD_flask_app/
├── app.py
├── templates/
│   ├── transactions.html
│   ├── form.html
│   ├── edit.html
│   └── search.html
├── .gitignore
└── README.md
```

## Setup

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install flask
```

3. Run the application:

```bash
python app.py
```

4. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## How It Works

The app stores sample transaction data in memory and exposes routes for:

- `GET /` to list all transactions
- `GET /add` and `POST /add` to create a new transaction
- `GET /edit/<id>` and `POST /edit/<id>` to update a transaction
- `GET /delete/<id>` to remove a transaction
- `GET /search` to filter transactions by minimum and maximum amount

## Notes

This is a lightweight sample project intended for learning CRUD operations in Flask and basic template rendering.
