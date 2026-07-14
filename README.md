# Personal Blog - Python Flask

A lightweight, feature-rich personal blog application built with Python Flask and SQLAlchemy.

## Features

- 📝 Create, read, update, and delete blog posts
- 🎨 Clean, responsive design with custom CSS
- 💾 SQLite database for data persistence
- 🔍 Post pagination
- 📱 Mobile-friendly interface
- ⚡ Fast and lightweight

## Project Structure

```
.
├── app.py                 # Main Flask application and routes
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── instance/              # Database files (created automatically)
├── templates/             # Jinja2 HTML templates
│   ├── base.html         # Base template for all pages
│   ├── index.html        # Home page with blog posts
│   ├── post.html         # Individual post view
│   ├── create.html       # Create new post form
│   ├── edit.html         # Edit post form
│   ├── about.html        # About page
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/               # JavaScript files (if needed)
└── .gitignore            # Git ignore rules
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory**

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**

   ```bash
   python app.py
   ```

6. **Open your browser and visit**

   ```
   http://localhost:5000
   ```

## Usage

### Creating a Blog Post

1. Click on "New Post" in the navigation menu
2. Enter your post title, author name, and content
3. Click "Publish Post" to save

### Editing a Post

1. View a blog post by clicking "Read More"
2. Click the "Edit" button
3. Modify the content and click "Update Post"

### Deleting a Post

1. View the blog post
2. Click the "Delete" button and confirm

### About Page

You can edit the `templates/about.html` file to customize your about page.

## Configuration

The `config.py` file contains configuration settings:

- `SQLALCHEMY_DATABASE_URI`: Database connection string (default: SQLite)
- `SECRET_KEY`: Flask secret key for sessions
- `DEBUG`: Debug mode (enabled in development)

### Using Environment Variables

Set these environment variables for production:

```bash
export SECRET_KEY="your-secret-key-here"
export DATABASE_URL="your-database-url"
```

## Database

The blog uses SQLite by default, which creates an `instance/blog.db` file automatically on first run.

The database includes the `BlogPost` table with the following fields:

- `id`: Unique post identifier
- `title`: Post title
- `content`: Post content
- `author`: Author name
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

## Customization

### Styling

Edit `static/css/style.css` to customize the appearance of your blog.

### Templates

Modify HTML templates in the `templates/` directory to change the layout and structure.

### Database Models

Edit `app.py` to add new fields or models (e.g., categories, tags, comments).

## Deployment

This app is ready to run in production with a WSGI server and environment configuration.

### Local production-style run

```bash
set FLASK_CONFIG=DevelopmentConfig
python app.py
```

### Using Gunicorn locally or on a host

```bash
pip install -r requirements.txt
gunicorn app:app
```

### Procfile for hosts like Heroku / Railway / Render

Create a file named `Procfile` with:

```text
web: gunicorn app:app
```

### Deploying to Railway

Railway can deploy this Flask app directly from your GitHub repository.

1. Push your code to GitHub.
2. In Railway, create a new project and connect your GitHub repository.
3. Railway will detect the Python app and use the `Procfile`.
4. Set environment variables in Railway:
   - `FLASK_CONFIG=ProductionConfig`
   - `SECRET_KEY=your-secret-key`
   - `DATABASE_URL` (optional if you want PostgreSQL instead of SQLite)
5. Deploy the project.

Railway will run `gunicorn app:app` automatically from the `Procfile`.

### Deploying to Vercel

This app can also run on Vercel using a Python serverless function adapter.

1. Make sure `requirements.txt` includes `vercel_wsgi`.
2. Add `vercel.json` and `api/index.py` to the project.
3. Set environment variables on Vercel:
   - `FLASK_CONFIG=ProductionConfig`
   - `SECRET_KEY=your-secret-key`
   - `DATABASE_URL` (recommended if you need a persistent database)

> Note: Vercel serverless functions cannot write reliably to the project folder. The config now falls back to `/tmp/blog.db` when the repository folder is not writable.

### Recommended cloud deployment

1. Add the project to Git and push to a host like Heroku, Render, or Railway.
2. Set environment variables in the host dashboard:
   - `FLASK_CONFIG=ProductionConfig`
   - `SECRET_KEY=your-secret-key`
   - `DATABASE_URL` (optional for PostgreSQL or external DB)
3. Use the start command:
   - `gunicorn app:app`

### Heroku / Railway / Render example

- `git init`
- `git add .`
- `git commit -m "Deploy blog"
- `git push <remote> main`

Then configure the platform to use `gunicorn app:app` and the correct environment variables.

### Production notes

- Keep `DEBUG = False` in production.
- Use a proper production database instead of SQLite for larger traffic.
- Keep secrets out of source control by using environment variables.

## Dependencies

- **Flask**: Web framework
- **Flask-SQLAlchemy**: ORM for database operations
- **SQLAlchemy**: SQL toolkit and ORM
- **Werkzeug**: WSGI utility library

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, feel free to modify the code or refer to the official documentation:

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

Happy blogging! 📝✨
