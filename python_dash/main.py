import dash
import dash_html_components as html

app = dash.Dash(__name__)
block = html.Div(
    [
        html.H1("Use DASH write all stuff!",
                style={"fontSize":"6rem","textAlign":"center"}),
        html.Img(src="/asserts/meme.png")
                ],style={"textAlign":"center"})
app.layout = block
app.run_server(debug=False)