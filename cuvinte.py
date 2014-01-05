from flask import Flask, render_template
from random import choice
from json import load

app = Flask(__name__)

class WordManager:
    file = open('cuvinte.json')
    words = load(file)
    cache = []

    @classmethod
    def getWord(cls):
        while True:
            word = choice(cls.words)
            if word not in cls.cache:
                cls.cache.insert(0, word)
                if len(cls.cache) > 20:
                    cls.cache.pop()
                return word

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', word=WordManager.getWord())

@app.route('/api/', methods=['GET'])
def api_word():
    return WordManager.getWord()
