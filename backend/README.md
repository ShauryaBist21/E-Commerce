# E-Commerce Backend API

A Django REST Framework backend for the E-Commerce application with JWT authentication.

## Features

- **Custom User Model**: Extended Django's AbstractUser with email authentication
- **JWT Authentication**: Secure token-based authentication
- **User Registration & Login**: Complete authentication flow
- **Profile Management**: User profile CRUD operations
- **Password Management**: Change password functionality
- **Admin Interface**: Django admin integration
- **CORS Support**: Cross-origin resource sharing enabled

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository and navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`

## API Endpoints

### Authentication Endpoints

#### Register User
- **URL:** `POST /api/auth/register/`
- **Description:** Register a new user
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "username": "username",
    "password": "securepassword123",
    "password2": "securepassword123",
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "+1234567890",
    "address": "123 Main St, City, Country",
    "is_customer": true,
    "is_merchant": false
  }
  ```
- **Response:**
  ```json
  {
    "message": "User registered successfully",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
      "id": 1,
      "username": "username",
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "is_customer": true,
      "is_merchant": false
    }
  }
  ```

#### Login User
- **URL:** `POST /api/auth/login/`
- **Description:** Authenticate user and get JWT tokens
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword123"
  }
  ```
- **Response:**
  ```json
  {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
      "id": 1,
      "username": "username",
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "is_customer": true,
      "is_merchant": false
    }
  }
  ```

#### Refresh Token
- **URL:** `POST /api/auth/login/refresh/`
- **Description:** Get new access token using refresh token
- **Request Body:**
  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

#### Logout User
- **URL:** `POST /api/auth/logout/`
- **Description:** Logout user and blacklist refresh token
- **Headers:** `Authorization: Bearer <access_token>`
- **Request Body:**
  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

#### Check Authentication
- **URL:** `GET /api/auth/check-auth/`
- **Description:** Check if user is authenticated
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
    "authenticated": true,
    "user": {
      "id": 1,
      "username": "username",
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "is_customer": true,
      "is_merchant": false
    }
  }
  ```

### User Profile Endpoints

#### Get/Update Profile
- **URL:** `GET/PUT/PATCH /api/auth/profile/`
- **Description:** Retrieve or update user profile
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
    "id": 1,
    "email": "user@example.com",
    "username": "username",
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "+1234567890",
    "address": "123 Main St, City, Country",
    "profile_image": null,
    "is_customer": true,
    "is_merchant": false
  }
  ```

#### Change Password
- **URL:** `PUT /api/auth/change-password/`
- **Description:** Change user password
- **Headers:** `Authorization: Bearer <access_token>`
- **Request Body:**
  ```json
  {
    "old_password": "currentpassword",
    "new_password": "newpassword123"
  }
  ```

### Admin Endpoints

#### User Statistics
- **URL:** `GET /api/auth/stats/`
- **Description:** Get user statistics (admin only)
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
    "total_users": 100,
    "users_created_today": 5,
    "users_created_this_week": 25,
    "recent_users": [...]
  }
  ```

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the access token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Invalid credentials or missing token
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

### Django Admin
Access the admin interface at `http://localhost:8000/admin/`

## Configuration

Key settings in `settings.py`:

- **Database**: SQLite3 (development)
- **JWT Settings**: 30-minute access tokens, 1-day refresh tokens
- **CORS**: Enabled for development
- **Custom User Model**: `accounts.CustomUser`

## Security Features

- Password validation using Django's built-in validators
- JWT token blacklisting for logout
- CORS protection
- CSRF protection
- Secure password hashing

## Production Deployment

For production deployment:

1. Set `DEBUG = False`
2. Configure a production database (PostgreSQL recommended)
3. Set a secure `SECRET_KEY`
4. Configure proper CORS settings
5. Use environment variables for sensitive data
6. Set up proper logging
7. Configure static file serving