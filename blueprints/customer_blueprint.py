from flask import Blueprint, render_template

from init_db import get_db_connection

customer_blueprint = Blueprint('customer', __name__)


@customer_blueprint.route('/names')
def get_names():
    """Return the number of distinct first names in the database"""
    con = get_db_connection()
    count = con.execute('SELECT COUNT(DISTINCT first_name) FROM customers').fetchone()
    return render_template('customers.html', title='Customer Names', count=count[0])
