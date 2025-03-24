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
git clone https://github.com/your-username/podcast-app.git
cd podcast-app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
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
- **Static Files**: Located in `static/`.

## Project Structure

```
/ podcast-app
  ├── podcasts/          # Podcast & Episode models, views, templates
  ├── users/             # User authentication & profiles
  ├── reviews/           # Review system for podcasts & episodes
  ├── static/            # CSS, JS, and media files
  ├── templates/         # HTML templates
  ├── manage.py          # Django project manager
  ├── requirements.txt   # Python dependencies
  └── README.md          # This file
```

## License

This project is open-source. Feel free to modify and use it as needed.

## Contact

For any questions, contact us at martinmatustik90@gmail.com.
