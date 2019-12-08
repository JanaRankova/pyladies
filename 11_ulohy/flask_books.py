from flask import Flask, url_for, render_template, abort
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    """Homepage that informs you about purpose of this app."""
    return render_template('welcome.html')

@app.route('/list/')
def listing():
    """Shows all authors from dictionary for us to know which key to use."""
    with open(r'C:\\Users\\ranko\Desktop\\Python_lectures\\11\\books.txt', 'r') as books_file:
        data = json.loads(books_file.read())
        for key in data.keys():
            data[key]
    return render_template('books.html', data=data)

@app.route('/list/<author>')
def author(author=None):
    with open(r'C:\\Users\\ranko\Desktop\\Python_lectures\\11\\books.txt', 'r') as books_file:
        data = json.loads(books_file.read())
        if author in data:
            return 'Book you are currently reading written by {} is {}.'.format(author, (data[author]))
        else:
            return render_template('404.html')

if __name__ == '__main__':          
    app.run()