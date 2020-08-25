from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

# landing page that will display all the books in our database
# This function will operate on the Read operation.
@app.route('/')
@app.route('/books')
def showBooks():
    return render_template('books.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
