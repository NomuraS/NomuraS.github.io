from flask_frozen import Freezer
from main import app

freezer = Freezer(app)

app.config['FREEZER_RELATIVE_URLS'] = True

if __name__ == '__main__':
    freezer.freeze()