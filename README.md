
# 📚 Book Hive

**Book Hive** is a Django-based web application for managing and exploring a collection of books. It includes features for user management, admin control, and book listings.

---

## 🚀 Features

- User registration and login
- Admin dashboard for book management
- Book listing and details view
- Media uploads (images for books, etc.)
- Static file handling
- Role-based access control

---

## 🛠️ Technologies Used

- Python 3
- Django
- SQLite3 (default development database)
- HTML/CSS (with Django templating)
- Bootstrap (if used in assets)
- JavaScript (optional)

---

## 🗂️ Project Structure

```
book_hive/
│
├── manage.py
├── db.sqlite3
├── admins/         # Admin-side app
├── users/          # User registration and profile app
├── book_hive/      # Django project config (settings, urls, wsgi)
├── static/         # Static assets like CSS, JS, etc.
├── media/          # Uploaded media files (images, docs)
└── assets/         # Extra design or front-end assets
```

---

## 🔧 Setup Instructions

1. **Clone or extract the project:**

   ```bash
   git clone <repo-url>
   cd book_hive
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt  # Create this file manually if not present
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. Open in browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📸 Screenshots

_Add screenshots here (optional)_

---

## 📬 Contact

For questions, reach out at [your-email@example.com]  
Or connect via LinkedIn/GitHub.
