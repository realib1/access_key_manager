# Access Key Manager

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Folder Structure](#folder-structure)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## Overview
Access Key Manager is a Django-based web application that allows users to sign up, sign in, and reset their passwords. The project leverages Tailwind CSS for modern, responsive styling. Admin generates access keys for schools to be used
on their systems to get access to a school management system after paying for the key instead 
## Features
- User authentication (sign up, sign in, sign out)
- Password reset functionality
- Tailwind CSS for responsive UI
- Custom Django forms for authentication
- Access key generation and management

## Setup Instructions

### Prerequisites
- Python 3.x
- Django 3.x or higher
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/access-key-manager.git
   cd access-key-manager
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser to access the Django admin:**
   ```bash
      python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

### Setting Up Tailwind CSS

1. **Install Node.js and npm** if you haven't already. You can download it from [nodejs.org](https://nodejs.org/).

2. **Install Tailwind CSS pip:**
   ```bash
   python -m pip install django-tailwind
   ```

3. **For automatic reload install django-browser-reload:**
   ```bash
   python -m pip install 'django-tailwind[reload]'
   ```

4. **Add Tailwind to ```INSTALLED_APPS``` in ```settings.py```:**
   In your project's CSS file (e.g., `static/css/styles.css`), include the following:
   ```css
   INSTALLED_APPS = [
    # other Django apps
    'tailwind',
    ]
   ```

5. **Create a Tailwind CSS compatible Django app:**
    NOTE: default app name is ```theme```, enter the name you would like or press enter to continue, I used the default.
   ```bash
      python manage.py tailwind init
   ```

6. **Add your newly created ```'theme'``` app to ```INSTALLED_APPS``` in ```settings.py```:**
   ```bash
   INSTALLED_APPS = [
    # other Django apps
    'tailwind',
    'theme'
    ]
   ```

7. **Register the generated ```'theme'``` app by adding the following line to ```settings.py``` file:**
   ```bash
   INSTALLED_APPS = [
    # other Django apps
    'tailwind',
    'theme'
    ]
   ```
8. **Make sure that the ```INTERNAL_IPS``` list is present in the ```settings.py``` file and contains the ```127.0.0.1``` ip address**
   ```bash
    INTERNAL_IPS = [
    "127.0.0.1",
    ]
   ```
9. **Install Tailwind CSS dependencies, by running the following command**
   ```bash
    python manage.py tailwind install
   ```
9. **Finally, Start the Tailwind CSS development server by running the following command in your terminal:**
   ```bash
    python manage.py tailwind start
   ```

## Running the Project

To start the development server, run:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the application.

## Folder Structure

```
access_key_manager/
│
├── key_manager/
│   ├── migrations/
|   ├── static
|   |   ├── js
|   |   |   ├── man.js
│   ├── templates/
│   │   ├── keymanager/
│   │   │   ├── password_reset_form.html
│   │   │   ├── password_reset_done.html
│   │   │   ├── password_reset_confirm.html
│   │   │   ├── password_reset_complete.html
│   │   │   ├── signin.html
│   │   │   ├── signup.html
│   │   ├── base.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│
├── access_key_manager/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Usage

### User Authentication

- **Sign Up:** Users can sign up for a new account.
- **Sign In:** Existing users can sign in.
- **Password Reset:** Users can reset their password if they forget it.

### Tailwind CSS Styling

All forms are styled using Tailwind CSS classes. Ensure you've run the Tailwind build process to generate the necessary CSS.

## Technologies Used

- **Django:** Backend framework
- **Tailwind CSS:** Frontend styling
- **HTML5:** Markup language
- **JavaScript:** Interactivity


## ER Diagram of the Database Design
To design an Entity-Relationship (ER) diagram for the Access Key Manager project, we need to identify the entities and their relationships based on the project requirements and functionalities. Since this project is primarily focused on user authentication and password management, the entities and relationships will be straightforward.

### Entities
1. **User**: This entity represents users of the application.
2. **PasswordReset**: This entity represents password reset requests made by users.

### Attributes
1. **User**:
   - `id`: Primary Key
   - `username`: Unique identifier for the user
   - `email`: Email address of the user
   - `password`: Hashed password of the user
   - `first_name`: First name of the user
   - `last_name`: Last name of the user

2. **PasswordReset**:
   - `id`: Primary Key
   - `user_id`: Foreign Key referencing `User`
   - `reset_token`: Unique token for password reset
   - `created_at`: Timestamp of when the reset request was created
   - `used`: Boolean indicating whether the reset request has been used

### Relationships
- **User** to **PasswordReset**: One-to-Many (One user can have many password reset requests)

### ER Diagram

Here's a textual representation of the ER diagram:

```
+-------------------+     +-------------------+
|       User        |     |   PasswordReset   |
+-------------------+     +-------------------+
| id (PK)           |<----| id (PK)           |
| username          |     | user_id (FK)      |
| email             |     | reset_token       |
| password          |     | created_at        |
+-------------------+     | used              |      
                          +-------------------+

```



![ER Diagram]()
