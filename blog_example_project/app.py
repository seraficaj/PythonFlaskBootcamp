print('hello world ~ app.py!')

from logging import debug
from puppycompanyblog import app

if __name__ == '__main__':
    app.run(debug=True)