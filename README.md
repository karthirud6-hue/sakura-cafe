# 🌸 Sakura Café

A Japanese-inspired café management system developed as a **Full Stack CRUD Project** using Django and MySQL.

Sakura Café provides a simple and elegant interface for managing café products, customers, and orders while demonstrating the core concepts of a full-stack web application.

---

## 📌 Project Overview

**Sakura Café** is a web-based café management application built using the Django framework.

The application allows users to:

- Manage café products
- Upload product images
- Manage customers
- Manage orders
- Create, update, and delete records
- Register and authenticate users
- Access protected management pages after login

The project combines a Japanese-inspired user interface with a functional CRUD-based backend.

---

## ✨ Features

### 🔐 User Authentication

- User registration
- User login
- User logout
- Custom Django user model
- Password authentication
- Protected customer and order management pages

### ☕ Product Management

- Add new products
- View all products
- Update product details
- Delete products
- Set product availability
- Upload product images
- Display product images on the menu

### 👥 Customer Management

- Add customers
- View customer records
- Update customer information
- Delete customers
- Store customer registration dates

### 🧾 Order Management

- Create orders
- View all orders
- Update orders
- Delete orders
- Select customers and products
- Store order number, date, and quantity

### 🌸 User Interface

- Japanese-inspired Sakura Café theme
- Responsive layout
- Custom navigation bar
- Hero section
- Product cards
- Customer management interface
- Orders table
- Styled authentication pages
- Responsive mobile design

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- Bootstrap 5

### Backend

- Python
- Django

### Database

- MySQL

### Other

- Django ORM
- Django Forms
- Django Authentication
- Django File/Image Uploads
- Git & GitHub

---

## 🏗️ Project Structure

```text
Fullstack_Cafe/
│
├── Cafe/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── OrderManagement/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── authentication/
│   ├── migrations/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── Fullstack_Cafe/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── assets/
│   └── css/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── products.html
│   ├── products_add.html
│   ├── customers.html
│   ├── customers_add.html
│   ├── orders.html
│   ├── orders_add.html
│   ├── navbar.html
│   └── footer.html
│
├── manage.py
├── .gitignore
└── README.md
