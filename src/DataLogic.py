import json

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


def get_hierarchy():
    conn = Database.dbConnection()
    hierarchy = {}
    hierarchy_list = []
    try:
        cursor = conn.cursor(dictionary=True)
        # sql = "SELECT DISTINCT REPORTSTO,FIRSTNAME,LASTNAME FROM CLASSICMODELS.EMPLOYEES WHERE REPORTSTO <> 'NULL'"
        sql = "SELECT FIRSTNAME,LASTNAME,EMPLOYEENUMBER,REPORTSTO FROM EMPLOYEES"
        cursor.execute(sql)
        reports_to = cursor.fetchall()
        for i in range(0, len(reports_to)):
            hierarchy_dict = {}
            employee_number = reports_to[i]['EMPLOYEENUMBER']
            sql = "SELECT FIRSTNAME,LASTNAME,EMPLOYEENUMBER FROM CLASSICMODELS.EMPLOYEES WHERE REPORTSTO = {}".format(
                employee_number)
            cursor.execute(sql)
            employee_details = cursor.fetchall()
            hierarchy_dict['head'] = reports_to[i]
            hierarchy_dict['staff'] = employee_details
            hierarchy_list.append(hierarchy_dict)
        hierarchy['hierarchy'] = hierarchy_list
        return jsonify(hierarchy)
    except Exception as exception:
        hierarchy['error'] = str(exception)
        return jsonify(hierarchy)
    finally:
        conn.close()


def update_employee(request):
    conn = Database.dbConnection()
    update = {}
    try:
        first_name = request['FIRST_NAME']
        last_name = request['LAST_NAME']
        employee_number = request['EMPLOYEE_NUMBER']

        cursor = conn.cursor()
        sql = "UPDATE EMPLOYEES SET FIRSTNAME = '{}',LASTNAME = '{}' WHERE EMPLOYEENUMBER={}".format(first_name,
                                                                                                     last_name,
                                                                                                     employee_number)
        cursor.execute(sql)
        conn.commit()
        update['success'] = "operation successful"
        return jsonify(update)
    except Exception as exception:
        update['error'] = str(exception)
        return jsonify(update)
    finally:
        conn.close()
