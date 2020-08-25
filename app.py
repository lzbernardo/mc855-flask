from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
from ytutils import download

app = Flask(__name__)

# landing page that will display all the books in our database
# This function will operate on the Read operation.
@app.route('/')
def showBooks():
    return render_template('page.html')

@app.route('/download')
def downloadVid():
    return download('http://www.youtube.com/watch?v=TcfXwMnBsJ8')

if __name__ == '__main__':
    app.run()
