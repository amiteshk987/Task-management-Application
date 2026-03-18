# Task Management Application

A simple Django-based Task Management Application with MVC architecture, supporting CRUD operations, search functionality, and a clean Bootstrap UI.

## Overview

This application allows users to manage their tasks with the following features:
- Create, Read, Update, Delete tasks
- Search tasks by title or description
- User authentication
- REST API endpoints
- Clean and responsive UI using Bootstrap

## Detailed Task View

The detail view provides a comprehensive look at individual tasks:
- Full task information: title, description, status, due date, remarks
- Timestamps: created_on, last_updated_on
- User info: created_by, last_updated_by
- Action buttons: Edit, Delete, Back to list
- Responsive design for mobile/desktop

Users can click on a task from the list to view details and perform updates or deletions directly.

## Features

- **Task Management**: Full CRUD operations for tasks
- **User Authentication**: Login/logout functionality
- **Search**: Search tasks by title or description
- **REST API**: API endpoints for programmatic access
- **Responsive UI**: Clean Bootstrap-based interface

## Tech Stack

- **Backend**: Python 3.14, Django 5.1
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite
- **API**: Django REST Framework

## Setup Instructions

### Prerequisites
- Python 3.14 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project** (if not already done)

2. **Navigate to the project directory**:
   ```bash
   cd path/to/taskmanagement
   ```

3. **Install dependencies**:
   ```bash
   pip install django djangorestframework
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

## Build & Run Steps

### Development Server
1. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

2. **Access the application**:
   - Web UI: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API: http://127.0.0.1:8000/api/tasks/

### Login
- Use the superuser credentials created above to log in.
- Or create regular users via the admin panel.

## Dependencies

- Django==5.1.1
- djangorestframework==3.15.2
- Bootstrap 5 (CDN)

## API Endpoints

The application provides REST API endpoints:

- `GET /api/tasks/` - List all tasks for the authenticated user
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a specific task
- `PUT /api/tasks/{id}/` - Update a specific task
- `DELETE /api/tasks/{id}/` - Delete a specific task

### API Authentication
Use Django's session authentication or token authentication for API access.

## MVC Structure

- **Model**: `Task` model in `tasks/models.py` handles data structure and database interactions
- **View**: Functions in `tasks/views.py` handle request processing and response generation
- **Controller**: Django's URL dispatcher routes requests to appropriate views
- **Templates**: HTML templates in `templates/` directory for rendering UI

## Database Schema

### Task Table
- `id` (Primary Key, Auto-increment)
- `title` (CharField, max 200 chars)
- `description` (TextField)
- `due_date` (DateField)
- `status` (CharField, choices: 'Pending', 'In Progress', 'Completed')
- `remarks` (TextField, optional)
- `created_on` (DateTimeField, auto_now_add)
- `last_updated_on` (DateTimeField, auto_now)
- `created_by` (ForeignKey to User)
- `last_updated_by` (ForeignKey to User)

## Sample Data

After setup, you can create sample tasks through the web UI or API. A sample task is created during initial setup.

Example task data:
- Title: "Sample Task"
- Description: "This is a sample task"
- Due Date: 2026-03-25
- Status: Pending

## Folder Structure

```
taskmanagement/
├── taskmanagement/          # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── tasks/                  # Tasks app
│   ├── __init__.py
│   ├── admin.py           # Admin configuration
│   ├── api_views.py       # REST API views
│   ├── apps.py
│   ├── forms.py           # Django forms
│   ├── models.py          # Database models
│   ├── serializers.py     # API serializers
│   ├── tests.py
│   ├── urls.py            # App URL configuration
│   └── views.py           # Web views
├── templates/             # HTML templates
│   ├── base.html
│   ├── registration/
│   │   └── login.html
│   └── tasks/
│       ├── task_list.html
│       ├── task_form.html
│       └── task_confirm_delete.html
├── static/                # Static files
│   └── css/
│       └── style.css
├── db.sqlite3            # SQLite database
├── manage.py            # Django management script
└── README.md            # This file
```

## Troubleshooting

- **Migration issues**: Run `python manage.py makemigrations` and `python manage.py migrate`
- **Static files not loading**: Ensure `DEBUG=True` in settings.py for development
- **Login issues**: Check user credentials or create a new user via admin
- **API access**: Ensure authentication headers are included in requests

## License

This project is for educational purposes.

