import dash_html_components as dash_html_components

content = html.Div([
    html.Iframe(
        src="localhost:5555",
        style={
        'width':'100%',
        'height':'100%',
        'border':'0',
        'overflow':'hidden',
        }
    )
], style={'height:100%'})
