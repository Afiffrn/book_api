from config import app, db
from routes.Book_bp import book_bp
from routes.Category_bp import category_bp

app.register_blueprint(book_bp)
app.register_blueprint(category_bp)

# Remove the `if __name__ == '__main__':` block
# and run the app with WSGI server

if __name__ == "__main__":
    app.run()

