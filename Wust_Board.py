
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import pendulum as pen



df = pd.read_csv("https://docs.google.com/spreadsheets/d/{key}/gviz/tq?tqx=out:csv&sheet={sheet_name}".format(key="1ml0Q-rOSckeCj84Tt4GQ8lwmYKuiFCq4uEYAEGM_7D4",sheet_name="Sheet1"))
# print(df.head())

# date_options=[]

# for date in df['Date'].unique():
#     date_options.append({'label':str(date),'value':date})

Indicators = df.columns[1:4]

# days = (pen.today() - pen.create(2018,5,18)).days

app = dash.Dash('hello')
# app.title('Wuesthof')

server = app.server
app.layout = html.Div([

    html.Div([

            html.H2('Wuest_Board: an intelligence dashboard designed for the kitchen brand:Wuesthof',style={'fontFamily':'roboto','width':'60%','display':'inline-block'}),
            html.Img(src='https://upload.wikimedia.org/wikipedia/en/a/a4/Wusthof_Logo.png',style={'display':'inline-block','verticalAlign':'sub','marginLeft':100}),


        ],style={'marginLeft':20,'marginTop':20}),


    html.Div([

            html.Div([
                dcc.Dropdown(id='xaxis',
                options=[{'label':i,'value':i} for i in Indicators],
                value = 'Sentiment_Index',)],style={'width':'48%','display':'inline-block'}),


            html.Div([
                dcc.Dropdown(id='yaxis',
                options=[{'label':i,'value':i} for i in Indicators],
                value = 'Price',)],style={'width':'48%','display':'inline-block'}),

            ],style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),




    html.Div([
        dcc.Graph(id='Plot',
        hoverData={'points':[{'customdata':'Wusthof Gourmet 12 Piece Block Set 9312'}]},)
        # dcc.Dropdown(id='date_picker',
        #             options=date_options,
        #             value=df['Date'][0])
        ],style={'width':'48%','display':'inline-block'}),

    html.Div([
        html.Div([
            dcc.Graph(id='x-timeseries'),

        ],style={'marginLeft':10}),
        html.Div([
            dcc.Graph(id='y-timeseries'),

        ],style={'marginLeft':10}),
        ],style={'display': 'inline-block', 'width': '48%','marginLeft':10}),


    html.Div([
    dcc.Slider(id='Date-Slider',
                min= df['Date'].unique().min(),
                max= 20180531,
                value = 20180531,
                step = None,
                marks ={str(i): str(i) for i in df['Date'].unique()}
                )

    ],style={'width': '95%', 'display': 'inline-block','padding': '0px 20px 20px 20px','marginLeft':10}),






])


@app.callback(Output('Plot','figure'),
                [Input('Date-Slider','value'),
                Input('xaxis','value'),
                Input('yaxis','value')]
                )
def update_plot(selected_Date,xaxis_name,yaxis_name):

    filtered_df = df[df['Date']==selected_Date]
    traces=[]
    for item in filtered_df['Name'].unique():
        df_by_item = filtered_df[df['Name']==item]
        traces.append(go.Scatter(
                        x = df_by_item[xaxis_name],
                        y = df_by_item[yaxis_name],
                        mode='markers',
                        text =df_by_item['Name'],
                        # customdata = filtered_df['Name'].unique(),
                        customdata = df_by_item['Name'],
                        marker={'size':15},
                        opacity=0.5,
                        showlegend=False)




        )
    return {'data':traces,
            'layout':
                    go.Layout(
                    title = 'Wuesthof Scatter Plot',
                    xaxis= {'title':xaxis_name},
                    yaxis = {'title':yaxis_name},
                    hovermode='closest')


    }




@app.callback(Output('x-timeseries','figure'),
                [Input('Plot','hoverData'),
                Input('xaxis','value')])


def update_x_series(hoverData, xaxis_column_name):

    item_name = hoverData['points'][0]['customdata']
    dff = df[df['Name']==item_name]
    # dff['new_date'] = pd.to_datetime(dff['Timestamp'],unit='s')
    # dff.set_index('new_date',inplace=True)
    title = '<b>{}</b><br>{}'.format(item_name, xaxis_column_name)

    figure = {
        'data': [go.Scatter(
            x=dff['Date_Dashed'].unique(),
            # x=dff.index,
            y=dff[xaxis_column_name],
            mode='lines+markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'yaxis': {},
            'xaxis': {'showgrid': False}
        }
    }
    return figure


@app.callback(Output('y-timeseries','figure'),
                [Input('Plot','hoverData'),
                Input('yaxis','value')])


def update_y_series(hoverData, yaxis_column_name):

    item_name = hoverData['points'][0]['customdata']
    dff = df[df['Name']==item_name]
    # dff['new_date'] = pd.to_datetime(dff['Timestamp'],unit='s')
    # dff.set_index('new_date',inplace=True)
    title = '<b>{}</b><br>{}'.format(item_name, yaxis_column_name)

    figure = {
        'data': [go.Scatter(
            # x=dff.index,
            x=dff['Date_Dashed'].unique(),
            y=dff[yaxis_column_name],
            mode='lines+markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'yaxis': {},
            'xaxis': {'showgrid': False}
        }
    }
    return figure







# Append an externally hosted CSS stylesheet
my_css_url = "https://unpkg.com/normalize.css@5.0.0"
app.css.append_css({
    "external_url": my_css_url
})

# Append an externally hosted JS bundle
my_js_url = 'https://unkpg.com/some-npm-package.js'
app.scripts.append_script({
    "external_url": my_js_url
})







# app.scripts.config.serve_locally=True

if __name__ ==  '__main__':
    app.run_server(debug=True)
