## Africana Ecommerce 🛍️

Africana Ecommerce is a fully functional **Django-based** e-commerce platform originally developed as an academic project. It has been refactored and structured to align with **industry best practices** using the **monolithic approach**, while maintaining flexibility for future scaling.

> ⚙️ A clean and modular project to showcase practical knowledge of Django, good software design, and real-world e-commerce logic.

---

### 🎯 Project Objective

This project was built to:

- Demonstrate mastery of **core Django features**
- Apply **SOLID principles** to Django monoliths
- Simulate a **real-world ecommerce platform**
- Lay a foundation for future **DRF/React** decoupling

---

### ✅ Core Features

- 🛍️ Product browsing, search, and filtering
- 🛒 Add to cart, update cart, remove items
- 📦 Checkout workflow with order summary
- 👤 User authentication and profile management
- 🧾 Order tracking (per user)
- 📧 Contact form functionality
- 🛠️ Admin customization for product & order management
- 📦 M-PESA & Stripe Payment Integration | Daraja Sandbox & Stipe Test mode

---

### ⚙️ Tech Stack

| Layer        | Tech                  |
|--------------|------------------------|
| Backend      | Django (Python)        |
| Frontend     | Django Templates (DTL) |
| Database     | SQLite (dev), PostgreSQL ready |
| Auth         | Django-Allauth   |
| Admin Panel  | Customized Django Admin |
| Styling      | Bootstrap / Custom CSS |
| Env Config   | `python-decouple`      |

---


---

### 🚀 Getting Started

#### 1. Clone & Set Up

```bash
git clone https://github.com/LeonardOgendo/Africana-Ecommerce.git africana-ecommerce
cd africana-ecommerce
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/base.txt
```

#### 2. Configure .env

```ini
DEBUG=True
SECRET_KEY=your_django_secret
ALLOWED_HOSTS=127.0.0.1,localhost
```


#### 3. Migrate & Seed Database

```bash
python manage.py migrate
python manage.py createsuperuser
```

#### 4. Start the Server

```bash
python manage.py runserver
```

---

### 🔮 Future Enhancements

- MPESA & Stripe Payment Gateway Integration via Daraja Sandbox and Stripe Test mode



---

### 🧠 Learning Outcomes

This project allowed me to:

  - Structure Django projects using industry-grade patterns

  - Customize and extend Django Admin

  - Write reusable templates using DTL

  - Apply SOLID and DRY principles in a Django monolith

  - Handle real-world ecommerce workflows

