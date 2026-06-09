# 📦 Warehouse & Delivery Management System

A Django-based management system for handling sellers, clients, orders, deliveries, and warehouse operations.

---

## 📖 About The Project

Warehouse & Delivery Management System is a web application developed with Django to streamline product distribution and order management processes.

The system allows administrators to manage sellers, clients, warehouse inventory, deliveries, and customer orders from a centralized platform.

This project was created as part of a Django examination project to demonstrate backend development and database management skills.

---

## ✨ Features

### 👥 User Management

* User Authentication
* Login & Logout
* User Roles Management

### 🏢 Seller Management

* Add Sellers
* Update Seller Information
* Delete Sellers
* View Seller Details

### 👤 Client Management

* Register Clients
* Manage Client Information
* View Client Records

### 📦 Warehouse Management

* Manage Product Storage
* Warehouse Inventory Tracking
* Product Availability Monitoring

### 🛒 Order Management

* Create Orders
* Update Orders
* Delete Orders
* Track Order Status

### 🚚 Delivery Management

* Schedule Deliveries
* Manage Delivery Records
* Track Delivery Status

---

## 🛠️ Technologies Used

* Python 3
* Django
* SQLite3
* HTML5
* CSS3
* Bootstrap
* Django ORM
* Django Templates

---

## 📂 Project Structure

```bash
Django-Exam-1/
│
├── client/
├── delivery/
├── order/
├── seller/
├── users/
├── werehouse/
│
├── config/
│
├── manage.py
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Django-Exam-1.git
cd Django-Exam-1
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
source venv/Scripts/activate
```

Linux / MacOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 📊 Main Modules

### Seller

Manages suppliers and sellers participating in the system.

### Client

Stores customer information and purchase records.

### Warehouse

Handles product storage and inventory operations.

### Order

Responsible for order creation, management, and tracking.

### Delivery

Controls shipment and delivery processes.

### Users

Provides authentication and authorization functionality.

---

## 🎯 Learning Objectives

This project demonstrates:

* Django Models & Relationships
* CRUD Operations
* Authentication System
* URL Routing
* Template Rendering
* Database Management
* Project Architecture
* Django Admin Customization

---

## 🚀 Future Improvements

* Product Management Module
* Real-Time Order Tracking
* Email Notifications
* REST API Integration
* Payment Gateway Integration
* Docker Deployment
* PostgreSQL Support

---

## 👨‍💻 Author

**Iqbola Toychiyeva**

Backend Developer | Django Developer

GitHub: https://github.com/Alisherovna-Iqbola0o1

---

## 📄 License

This project is created for educational and portfolio purposes.
