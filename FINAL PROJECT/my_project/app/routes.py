from flask import  url_for, request, render_template, make_response, flash, redirect
from flask import current_app as app
from flask_login import login_required, logout_user, current_user, login_user
from . import loginManager
from . import db
from .models import Book, Author, UsersBook, User

@app.route('/')
def index():
    """Homepage of my project."""
    return 'Hello There'


@app.route('/db')
def populatedb():
    """Populates db with fake data."""

    # john_doe = User.query.get(1)

    # return '<br>'.join(list(map(
    #     lambda book: '{}: {}'.format(users_books.book.name, users_books.rating),
    #     john_doe.books
    # )))

    # return 'done'

