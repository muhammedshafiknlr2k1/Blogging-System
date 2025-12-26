📝 Django Blogging System

A complete blogging system built using Django, designed to demonstrate real-world backend development concepts such as authentication, role-based access, CRUD operations, search, comments, and admin management.

This project follows a practical, industry-oriented approach and reflects how modern blogging platforms are structured and implemented.

📖 Project Description

The Django Blogging System is a full-stack web application that allows users to create, manage, and interact with blog content.
It supports multiple user roles, secure authentication, category-based blogs, comments, and an admin dashboard for managing the entire system.

The project is built with clean Django architecture using:

Models for database structure

Views for business logic

Templates for UI rendering

URLs for routing

Django Admin for backend management

🛠 Technologies Used

Programming Language: Python

Framework: Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django DB)

Version Control: Git & GitHub

✨ Features Explained
🔐 Authentication & Authorization

User registration and login system

Secure session-based authentication

Logout functionality

Role-based access control

👤 User Roles

Admin

Full access to the system

Manage users, categories, posts, and comments

Author

Create, update, and delete their own blog posts

View comments on their posts

Normal User

View blog posts

Search blogs

Add comments

📝 Blog Management

Create new blog posts

Edit existing blog posts

Delete blog posts

Upload featured images

Assign categories to posts

Display blogs in structured format

🗂 Category Management

Create multiple blog categories

Display blogs category-wise

Easy filtering and organization of content

🔍 Search Functionality

Search blog posts using keywords

Search based on blog title or content

Improves user experience and accessibility

💬 Comment System

Logged-in users can add comments

Comments displayed under each blog post

Admin can manage or moderate comments

🧑‍💼 Admin Dashboard

Django Admin customization

Manage users and permissions

Manage blog posts and categories

Moderate comments

View all application data from a single dashboard

🗂 Project Structure
blogging_system/
│
├── blog/                # Blog application (models, views, urls)
├── accounts/            # User authentication & roles
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── media/               # Uploaded blog images
├── db.sqlite3           # Database file
├── manage.py
└── requirements.txt

⚙️ How to Run the Project Locally
Step 1: Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Step 2: Create Virtual Environment
python -m venv venv

Step 3: Activate Virtual Environment

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

Step 4: Install Dependencies
pip install -r requirements.txt

Step 5: Apply Migrations
python manage.py makemigrations
python manage.py migrate

Step 6: Create Superuser
python manage.py createsuperuser

Step 7: Run Server
python manage.py runserver


Open browser and visit:
👉 http://127.0.0.1:8000/

Admin panel:
👉 http://127.0.0.1:8000/admin/

📚 Learning Outcomes

This project helped me gain strong hands-on experience in:

Django project structure

Django ORM and database relationships

Authentication and authorization

Template inheritance

CRUD operations

Admin customization

GitHub version control
