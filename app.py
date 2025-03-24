
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = '8704b6af58ad428903e9091750378e25'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    favorite_genre = db.Column(db.String(100), nullable=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    reviews = db.relationship('Review', backref='book', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

# Routes
@app.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        favorite_genre = request.form['favorite_genre']
        new_user = User(username=username, password=password, favorite_genre=favorite_genre)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        return "Invalid credentials. Please try again."
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        new_book = Book(title=title, author=author, genre=genre)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_book.html')

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        content = request.form['content']
        rating = request.form['rating']
        user_id = session.get('user_id')
        if user_id:
            new_review = Review(content=content, rating=rating, user_id=user_id, book_id=book.id)
            db.session.add(new_review)
            db.session.commit()
            return redirect(url_for('book_detail', book_id=book.id))
        return "You need to be logged in to review."
    reviews = Review.query.filter_by(book_id=book_id).all()
    return render_template('book_detail.html', book=book, reviews=reviews)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Initialize the database and create tables
    app.run(debug=True)
