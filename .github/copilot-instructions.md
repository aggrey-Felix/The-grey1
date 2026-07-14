<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

## Python Flask Personal Blog

This is a personal blog application built with Python Flask and SQLAlchemy. It provides a lightweight, feature-rich blogging platform with a clean, responsive design.

### Project Overview

- **Framework**: Flask 2.3.3
- **Database**: SQLAlchemy with SQLite (default)
- **Template Engine**: Jinja2
- **Styling**: Custom CSS with responsive design

### Key Features

1. **Blog Post Management**: Create, read, update, and delete blog posts
2. **Database**: SQLAlchemy ORM with SQLite for local development
3. **Responsive Design**: Mobile-friendly interface
4. **Error Handling**: Custom 404 and 500 error pages
5. **Pagination**: Posts displayed with pagination (5 per page)

### Project Structure

- `app.py` - Main Flask application with routes and database models
- `config.py` - Configuration for different environments
- `requirements.txt` - Python package dependencies
- `templates/` - Jinja2 HTML templates
- `static/css/` - Custom stylesheet
- `instance/` - Database storage (auto-created)

### Running the Application

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

The application will be available at `http://localhost:5000`

### Development Guidelines

- Keep business logic in `app.py` with route handlers
- Use Jinja2 templates for HTML rendering
- Database models are defined in `app.py` as SQLAlchemy models
- CSS styling is in `static/css/style.css`
- Use Flask's `render_template` and `redirect` for navigation

### Database Models

**BlogPost Model**:
- `id`: Primary key
- `title`: Post title (max 200 chars)
- `content`: Post content (text)
- `author`: Author name (default: 'Admin')
- `created_at`: Creation timestamp
- `updated_at`: Update timestamp

### Route Overview

- `/` - Homepage with blog posts listing
- `/post/<id>` - View individual blog post
- `/create` - Create new blog post
- `/edit/<id>` - Edit existing blog post
- `/delete/<id>` - Delete blog post
- `/about` - About page
- `/404` - 404 error handler
- `/500` - 500 error handler

### Configuration

Edit `config.py` to:
- Change database URL: `SQLALCHEMY_DATABASE_URI`
- Set secret key: `SECRET_KEY`
- Toggle debug mode: `DEBUG`

### Customization Tips

1. **Add Features**: Extend models in `app.py` (e.g., tags, categories, comments)
2. **Styling**: Modify `static/css/style.css`
3. **Templates**: Edit files in `templates/` directory
4. **Database**: Use Flask-SQLAlchemy ORM for new models
5. **Environment**: Use `.env` file with `python-dotenv` for sensitive data

### Common Tasks

- **Create Migration**: Modify `config.py` or models in `app.py`
- **Add New Route**: Add function with `@app.route()` decorator in `app.py`
- **Update Styling**: Edit `static/css/style.css`
- **Add Template**: Create new HTML file in `templates/` and use `render_template()`

### Troubleshooting

- **Database Issues**: Delete `instance/blog.db` and restart to reinitialize
- **Port in Use**: Change port in `app.py` (last line)
- **Import Errors**: Ensure virtual environment is activated and dependencies installed

### Next Steps

1. Customize the about page in `templates/about.html`
2. Add your blog title and branding to `templates/base.html`
3. Create your first blog post through the web interface
4. Customize colors in `static/css/style.css`
