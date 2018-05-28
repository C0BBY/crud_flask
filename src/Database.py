from mysql.connector import Error, connect


def dbConnection():
    try:
        connection = connect(host='localhost',
                             database='classicmodels',
                             user='root',
                             password='')
        return connection
    except Error as exception:
        return exception
