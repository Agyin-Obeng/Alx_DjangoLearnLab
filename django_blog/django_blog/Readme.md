# Authentication System - django_blog

## Overview

This project uses Django's built-in authentication system with a small custom registration form (adds email) and a profile edit feature (email update).

## Files added/changed

- `blog/forms.py` - custom RegisterForm (extends UserCreationForm).
- `blog/views.py` - home view, register, login_view, logout_view, profile (with POST handling).
- `blog/urls.py` - app URLs for login/logout/register/profile.
- `blog/templates/base.html` - replaced nav and added messages block.
- `blog/templates/blog/register.html` - registration page.
- `blog/templates/blog/login.html` - login page.
- `blog/templates/blog/profile.html` - profile view + update.

## How it works

- Registration uses `RegisterForm` to collect username, email, and password; on success the user is logged in.
- Login uses `AuthenticationForm`.
- Logout uses Django's `logout()` and redirects to home.
- Profile view requires login and allows updating the user's email via POST.

## How to test

1. Run server: `python manage.py runserver`.
2. Create a user at `/register/`.
3. After signup you should be redirected to `/` and be logged in.
4. Visit `/profile/` to see or update your email.
5. Try `/logout/` and then `/profile/` — you should be redirected to login.

## Security notes

- CSRF tokens are present on all forms.
- Passwords are stored via Django's secure hashing mechanism (no plain-text).
- For production, set `DEBUG=False`, configure `ALLOWED_HOSTS`, and use HTTPS.
