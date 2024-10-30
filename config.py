from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Membuat aplikasi Flask
app = Flask(__name__)

# Konfigurasi database MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://apips:12321@localhost:3306/db_mvc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi objek database
db = SQLAlchemy(app)

app.app_context().push()