# 🍽️ FoodieFinder

FoodieFinder is a Django-based web application designed to help users discover, explore, and manage food-related content in one place. It provides a simple interface for browsing food options, viewing details, and organizing information in a user-friendly way.

This project was built as a learning-focused full-stack web application using Python and Django, with an emphasis on clean architecture, database integration, and maintainable code.

## 🚀 Features

- Browse and explore food-related listings  
- View detailed pages for individual food items or locations  
- Admin dashboard for managing content  
- Database-backed models using SQLite  
- Modular Django app structure  

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite  
- **Version Control:** Git & GitHub  

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/jgarciav305/FoodieFinder.git
cd FoodieFinder
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

Activate it:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```

Then open:  
👉 http://127.0.0.1:8000/

## 🗂️ Project Structure

```
FoodieFinder/
├── foodsites/
├── homepages/
├── mytravel/
├── manage.py
├── db.sqlite3
└── README.md
```
