import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

app = dash.Dash(__name__)

# Carregar e processar os dados
df = pd.read_csv('processed_tweets.csv')

# Gráfico de tweets por data
fig_tweets = px.line(df, x='created_at', y='word_count', title='Volume de Tweets por Data')

# Layout do dashboard
app.layout = html.Div(children=[
    html.H1(children='Twitter Dashboard'),
    dcc.Graph(id='tweets-graph', figure=fig_tweets)
])

if __name__ == '__main__':
    app.run_server(debug=True)
