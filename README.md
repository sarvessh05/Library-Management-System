# 📚 Library Management System

A Django-based web application to manage library operations such as student registrations, book issue/return tracking, and admin-level controls — all through a responsive and secure interface.

---

## 🚀 Features

- 👤 **Student & Admin Login**
- 📚 **Book Inventory Management**
- 🔄 **Issue / Return Book Tracking**
- 🔐 **Authentication & Authorization**
- 📩 **Email Notifications (configurable)**
- 📊 **Dashboard for Admin Overview**
- 📅 **Due Date Management**

---

## 🛠 Tech Stack

- **Backend**: Django 3.2+
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default), configurable to PostgreSQL
- **Deployment**: Render

---

## 📂 Project Structure

```
Library-Management-System/
│
├── library/                   # App for core library logic
├── librarymanagement/        # Django project settings and URLs
├── templates/                # HTML templates
├── static/                   # Static assets (CSS, JS, images)
├── db.sqlite3                # SQLite database
├── manage.py                 # Django project manager
├── requirements.txt          # Python package requirements
└── README.md                 # Project documentation
```

---

## ⚙️ Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Library-Management-System.git
   cd Library-Management-System
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   Open `http://127.0.0.1:8000` in your browser.

---

## 🌐 Deployment on Render

Make sure you:

- Set environment variable `DJANGO_SETTINGS_MODULE=librarymanagement.settings`
- Use `gunicorn librarymanagement.wsgi:application` as start command
- Set Python version (e.g., 3.10)
- Add `staticfiles` as the static publish path
- Collect static files before deployment:
  ```bash
  python manage.py collectstatic
  ```

---

## 📧 Email Configuration (Optional)

To enable email notifications (e.g., for password reset), configure these in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
```

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ by **Sarvesh Ghotekar**  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/sarveshghotekar/) or [contact](https://sarvessh05.github.io/Portfolio/contact.html) page on my [portfolio](https://sarvessh05.github.io/Portfolio/)
