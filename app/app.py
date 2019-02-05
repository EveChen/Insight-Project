# Initiate my Flask app - to check if MySQL can connect with Flask

# Packages
from flask import Flask
from flaskext.mysql import MySQL
from flask import render_template

app = Flask(__name__)

# Configuration: set up connection
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'database_name'
app.config['MYSQL_DATABASE_HOST'] = 'public_DNS'
mysql.init_app(app)


# Query 10 lines from the table to Flask
@app.route("/")
def show_top_five():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name LIMIT 10")
    results = cursor.fetchall()
    print(results)
    print(type)
    return render_template("index.html", results = results)


if __name__ == "__main__":
    app.run(debug=True)
