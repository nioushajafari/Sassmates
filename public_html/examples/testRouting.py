from flask import Flask, render_template

app = Flask(__name__)

#from flask.ext.mysqldb import MySQL
#mysql = MySQL(app)

@app.route("/test/<id>")
def hello(id):
    return render_template('hello.html', name=id)

@app.route("/route2")
def test2():
    return render_template('test2.html')

# @app.route('/sql')
# def users():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT user, host FROM mysql.user''')
#     rv = cur.fetchall()
#     return str(rv)

if __name__ == "__main__":
    app.run(debug=True)