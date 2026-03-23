# Simple Login System

A beginner-friendly web authentication system built with Flask, featuring user registration, login, password hashing with bcrypt, and input validation.

## Features

- User registration and login
- Password hashing using bcrypt
- Client-side and server-side input validation
- SQLite database for user storage
- Clean, responsive UI
- Session management

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite
- **Password Hashing**: Flask-Bcrypt
- **Frontend**: HTML, CSS, JavaScript

## Setup Instructions

1. **Install Python** (if not already installed)
   - Download from [python.org](https://python.org)
   - Make sure to check "Add Python to PATH" during installation

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Open in Browser**
   - Navigate to `http://127.0.0.1:5000/`

## Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html
│   ├── welcome.html
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
└── static/               # Static files
    ├── css/
    │   └── style.css
    └── js/
        └── validation.js
```

## How It Works

1. **Registration**: Users can create accounts with username, email, and password
2. **Validation**: Both client-side (JavaScript) and server-side (Python) validation
3. **Password Security**: Passwords are hashed using bcrypt before storage
4. **Login**: Users authenticate with username and password
5. **Session Management**: Flask sessions keep users logged in
6. **Dashboard**: Protected page showing user information

## Security Features

- Password hashing with bcrypt
- Input sanitization and validation
- SQL injection prevention with parameterized queries
- Session-based authentication
- CSRF protection (Flask-WTF not implemented but SECRET_KEY set)

## Demo

1. Start the app
2. Visit the home page
3. Click "Sign Up" to create an account
4. Fill out the registration form
5. Login with your credentials
6. View your dashboard
7. Logout when done

This is a basic implementation suitable for learning purposes. For production use, additional security measures would be needed.