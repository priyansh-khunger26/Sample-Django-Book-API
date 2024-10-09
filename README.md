# Sample Django Book API

This is a simple Django application that provides a RESTful API for managing a collection of books. It allows you to perform CRUD (Create, Read, Update, Delete) operations on book records.

## Features

- Create a new book record
- Retrieve a list of all books
- Update an existing book record
- Delete a book record

## Requirements

- Python 3.x
- Django
- Django Rest Framework

## Setup Instructions

Follow these steps to set up and run the application on your local machine:

### 1. Clone the Repository

### 2, Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Apply Migrations

```bash
python manage.py migrate

```

### 4. Run the Development Server

```bash
python manage.py runserver

```

### 5. Access the API

Open your web browser or an API client (like Postman) and navigate to:

API endpoint: http://127.0.0.1:8000/api/books/
Admin site: http://127.0.0.1:8000/admin/ (if you created a superuser)



