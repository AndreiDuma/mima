from flask import Flask, render_template
from random import choice

app = Flask(__name__)

words = ['mama', 'tata', 'câine', 'abstract']

@app.route('/')
def index():
    word = choice(words)
    return render_template('index.html', word=word)
