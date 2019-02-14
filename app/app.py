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

# Note: dash's category has the tag "imUrl" instead of "category"
def get_data(input_text):
    if len(input_text) <= 0:
        command = "SELECT title, price, category, original_ratings, adjusted_ratings, label FROM meta_index JOIN reviews_index ON meta_index.asin = reviews_index.asin WHERE title IS NOT NULL AND price IS NOT NULL LIMIT 10"
    else:
        command = "SELECT title, price, category, original_ratings, adjusted_ratings, label FROM meta_index JOIN reviews_index ON meta_index.asin = reviews_index.asin WHERE title LIKE '%{}%' AND price IS NOT NULL LIMIT 50".format(input_text)
    return fetchData(command)


# # Create a table based on the dataframe I created
def generate_table(input_text):
    data = get_data(input_text)
    df = pd.DataFrame([ij for ij in i] for i in data)
    df.rename(columns = {0 : "Product Name", 1: "Price", 2: "Category", 3: "Original Ratings", 4 : "Adjusted Ratings", 5: "Label"}, inplace = True)

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in df.columns])] +

        # Body
        [html.Tr([
            html.Td(df.iloc[i][col]) for col in df.columns
        ]) for i in range(len(df))]
    )

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1(children='''
        Amazon Adjusted Ratings
    '''),
    dcc.Input(id='input-productname', type='text', value=''),
    # html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-query')
])


@app.callback(Output('output-query', 'children'),
              [Input('input-productname', 'value')])
def update_output(input):
    return generate_table(input)


if __name__ == '__main__':
    app.run_server(debug=True, host = '0.0.0.0')
