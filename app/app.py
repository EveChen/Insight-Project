import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask
import plotly.graph_objs as go
import psycopg2
import MySQLdb
import pandas as pd

server = Flask(__name__)
app = dash.Dash(__name__, server = server)

# Connect MySQL with Dash
def fetchData(command):
    conn = MySQLdb.connect(host="ec2-34-213-6-190.us-west-2.compute.amazonaws.com",
            user="newuser", passwd="Xiavi293@", db="my_db")
    try:
        # connect to the MySQL server
        cur = conn.cursor()
        cur.execute(command);
        rows = cur.fetchall()
        cur.close()
    except (Exception) as error:
        print(error)
        raise error
    finally:
        if conn is not None:
            conn.close()
    return rows



# Make category dropdown list
def query_category():
    results = "SELECT DISTINCT category FROM metadata_small"
    return fetchData(results)

#
# all_category = query_category()
# category_dropdown = dcc.Dropdown(
#     id = "category_dropdown",
#     options = [{"label": c, "value": c} for c in all_category],
#     placeholder = "Select a category"
# )
categories = ['', 'books', 'electronics', 'moviestv', 'cdsvinyl', 'clothingshoesjewelry', 'homekitchen', 'kindlestore', 'sportsoutdoors', 'cellphonesaccessories', 'healthpersonalcare', 'toysgames', 'videogames', 'toolshomeimprovement', 'beauty', 'appsforandroid', 'officeproducts', 'petsupplies', 'automotive', 'grocerygourmetfood', 'patiolawngarden', 'baby', 'digitalmusic', 'musicalinstruments', 'amazoninstantvideo']
category_dropdown = dcc.Dropdown(
    id = "category_dropdown",
    options = [{"label": c, "value": c} for c in categories],
    placeholder = "Select a category"
)

# Get Metadata from MySQL
def query_metadata():
    results = "SELECT asin, title FROM metadata_small"
    return fetchData(results)

all_products = query_metadata()
product_dropdown = dcc.Dropdown(
    id = "product_dropdown",
    options = [{"label": p[1], "value": p[0]} for p in all_products],
    placeholder = "Select a product"
)

def query_info():
    results = "SELECT price, imUrl FROM metadata_small"
    return fetchData(results)

# Test table
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

# app.layout = dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict("rows"),
# )

app.layout = html.Div([
    # Header
    html.H1(children='Search the Adjusted Amazon Ratings'),
    # Dropdown lists
    html.Div([
        html.Div([
            category_dropdown,
            product_dropdown
        ],
        style = {'width' : '48%', 'display' : 'inline-block'})

        # html.Div([
        #
        # ],
        # style = {'width' : '48%', 'display' : 'inline-block'})
    ]),

    # Image
    html.Div(
        html.Img(src='http://ecx.images-amazon.com/images/I/41SwthpdD9L._SX300_.jpg',height="10%")
        ,style={"float":"middle","height":"10%"}),

])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
