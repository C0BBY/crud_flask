from mysql.connector import Error
from flask import jsonify

from src import Database


def get_employees():
    conn = Database.dbConnection()
    employees_dictionary = {}
    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM EMPLOYEES"
        cursor.execute(sql)
        rs = cursor.fetchall()
        employees_dictionary['employees'] = rs
        return jsonify(employees_dictionary)
    except Error as exception:
        employees_dictionary['error'] = exception
        return jsonify(str(employees_dictionary))
    finally:
        conn.close()


def get_job_titles():
    conn = Database.dbConnection()
    job_dictionary = {}
    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT DISTINCT JOBTITLE FROM EMPLOYEES"
        cursor.execute(sql)
        job_dictionary['job_titles'] = cursor.fetchall()

        return jsonify(job_dictionary)

    except Exception as exception:
        job_dictionary['error'] = str(exception)
        return jsonify(job_dictionary)

    finally:
        conn.close()
