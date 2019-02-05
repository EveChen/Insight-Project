# Initiate my Flask app - to check if MySQL can connect with Flask

# Packages
from flask import Flask
from flaskext.mysql import MySQL
from flask import render_template

app = Flask(__name__)

# set up connection
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'newuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Xiavi293@'
app.config['MYSQL_DATABASE_DB'] = 'my_db'
app.config['MYSQL_DATABASE_HOST'] = 'ec2-34-213-6-190.us-west-2.compute.amazonaws.com'
mysql.init_app(app)


@app.route("/")
def show_top_five():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews LIMIT 5")
    results = cursor.fetchall()
    print(results)
    print(type)
    return render_template("index.html", results = results)


if __name__ == "__main__":
    app.run(debug=True)
