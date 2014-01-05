from flask import Flask, render_template
from random import choice

app = Flask(__name__)

class WordManager:
    words = [
        'miting', 'tălpoi', 'belonid', 'carbonado', 'lobar', 'reclamant', 'relansare', 'africanolog', 'halomorfoză',
        'tus', 'stârpitură', 'interspecific', 'cremnofobie', 'fularda', 'scuzare', 'mârlănoi', 'acqua-tofana',
        'autentificat', 'imaterializare', 'factor', 'înmrejuit', 'lastic', 'tărâța', 'vutcă', 'bâzgâli', 'capturat',
        'concomitență', 'supraînălțare', 'bigrilă', 'norveg', 'astenologie', 'proteiform', 'canci', 'jegăl', 'coerent',
        'zolniță', 'manualitate', 'transformaționalism', 'autodidact', 'piroscaf', 'timpanotom', 'ciao', 'cârav',
        'multimetru', 'sveter', 'unidimensionare', 'șoimar', 'vestiment', 'prindoi', 'lagunar', 'zupăire', 'strungar',
        'caut', 'sociolect', 'cartonaj', 'acribie', 'frânghienică', 'vegetal', 'paleontologic', 'pergamentos', 'protestuit',
        'periodologie', 'melodramatic', 'brodnic', 'șufărire', 'termoluminiscență', 'celebrare', 'șoală', 'keriterapie',
        'numerabil', 'cramă', 'superpoziție', 'ruguș', 'stagflație', 'adins', 'reinventat', 'adăugat', 'memorie', 'abdomen',
        'bioenergoterapeut', 'mezdrea', 'ghiovăsi', 'interdicție', 'rheum', 'tărâcioară', 'tomograf', 'ialomițeancă',
        'moderantism', 'venoscleroză', 'cârstitel', 'răzvesti', 'tetanic', 'strâmbet', 'hâțâi', 'explosiv', 'scârpălui',
        'titlu', 'fosforilare', 'reînregistra', 'petitio'
    ]
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
