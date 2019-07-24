from flask import Flask, request, render_template,flash
import sqlite3


sqlite3_connection = sqlite3.connect('mydb.db', check_same_thread=False)
cursor_variable = sqlite3_connection.cursor()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/home", methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        if request.form['name'] is None:
            flash("This is dummy")
        else:
            result = request.form['name']
            result = result.lower()
            query = ("Select * from dictionary_tb where eng == '%s'" %result)
            # query = ("Select * from dictionary_tb where eng like '%s'" % result)

            execute_query = cursor_variable.execute(query)
            result_data = execute_query.fetchall()
            return render_template('home.html', rows=result_data)


@app.route("/AllWord")
def all_word():
    query = "Select * from dictionary_tb"
    execute_query = cursor_variable.execute(query)
    result_data = execute_query.fetchall()
    return render_template('AllWord.html', rows=result_data)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
