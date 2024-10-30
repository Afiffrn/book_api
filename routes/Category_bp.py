from flask import Blueprint
from controllers.CategoryController import get_categories, get_category, update_category, delete_category,add_category

category_bp = Blueprint('category_bp', __name__)

# Route untuk mendapatkan semua kategori
category_bp.route('/api/category', methods=['GET'])(get_categories)

# Route untuk mendapatkan kategori spesifik
category_bp.route('/api/category/<int:category_id>', methods=['GET'])(get_category)

# Route untuk menambah kategori spesifik
category_bp.route('/api/category', methods=['POST'])(add_category)

# Route untuk memperbarui kategori spesifik
category_bp.route('/api/category/<int:category_id>', methods=['PUT'])(update_category)

# Route untuk menghapus kategori spesifik
category_bp.route('/api/category/<int:category_id>', methods=['DELETE'])(delete_category)