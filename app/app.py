import plotly.plotly as py
import plotly.graph_objs as go
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import MySQLdb
import pandas as pd
from dash.dependencies import Output, Input, State

# Connect MySQL with Dash
def fetchData(command):
    conn = MySQLdb.connect(host="publicDNS",
            user="username", passwd="password", db="dbname")
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


# Note: dash's category has the column name "imUrl" instead of "category" (would be fixed later)
def get_data(input_text):
    command = "SELECT title, price, imUrl, original_ratings, adjusted_ratings, label FROM dash WHERE title LIKE '%{}%'".format(input_text)
    return fetchData(command)


# # Create a table based on the dataframe I created
def generate_table(input_text):
    data = get_data(input_text)
    df = pd.DataFrame([ij for ij in i] for i in data)
    df.rename(columns = {0 : "Product Name", 1: "Price", 2: "Category", 3: "Original_ratings", 4 : "Adjusted_ratings", 5: "Label"}, inplace = True)

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in df.columns])] +

        # Body
        [html.Tr([
            html.Td(df.iloc[i][col]) for col in df.columns
        ]) for i in range(len(df))]
    )

# Create the Dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Design the layout
app.layout = html.Div([
    html.H1(children='''
        Amazon Adjusted Ratings
    '''),
    dcc.Input(id='input-productname', type='text', value=''),
    # html.Button(id='submit-button', n_clicks=0, children='Submit'), #Haven't done the submit button part
    html.Div(id='output-query')
])


# Callback: use the input value as the key to query product information
@app.callback(Output('output-query', 'children'),
              [Input('input-productname', 'value')])
def update_output(input):
    return generate_table(input)



if __name__ == '__main__':
    app.run_server(debug=True, host = '0.0.0.0')
