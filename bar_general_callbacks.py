# bar_general_callbacks


# 1.1 BAR WIDTH #

# 1.1.1 Refresh traces_dict
@app.callback(
    Output('trace-pane', 'dummy-bar-width'),
    [Input('trace-bar-width', 'value'),
     Input('trace-selector','value')])
def updateTraceLineWidth(width, trace):
    try:
        try:
            traces_dict[graph_name[0]][trace.replace('-','_')]['width']=width
        except:
            traces_dict[graph_name[0]][trace.replace('-','_')]={'width':width}
    except:
        pass
    return 1

# 1.1.2 Remember Width
@app.callback(
    Output('trace-bar-width','value'),
    [Input('trace-selector','value')])
def updateLineWidth(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['width']
    except:
        return None
