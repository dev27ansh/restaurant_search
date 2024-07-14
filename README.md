# Restaurant Search Application

This is a Django-based web application that allows users to search for dishes by name and get recommendations for the best match.

 The application includes an admin interface for managing the dishes database.

## Features

- Search for dishes by name
- Admin interface for managing dishes
- Uses SQLite as the database
- Implements Django Crispy Forms for elegant form rendering


## Installation

1. Clone the repository:

```bash
git clone https://github.com/dev27ansh/restaurant_search.git
cd restaurant_search
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\\Scripts\\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Apply the migrations to create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser to access the admin site:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

## Usage

1. **Admin Site**: Visit `http://127.0.0.1:8000/admin/` to log in with your superuser credentials and add dishes.
2. **Search Functionality**: Visit `http://127.0.0.1:8000/search/` to use the search functionality.
