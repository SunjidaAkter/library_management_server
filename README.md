# Live Link: [Library Management Server](https://library-management-server-tp1n.vercel.app/)

## Overview

The **Bookit** Library Management Project Backend serves as a comprehensive backend platform tailored for efficient management of a library system. Built with **Django** and **Django REST Framework**, it supports smooth interactions between `reader` (Reader) and `library admin` (Admin) roles, ensuring a user-friendly and feature-rich experience.

he project allows library admins to create, update, and manage books and authors, handle borrow orders, and oversee customer feedback, while customers can browse the books, borrow books, and track their borrowing history. Key features include role-based access control, borrow order tracking, and notification functionalities, enhancing the overall user experience for both readers and admins.

Powered by **PostgreSQL** the backend offers robust data management and scalability, preparing it for future expansions and upgrades. This architecture makes **Bookit**  a reliable solution for managing a dynamic and growing library.

---

<br>

## Features

- **Admin Capabilities**:
  - Create, update, and manage books.
  - Process and track reader borrowing orders.
  - View and respond to reader feedback.

- **Reader Capabilities**:
  - Browse the book and view book details.
  - Place borrowing orders and track order status.
  - Return borrowing books and track the record.
  - Access account details and order history.

- **Additional Features**:
  - Role-based access control to secure different user operations.
  - Real-time order tracking and notifications.
  - Support for future feature enhancements.

 ---

 <br>

 ## Tech Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: PostgreSQL(Using Supabse Deployment)
  - Ensures reliable data handling, scalability, and flexibility for future improvements.

---

<br>

## Instructions to Run Locally

### Prerequisites

- Python 3.12.2
- Django 4.2.4
- Django REST Framework 3.15.2
- PostgreSQL

### Packages used:

- **Django**: v5.1.2
- **Django REST Framework**: v3.15.2 
- **PostgreSQL**: v2.9.10 (psycopg2-binary)
- **django-cors-headers**: v4.5.0 
- **django-environ**: v0.11.2 
- **requests**: v2.32.3 
- **whitenoise**: v6.7.0
- **pillow**: v11.0.0 
- **JWT**: v8.5.1 


## Getting Started

1. Open `command prompt` in the folder directory where you want to create & run the project locally

2. Copy the `repository_url` to **Clone the repository**

   ```bash
   git clone https://github.com/SunjidaAkter/library_management_server.git
   cd library_management_server
   ```

3. **Create a virtual environment**

   ```bash
   python -m venv library_venv
   cd library_venv
   Scripts\activate.bat
   cd ..
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   code .
   ```

<br>


5. **Then, add the `SECRET_KEY` in that `.env` file:**

- SECRET_KEY=(Your SECRET_KEY)

       to get the `SECRET_KEY`, Temporarily `Create a new project` named `library_management_server` anywhere `outside the current project directory` (may be in the `desktop`, `documents` or `downloads`, wherever you want, just outside the current project directory)

- Copy the `secret key` from the temporarily created project's `temp_settings.py` file

<br>

6. **Add the supabase postgreeSQL database credentials** in `.env` file:

- DB_NAME=(Your database name)
- DB_USER=(Your database username)
- DB_PASSWORD=(Your database password)
- DB_HOST=(The host for your database)
- DB_PORT=(The port for your database)



<br>

7. **Also, Add the email sending accessibility credentials** in `.env` file:

- EMAIL: (Your email address for sending emails)
- EMAIL_PASSWORD: (Your email password or an app-specific password)

 
<br>

8. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

9. **Creating superuser**

```bash
python manage.py createsuperuser
```

10. **Run the development server**

```bash
python manage.py runserver
```

<br>

11. **Finally, Access the application**

- Local: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/login/

---

<br>


## API Endpoints

| Endpoint            | Method | Description                     |
|-----------------------------|--------|---------------------------------|
| `/book/list/`               | POST   | Create Book Item                |
| `/book/list/`               | GET    | List all book items             |
| `/book/list/<id>/`          | GET    | Retrieve a specific book item   |
| `/book/list/<id>/`          | DELETE | Delete a specific book item     |
| `/book/list/<id>/`          | PATCH  | Update a specific book item     |
| `/borrow/`                  | POST   | Place a new borrow order        |
| `/borrow/<id>/`             | PATCH  | Update an existing borrow order |
| `/borrow/<id>/`             | DELETE | Delete an existing borrow order |
| `/users/<id>/`              | GET    | Retrieve user details           |
| `/users/`                   | GET    | Retrieve all users              |
| `/user_account/list/`       | POST   | Create useraccount              |
| `/user_account/list/`       | GET    | Retrieve all useraccounts       |
| `/user_account/list/<id>/`  | GET    | Retrieve useraccount Detail     |
| `/user_account/list/<id>/`  | DELETE | Delete useraccount              |
| `/user_account/list/<id>/`  | PATCH  | Update a specific useraccount   |

---

<br>


# Conclusion

In developing the BookIt Library Management System backend, the goal was to create a streamlined, secure platform for managing book inventory, lending, and user interactions. Leveraging Django and PostgreSQL provides a reliable and scalable foundation, supporting smooth transactions between library staff and patrons.

With features like role-based access, book tracking, and lending management, this system aims to enhance the library experience for users and optimize operational workflows. I’m excited about the value it can bring to libraries, and if you have any questions or would like to contribute, please don’t hesitate to reach out!
