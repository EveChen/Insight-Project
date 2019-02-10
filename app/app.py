import plotly.plotly as py
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import MySQLdb
import pandas as pd

# Connect with MySQL & Query
conn = MySQLdb.connect(host="ec2-34-213-6-190.us-west-2.compute.amazonaws.com",
user="newuser", passwd="Xiavi293@", db="my_db")
cursor = conn.cursor()
cursor.execute('SELECT * FROM dash');
rows = cursor.fetchall()

# Create a dataframe
df = pd.DataFrame([[ij for ij in i] for i in rows])
df.rename(columns = {0: "Product_ID", 1: "Title", 2: "Price", 3: "Category", 4: "Asin", 5: "Original_ratings", 6: "Adjusted_ratings", 7:"Average_subjectivity", 8:"Label"}, inplace = True)
df.drop(['Product_ID', 'Asin', 'Average_subjectivity'], axis = 1, inplace = True)
# Create a table based on the dataframe I created
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

# Create app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Create the app layout
app.layout = html.Div(children=[
    html.H4(children='Amazon Adjusted Ratings'),
    html.Label("Enter a keyword and press submit"),
    html.Div([
        html.Div([
            html.Div(dcc.Input(id='input-box', type='text', placeholder = 'Enter a product name...', value = ''))
        ]),
        html.Div([
            html.Button('Submit', id='button')
        ])
    ]),
    generate_table(df)
])

# @app.callback(
#     Output(component_id = '', component_property = ''),
#     [Input(component_id = 'input-box', component_property = 'value')]
# )

if __name__ == '__main__':
    app.run_server(debug=True, host = '0.0.0.0')
