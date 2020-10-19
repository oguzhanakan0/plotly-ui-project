# trace_pane_callbacks

# 1. HIDE/SHOW TRACE PANE #
@app.callback(
    Output('trace-pane-content', 'hidden'),
    [Input('add-trace-button', 'n_clicks')])
def tracePaneAppear(n):
    if n!=None:
        return False
    else:
        return True

# 2. REFRESH TRACE SELECTOR OPTIONS #
@app.callback(
    Output('trace-selector', 'options'),
    [Input('add-trace-button', 'n_clicks')])
def tracePaneOptions(n):
    if n!=None:
        return [{'label':'trace-'+str(a), 'value':'trace-'+str(a)} for a in range(1,n+1)]
    else:
        return []

# 2-3 ARASI 1. NAME #
@app.callback(
    Output('trace-pane', 'dummy-name'),
    [Input('trace-name', 'value'),
     Input('trace-selector','value')])
def updateTraceName(trace_name, trace):
    try:
        traces_dict[graph_name[0]][trace.replace('-','_')]['name']=trace_name
    except:
        pass
    return 1

@app.callback(
    Output('trace-name', 'value'),
    [Input('trace-selector','value')])
def updateTraceNameArea(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['name']
    except:
        return trace

# 2-3 ARASI 2. VISIBILITY #
@app.callback(
    Output('trace-pane', 'dummy-visibility'),
    [Input('trace-visibility', 'value'),
     Input('trace-selector','value')])
def updateTraceName(visibility, trace):
    try:
        traces_dict[graph_name[0]][trace.replace('-','_')]['visible']=visibility
    except:
        pass
    return 1

@app.callback(
    Output('trace-visibility', 'value'),
    [Input('trace-selector','value')])
def updateTraceNameArea(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['visible']
    except:
        return True

# 3. X-AXIS #
@app.callback(
    Output('trace-pane', 'dummy-xaxis'),
    [Input('trace-x-axis', 'value'),
     Input('trace-selector','value')])
def updateTraceName(xaxis, trace):
    try:
        traces_dict[graph_name[0]][trace.replace('-','_')]['xaxis']=xaxis
    except:
        pass
    return 1

# 3.1 Remember X-axis
@app.callback(
    Output('trace-x-axis', 'value'),
    [Input('trace-selector','value')])
def updateTraceNameArea(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['xaxis']
    except:
        return 'x'

# 4. Y-AXIS #
@app.callback(
    Output('trace-pane', 'dummy-yaxis'),
    [Input('trace-y-axis', 'value'),
     Input('trace-selector','value')])
def updateTraceName(yaxis, trace):
    try:
        traces_dict[graph_name[0]][trace.replace('-','_')]['yaxis']=yaxis
    except:
        pass
    return 1

# 3.1 Remember Y-axis
@app.callback(
    Output('trace-y-axis', 'value'),
    [Input('trace-selector','value')])
def updateTraceNameArea(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['yaxis']
    except:
        return 'y'



# OPACITY #
@app.callback(
    Output('trace-pane', 'dummy-opacity'),
    [Input('trace-opacity', 'value'),
     Input('trace-selector','value')])
def updateTraceOpacity(opacity, trace):
    try:
        traces_dict[graph_name[0]][trace.replace('-','_')]['opacity']=opacity
    except:
        pass
    return 1

@app.callback(
    Output('trace-opacity', 'value'),
    [Input('trace-selector','value')])
def updateTraceOpacityArea(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['opacity']
    except:
        return 1

# SHOW LEGEND #
@app.callback(
    Output('trace-pane', 'dummy-showlegend'),
    [Input('trace-showlegend', 'values'),
     Input('trace-selector','value')])
def updateTraceShowlegend(showlegend, trace):
    try:
        traces_dict[graph_name[0]][trace.replace('-','_')]['showlegend']=showlegend[0]
    except:
        try:
            traces_dict[graph_name[0]][trace.replace('-','_')]['showlegend']=False
        except:
            pass
    return 1

@app.callback(
    Output('trace-showlegend', 'value'),
    [Input('trace-selector','value')])
def updateTraceShowlegendArea(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['showlegend']
    except:
        return True
