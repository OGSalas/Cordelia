from flask_frozen import Freezer
from intro import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
