from flask import Flask, render_template

app = Flask(__name__)

from flask.ext.mysqldb import MySQL
mysql = MySQL(app)

@app.route("/")
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/sql')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main__":
    app.run()