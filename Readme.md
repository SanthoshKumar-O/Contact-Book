# 📒 Django Contact Book Application

A simple **Contact Book** web app built using **Django**.  
It allows users to **add, view, search, update, and delete** contacts securely with specified data foe each user through validation.

---

## 🌐 Live Demo
🔗 [View Live Project on Render](https://contact-book-vbz7.onrender.com)


## 🚀 Features

- 👤 User authentication (Login / Logout / Register)
- ➕ Add new contacts with validation
- 🔍 Search contacts by name or number
- ✏️ Update existing contact details
- ❌ Delete contacts safely with confirmation
- ⚠️ Real-time form validation and helpful error messages
- 🔒 Each user’s contacts are private and isolated

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Django (Python 3.x) |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite (default Django DB) |
| Authentication | Django’s built-in `User` model |
| Alerts | Django `messages` framework |
| Hosting | Render |

---

##  Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/contact-book.git
   cd contact-book
   cd contact
   python manage.py runserver
