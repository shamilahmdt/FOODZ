# Foodz - Modern Food Delivery Platform

Foodz is a comprehensive food delivery and restaurant management platform built with Django. It features a robust backend for managing restaurants, menus, and orders, along with a customer-facing web interface and a REST API for mobile integration.

## 🚀 Features

### Customer Features
- **User Authentication**: Secure registration and login for customers.
- **Store Browsing**: Browse restaurants by category with ratings and delivery times.
- **Menu Management**: View food items, filter by veg/non-veg, and see detailed pricing.
- **Cart & Checkout**: Seamlessly add items to cart, apply coupon codes, and manage delivery addresses.
- **Order Tracking**: Real-time tracking of order status (Placed, Accepted, Prepared, Dispatched, Cancelled).
- **Address Management**: Save multiple addresses with landmark and geolocation support.

### Restaurant & Management Features
- **Dashboard**: Centralized management for store categories, sliders, and food items.
- **Order Lifecycle Management**: Managers can accept, reject, mark as prepared, and pick orders.
- **Inventory Control**: Create and update food categories and items per restaurant.
- **Offer System**: Manage promotional coupons and discounts (flat or percentage-based).

### Technical Features
- **REST API (v1)**: Dedicated API endpoints for customer authentication and address management using Django REST Framework.
- **JWT Authentication**: Secure token-based authentication for mobile/external clients.
- **Responsive Design**: Styled with Tailwind CSS for a modern, mobile-friendly user experience.
- **Custom User Model**: Extended authentication system to handle different user roles.

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **API**: Django REST Framework (DRF)
- **Database**: PostgreSQL (Default) / SQLite (Local)
- **Authentication**: JWT (via `djangorestframework-simplejwt`)
- **Frontend**: Django Templates + Tailwind CSS
- **Media**: Django File Storage for store and food item images.

## 📁 Project Structure

```text
foodz/
├── api/             # REST API implementation (v1)
├── customer/        # Customer-specific models and logic
├── restaurant/      # Restaurant, Store, and Food Item models
├── manager/         # Admin/Manager interface and dashboard
├── users/           # Custom User model and authentication
├── web/             # Frontend views and templates
├── static/          # CSS, JS, and image assets
├── templates/       # Global HTML templates
├── foodz/           # Project settings and configuration
└── manage.py        # Django management script
```

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL (optional, defaults can be switched to SQLite)
- Virtualenv

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd foodz/src/foodz
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary
   ```

4. **Database Configuration**:
   Update the `DATABASES` setting in `foodz/settings.py` with your PostgreSQL credentials or switch to SQLite for local development.

5. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

## 🔗 API Endpoints (v1)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/customer/login/` | POST | Customer login & JWT generation |
| `/api/v1/customer/register/` | POST | New customer registration |
| `/api/v1/customer/address/` | GET | List saved addresses |
| `/api/v1/customer/address/add/` | POST | Add a new delivery address |

## 📝 License

This project is licensed under the MIT License.
