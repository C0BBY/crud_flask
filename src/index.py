from flask import Flask, jsonify
from mysql.connector import Error

from src import Database

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    return 'hello user'


@app.route("/customers", methods=['GET', 'POST'])
def get_customers():
    conn = Database.dbConnection()
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM CUSTOMERS"
        cursor.execute(sql)
        rs = cursor.fetchall()
        return jsonify(rs)
    except Error as exception:
        return '{error:{}}'.format(exception)
    finally:
        conn.close()


if __name__ == '__main__':
    app.debug = True
    app.run()
