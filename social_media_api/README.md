Social Media API

A backend API for a social media platform built with Django and Django REST Framework (DRF).
Supports user registration, login with token authentication, and a custom user model with followers.

User Authentication Flow
flowchart TD
A[User] --> B[POST /api/accounts/register/]
B --> C{Server}
C -->|Valid Data| D[Create CustomUser]
D --> E[Generate Token]
E --> F[Return User Data + Token]
C -->|Invalid Data| G[Return Error Response]

    H[User] --> I[POST /api/accounts/login/]
    I --> C2{Server}
    C2 -->|Valid Credentials| E2[Return Token]
    C2 -->|Invalid Credentials| G2[Return Error Response]

Explanation of Flow: 1. Registration (/api/accounts/register/):
-User sends username, email, and password.
-Server validates the input.
-If valid, creates a CustomUser and generates an authentication token.
-Returns user info + token.

    2. Login (/api/accounts/login/):
        -User sends username and password.
        -Server validates credentials.
        -If correct, returns the token for authenticated requests.

    3. Authenticated Requests:
        -Use the token in the Authorization header:

            Authorization: Token your-generated-token





                CustomUser Model Overview

| Field             | Type                   | Notes                                     |
| ----------------- | ---------------------- | ----------------------------------------- |
| `username`        | CharField              | Unique username                           |
| `email`           | EmailField             | User email                                |
| `password`        | CharField              | Stored as hashed password                 |
| `bio`             | TextField              | Optional user bio                         |
| `profile_picture` | ImageField             | Optional profile picture                  |
| `followers`       | ManyToManyField (self) | Users who follow this user (asymmetrical) |

                Setup & Testing
       1. Install dependencies:
            python -m ensurepip --upgrade
            python -m pip install --upgrade pip
            python -m pip install django djangorestframework djangorestframework-authtoken

        2. Make migrations:
            python manage.py makemigrations
            python manage.py migrate

        3. Create a superuser:
            python manage.py createsuperuser


        4. Run server:
            python manage.py runserver

        5. Test API:
        Test endpoints via Postman, Insomnia, or curl.


        ## User Follow & Feed Functionality

### Follow a User

POST /api/accounts/follow/<user_id>/
Headers:
Authorization: Token <token>

### Unfollow a User

POST /api/accounts/unfollow/<user_id>/

### User Feed

GET /api/posts/feed/
Returns posts from users the authenticated user follows, ordered by newest first.

POST /posts/<id>/like/
Likes a post and creates a notification for the post author.

GET /notifications/
Returns a list of notifications ordered by most recent.
