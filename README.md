# Podcast App

Welcome to **Podcast App**, a Django-based web application for discovering, reviewing, and managing podcasts.

## Features

- **User Authentication**: Register, log in, and manage user profiles.
- **Podcast Management**: Add, edit, and browse podcasts by category and language.
- **Episode Reviews**: Rate and review podcasts and individual episodes.
- **Dashboard**: View top-rated podcasts and episodes.
- **Filtering & Sorting**: Sort podcasts and filter by category and language.
- **Static Pages**: "About Us" and "Privacy Policy" pages.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Chijano/DjangoProject3.git
cd DjangoProject3
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies (if applicable)
If you have a `requirements.txt`, install dependencies:
```bash
pip install -r requirements.txt
```
Otherwise, manually install Django:
```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## Configuration

- **Database**: SQLite (default) – can be changed in `settings.py`.
- **Templates**: Stored in `templates/`.

## Project Structure

```
/ DjangoProject3
  ├── podcasts/          # Podcast & Episode models, views, templates
  ├── users/             # User authentication & profiles
  ├── reviews/           # Review system for podcasts & episodes
  ├── templates/         # HTML templates
  ├── manage.py          # Django project manager
  ├── README.md          # This file
```

## License

This project is open-source. Feel free to modify and use it as needed.

## Contact

For any questions, contact us at [martinmatustik90@gmail.com](mailto:martinmatustik90@gmail.com).
