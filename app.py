import os.path

from flask import Flask, render_template

from blueprints.errors_blueprint import errors_blueprint
from blueprints.customer_blueprint import customer_blueprint
from blueprints.tracks_blueprint import tracks_blueprint
from init_db import init_db

app = Flask(__name__)
app.register_blueprint(errors_blueprint)
app.register_blueprint(customer_blueprint)
app.register_blueprint(tracks_blueprint)


@app.route('/')
def home():
    return render_template('home.html', title='Home')


if __name__ == '__main__':
    if not os.path.exists('database.db'):
        init_db()
    app.run(debug=True, port=4000)
