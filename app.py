import os
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardToGuessString'

bootstrap = Bootstrap(app)

#import views
from views import *

if __name__ == '__main__':
    app.run(debug=True)