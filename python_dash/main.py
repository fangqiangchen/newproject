import dash
import dash_html_components as html

app = dash.Dash(__name__)
block = html.Div(children=["Hello",
                           html.H1("hello again")])
app.layout = block
app.run_server(debug=False)