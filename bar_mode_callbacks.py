# bar_mode_callbacks

# 1. BAR MODE #

# 1.1 Hide mode if the trace is not bar
@app.callback(
    Output('bar-mode-container', 'hidden'),
    [Input('trace-selector','value')])
def updateTraceModeArea(trace):
    try:
        if(traces_dict[graph_name[0]][trace.replace('-','_')]['trace_type']=='bar'):
            return False
        else:
            return True
    except:
        return True

# 1.2.1 Show Line Properties Pane
@app.callback(
    Output('bar-general-properties-pane', 'hidden'),
    [Input('show-bar-general-properties-button','n_clicks')])
def updateTraceModeArea(n_clicks):
    try:
        if(n_clicks%2==1):
            return False
        else:
            return True
    except:
        return True

# 1.2.2 Change button text
@app.callback(
    Output('show-bar-general-properties-button', 'children'),
    [Input('show-bar-general-properties-button','n_clicks')])
def updateTraceModeArea(n_clicks):
    try:
        if(n_clicks%2==1):
            return 'hide'
        else:
            return 'show'
    except:
        return 'show'

# 1.3.1 Show Marker Properties Pane
@app.callback(
    Output('bar-marker-properties-pane', 'hidden'),
    [Input('show-bar-marker-properties-button','n_clicks')])
def updateTraceModeArea(n_clicks):
    try:
        if(n_clicks%2==1):
            return False
        else:
            return True
    except:
        return True

# 1.3.2 Change button text
@app.callback(
    Output('show-bar-marker-properties-button', 'children'),
    [Input('show-bar-marker-properties-button','n_clicks')])
def updateTraceModeArea(n_clicks):
    try:
        if(n_clicks%2==1):
            return 'hide'
        else:
            return 'show'
    except:
        return 'show'

# 1.4.1 Show Marker Border Properties Pane
@app.callback(
    Output('bar-marker-border-properties-pane', 'hidden'),
    [Input('show-bar-marker-border-properties-button','n_clicks')])
def updateTraceModeArea(n_clicks):
    try:
        if(n_clicks%2==1):
            return False
        else:
            return True
    except:
        return True

# 1.4.2 Change button text
@app.callback(
    Output('show-bar-marker-border-properties-button', 'children'),
    [Input('show-bar-marker-border-properties-button','n_clicks')])
def updateTraceModeArea(n_clicks):
    try:
        if(n_clicks%2==1):
            return 'hide'
        else:
            return 'show'
    except:
        return 'show'





# 1.5 BAR MARKER COLOR #

@app.callback(
    Output('custom-bar-marker-color-input', 'disabled'),
    [Input('trace-bar-marker-color','value')
     ])
def enableCustomLineColor(color):
    if (color=='custom'):
        return False
    else:
        return True

@app.callback(
    Output('trace-pane', 'dummy-bar-marker-color'),
    [Input('trace-bar-marker-color', 'value'),
     Input('trace-selector','value'),
     Input('custom-bar-marker-color-input', 'value'),])
def updateTraceLineColor(color, trace, custom_color):
    try:
        try:
            if(color=='custom'):
                if(custom_color[0]=='#' and len(custom_color)==7):
                    traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['color']=custom_color
                else:
                    pass
            else:
                traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['color']=color
        except:
            if(color=='custom'):
                if(custom_color[0]=='#' and len(custom_color)==7):
                    traces_dict[graph_name[0]][trace.replace('-','_')]['marker']={'color':custom_color}
                else:
                    pass
            else:
                traces_dict[graph_name[0]][trace.replace('-','_')]['marker']={'color':color}
    except:
        pass
    return 1

@app.callback(
    Output('trace-bar-marker-color', 'value'),
    [Input('trace-selector','value')])
def updateLineColor(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['color']
    except:
        return None

# 1.6 BAR MARKER BORDER WIDTH

# 1.6.1 Refresh traces_dict
@app.callback(
    Output('trace-pane', 'dummy-bar-marker-border-width'),
    [Input('trace-bar-marker-border-width', 'value'),
     Input('trace-selector','value')])
def updateTraceLineWidth(width, trace):
    try:
        try:
            traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']['width']=width
        except:
            traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']={'width':width}
    except:
        pass
    return 1

# 1.6.2 Remember Width
@app.callback(
    Output('trace-bar-marker-border-width','value'),
    [Input('trace-selector','value')])
def updateLineWidth(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']['width']
    except:
        return None

# 1.7 BAR MARKER BORDER COLOR #
@app.callback(
    Output('custom-bar-marker-border-color-input', 'disabled'),
    [Input('trace-bar-marker-border-color','value')
     ])
def enableCustomLineColor(color):
    if (color=='custom'):
        return False
    else:
        return True

@app.callback(
    Output('trace-pane', 'dummy-bar-marker-border-color'),
    [Input('trace-bar-marker-border-color', 'value'),
     Input('trace-selector','value'),
     Input('custom-bar-marker-border-color-input', 'value'),])
def updateTraceLineColor(color, trace, custom_color):
    try:
        try:
            if(color=='custom'):
                if(custom_color[0]=='#' and len(custom_color)==7):
                    traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']['color']=custom_color
                else:
                    pass
            else:
                traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']['color']=color
        except:
            if(color=='custom'):
                if(custom_color[0]=='#' and len(custom_color)==7):
                    traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']={'color':custom_color}
                else:
                    pass
            else:
                traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']={'color':color}
    except:
        pass
    return 1

@app.callback(
    Output('trace-bar-marker-border-color', 'value'),
    [Input('trace-selector','value')])
def updateLineColor(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']['color']
    except:
        return None

