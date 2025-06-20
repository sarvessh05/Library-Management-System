# 📚 Library Management System

A **robust and user-friendly web-based application** built using **Python (Django)** to streamline library operations for both **librarians and members**. This system provides an intuitive interface for managing books, users, and transactions — all backed by a reliable SQLite3 database.

---

## 🛠️ Tech Stack

- **Backend**: Python, Django  
- **Frontend**: HTML, CSS (Tailwind or Bootstrap optional)  
- **Database**: SQLite3 (default with Django)

---

## 🚩 Features

### 📚 Book Management
- Add, update, delete, or view books  
- Real-time availability status of each book  
- (Optional) Search and category filters  

### 👥 User Roles & Permissions
- **Admin (Librarian)**:
  - Manage books and user accounts  
  - View and control issue/return records  
- **Member**:
  - Browse books  
  - Request and return books  

### 🔁 Issue & Return System
- Book issuing with due date assignment  
- Handles return transactions  
- Calculates overdue fines (if any)  

### 🔐 Authentication
- Secure login/logout system  
- Session-based authentication  
- Role-based access control (admin/member)  

### 📊 Dashboard
- Admin dashboard showing:
  - Total books, users  
  - Issued/returned book logs  
  - Overdue books  
  - Recent activity  

---

## 🧪 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/sarvessh05/Library-Management-System.git
cd Library-Management-System
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**

- On **macOS/Linux**:
```bash
source venv/bin/activate
```

- On **Windows**:
```bash
venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Apply migrations and run the server**
```bash
python manage.py migrate
python manage.py runserver
```

6. **Access the App**  
Open your browser and go to:
```
http://127.0.0.1:8000/
```
