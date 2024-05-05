# Django Todo Application

# Getting Started

### 1. Set Up Virtual Environment (Optional) 🌐

It's a good practice to create a virtual environment for Python projects. This keeps your dependencies organized and separate from other projects.

For Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

For macOS and Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Clone The Repository And Setup

```bash
git clone https://github.com/Sakshamkhandelwal123/Django-Todo-App.git
```

### 3. Install Packages 💻

Install `pip` dependencies with the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Migration

Once you have downloaded all packages, go to the cloned repo directory and run the following commands

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Admin User

We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user

```bash
python manage.py createsuperuser
```

### 6. Run the application 🏃‍♂️

Run the app:

```
python manage.py runserver
```
