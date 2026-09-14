# 🌸 Sakura Café

### Japanese-Inspired Café Management System

**Developed by RUDHRA KARTHIKEYAN**

B.Tech – Artificial Intelligence and Data Science  
V.S.B Engineering College, Karur

---

> A little taste of Japan, served with warmth. 🌸☕
>
> ---

## 📌 Project Overview

Sakura Café is a web-based café management system built using
the Django framework and MySQL.

The application provides a centralized platform for managing
the core operations of a café, including products, customers,
and orders.

The project follows the CRUD architecture, allowing authorized
users to create, view, update, and delete records through a
simple and responsive web interface.

The application also includes user authentication, product
image uploads, database relationships, and a Japanese-inspired
café interface.

---

## ✨ Features

### 🔐 User Authentication

- User registration and account creation
- Secure login and logout
- Custom Django user model
- Password-based authentication
- Protected management pages

### ☕ Product Management

- Add new café products
- View all products
- Edit existing products
- Delete products
- Set product availability
- Upload product images
- Display product images in the menu

### 👥 Customer Management

- Add new customers
- View customer records
- Edit customer information
- Delete customers
- Store customer registration dates

### 🧾 Order Management

- Create new orders
- View all orders
- Edit existing orders
- Delete orders
- Associate orders with customers and products
- Store order number, date, and quantity

### 🌸 User Interface

- Japanese-inspired Sakura Café theme
- Responsive design
- Custom navigation bar
- Interactive product cards
- Styled authentication pages
- Customer management interface
- Orders management table
- Mobile-friendly layout

  ---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Django Templates

### Backend

- Python
- Django 5

### Database

- MySQL

### Development Tools

- Visual Studio Code
- Git
- GitHub

### Python Libraries

- Django
- django-bootstrap5
- mysqlclient
- Pillow

---

## 🏗️ Project Structure

```text
Fullstack_Cafe/
│
├── Cafe/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── OrderManagement/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── authentication/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
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


---

## 🗄️ Database Design

Sakura Café uses **MySQL** as its relational database.

The application contains the following main entities:

### Product

Stores the café menu items.

| Field | Description |
|---|---|
| Product Name | Name of the menu item |
| Category | Product category |
| Price | Product price |
| Availability | Whether the product is currently available |
| Picture | Uploaded product image |

### Customer

Stores café customer information.

| Field | Description |
|---|---|
| Customer Name | Name of the customer |
| Customer Since | Date the customer was added |

### Orders

Stores customer orders.

| Field | Description |
|---|---|
| Customer Reference | Customer associated with the order |
| Product Reference | Product associated with the order |
| Order Number | Unique order identifier |
| Order Date | Date of the order |
| Quantity | Quantity ordered |
| Amount | Order amount |
| GST Amount | GST applicable to the order |
| Bill Amount | Final bill amount |

### User

The authentication system uses a custom Django user model based on Django's `AbstractUser`.

Additional user information includes:

- Username
- First name
- Last name
- Email
- Age
- Password
