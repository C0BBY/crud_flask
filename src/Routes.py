from flask import Flask, request
from src import DataLogic

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    return 'hello alpha'


@app.route("/employees", methods=['GET', 'POST'])
def get_employees():
    return DataLogic.get_employees()


@app.route("/employees/job_titles")
def get_job_titles():
    return DataLogic.get_job_titles()


if __name__ == '__main__':
    app.debug = True
    app.run()
