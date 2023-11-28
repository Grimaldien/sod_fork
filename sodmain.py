# Import required libraries
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.config.suppress_callback_exceptions = True

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.Button(
        id="btn-player-stats",
        children=[
            html.Img(
                src='https://pm1.aminoapps.com/7111/3e8ceb6dc8e354ca60a138fe71dcf09ceaa2318ar1-600-600v2_uhq.jpg',
                style={
                    'width': '100%',
                    'height': '100%',
                    'border-radius': '50%',
                    'object-fit': 'cover',
                },
            ),
            html.Div(
                "Your Text",
                style={
                    'position': 'absolute',
                    'top': '50%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'color': 'white',
                    'font-size': '14px',
                    'text-align': 'center',
                },
            ),
        ],
        style={
            'border': 'none',
            'padding': '0',
            'cursor': 'pointer',
            'outline': 'none',
            'align-items': 'center',
            'justify-content': 'center',
            'display': 'flex',
            'position': 'relative',
            'height': '75px',
            'width': '75px',
            'overflow': 'hidden',
        },
    )
,
        html.Button([html.Img(src='your-icon-url-here', style={'height': '20px', 'width': '20px'}), " Blackfathom Deeps Statistics"], 
                    id="btn-bfd-stats", 
                    style={'display': 'flex', 'align-items': 'center', 'border-radius': '50%', 'margin': '5px', 'padding': '10px 20px'}),
        html.Button([html.Img(src='your-icon-url-here', style={'height': '20px', 'width': '20px'}), " Player versus Player"], 
                    id="btn-pvp-stats", 
                    style={'display': 'flex', 'align-items': 'center', 'border-radius': '50%', 'margin': '5px', 'padding': '10px 20px'}),
        
        html.Button(id="btn-talent-stats", style={
        'background-image': 'url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtKzqVZvUcsh7VGVtryl8G1yTcCoRgYt5nsQ&usqp=CAU)',
        'background-size': 'cover',
        'background-position': 'center',  # Ensure the image is centered
        'border-radius': '50%',
        'height': '75px',  # Adjust size as needed
        'width': '75px',   # Adjust size as needed
        'border': 'none',  # Remove border
        'padding': '0',    # Remove padding
        'cursor': 'pointer', # Change cursor on hover
        'outline': 'none', # Remove outline
        'align-items': 'center',
        'justify-content': 'center',
        'display': 'flex',
    }
)
    ], style={'display': 'flex', 'justify-content': 'center', 'background-color': '#000000'}),  # Set the button container background to black
    html.Div(id='page-content')
], style={'background-color': '#000000', 'height': '100vh', 'color': 'black'})  # Set the overall app background to black

# Callbacks to navigate to different pages
@app.callback(Output('url', 'pathname'),
              [Input('btn-player-stats', 'n_clicks'),
               Input('btn-bfd-stats', 'n_clicks'),
               Input('btn-pvp-stats', 'n_clicks'),
               Input('btn-talent-stats', 'n_clicks')],
              prevent_initial_call=True)
def navigate(n1, n2, n3, n4):
    ctx = dash.callback_context

    if not ctx.triggered:
        return '/'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'btn-player-stats':
            return '/player-statistics'
        elif button_id == 'btn-bfd-stats':
            return '/blackfathom-deeps-statistics'
        elif button_id == 'btn-pvp-stats':
            return '/pvp-statistics'
        elif button_id == 'btn-talent-stats':
            return '/talent-statistics'
    raise PreventUpdate

# Function to render each page's content
def render_page_content(pathname):
    if pathname == '/player-statistics':
        # Define layout for Player Statistics
        return html.Div([html.H1('Player Statistics')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})
    elif pathname == '/blackfathom-deeps-statistics':
        # Define layout for Blackfathom Deeps Statistics
        return html.Div([html.H1('Blackfathom Deeps Statistics')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})
    elif pathname == '/pvp-statistics':
        # Define layout for Player vs Player Statistics
        return html.Div([html.H1('PvP Statistics')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})
    elif pathname == '/talent-statistics':
        # Define layout for Talent Statistics
        return html.Div([html.H1('Talent Statistics')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})
    else:
        # Default page when no buttons are clicked
        return html.Div([html.H1('Welcome to the WoW Dashboard')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})

# Update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return render_page_content(pathname)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
