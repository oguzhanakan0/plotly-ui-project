# scatter_mode_callbacks

# 1. MODE #

# 1.1 Hide mode if the trace is not scatter
@app.callback(
    Output('trace-mode-container', 'hidden'),
    [Input('trace-selector','value')])
def updateTraceModeArea(trace):
    try:
        if(traces_dict[graph_name[0]][trace.replace('-','_')]['trace_type']=='scatter'):
            return False
        else:
            return True
    except:
        return True

# 1.2.1 Show Line Properties Pane
@app.callback(
    Output('line-properties-pane', 'hidden'),
    [Input('show-line-properties-button','n_clicks')])
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
    Output('show-line-properties-button', 'children'),
    [Input('show-line-properties-button','n_clicks')])
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
    Output('marker-properties-pane', 'hidden'),
    [Input('show-marker-properties-button','n_clicks')])
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
    Output('show-marker-properties-button', 'children'),
    [Input('show-marker-properties-button','n_clicks')])
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
    Output('marker-border-properties-pane', 'hidden'),
    [Input('show-marker-border-properties-button','n_clicks')])
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
    Output('show-marker-border-properties-button', 'children'),
    [Input('show-marker-border-properties-button','n_clicks')])
def updateTraceModeArea(n_clicks):
    try:
        if(n_clicks%2==1):
            return 'hide'
        else:
            return 'show'
    except:
        return 'show'

@app.callback(
    Output('trace-pane', 'dummy-showmode'),
    [Input('trace-showlines', 'values'),
     Input('trace-showmarkers', 'values'),
     Input('trace-showtext', 'values'),
     Input('trace-selector','value')])
def updateTraceShowmode(lines,markers,text, trace):
    try:
        try: l = lines[0]
        except: l = False
        try: m = markers[0]
        except: m = False
        try: t = text[0]
        except: t = False
        if(l==True and m==False and t==False):
            traces_dict[graph_name[0]][trace.replace('-','_')]['mode']='lines'
        elif(l==True and m==True and t==False):
            traces_dict[graph_name[0]][trace.replace('-','_')]['mode']='lines+markers'
        elif(l==True and m==True and t==True):
            traces_dict[graph_name[0]][trace.replace('-','_')]['mode']='lines+markers+text'
        elif(l==False and m==True and t==False):
            traces_dict[graph_name[0]][trace.replace('-','_')]['mode']='markers'
        elif(l==False and m==True and t==True):
            traces_dict[graph_name[0]][trace.replace('-','_')]['mode']='markers+text'
        elif(l==True and m==False and t==True):
            traces_dict[graph_name[0]][trace.replace('-','_')]['mode']='lines+text'
        elif(l==False and m==False and t==True):
            traces_dict[graph_name[0]][trace.replace('-','_')]['mode']='text'
        else:
            traces_dict[graph_name[0]][trace.replace('-','_')]['mode']='none'
    except:
        try:
            traces_dict[graph_name[0]][trace.replace('-','_')]['mode']='markers+lines'
        except:
            pass
    return 1

@app.callback(
    Output('trace-showlines', 'values'),
    [Input('trace-selector','value')])
def updateTraceShowlines(trace):
    try:
        if(traces_dict[graph_name[0]][trace.replace('-','_')]['mode'].find('lines')==-1):
            return [False]
        else:
            return [True]
    except:
        return [True]

@app.callback(
    Output('trace-showmarkers', 'values'),
    [Input('trace-selector','value')])
def updateTraceShowmarkers(trace):
    try:
        if(traces_dict[graph_name[0]][trace.replace('-','_')]['mode'].find('markers')==-1):
            return [False]
        else:
            return [True]
    except:
        return [True]

@app.callback(
    Output('trace-showtext', 'values'),
    [Input('trace-selector','value')])
def updateTraceShowtext(trace):
    try:
        if(traces_dict[graph_name[0]][trace.replace('-','_')]['mode'].find('text')==-1):
            return [False]
        else:
            return [True]
    except:
        return [True]

# 1.0 Enable/Disable Line Components
@app.callback(
    Output('trace-line-color', 'disabled'),
    [Input('trace-showlines', 'values')])
def enableLineColor(show_line):
    try:
        if(len(show_line)==0):
            return True
        else:
            return False
    except:
         return False

@app.callback(
    Output('trace-line-dash', 'disabled'),
    [Input('trace-showlines', 'values')])
def enableLineColor(show_line):
    try:
        if(len(show_line)==0):
            return True
        else:
            return False
    except:
         return False

@app.callback(
    Output('trace-line-shape', 'disabled'),
    [Input('trace-showlines', 'values')])
def enableLineColor(show_line):
    try:
        if(len(show_line)==0):
            return True
        else:
            return False
    except:
         return False


# 1.1 LINE COLOR #

@app.callback(
    Output('custom-line-color-input', 'disabled'),
    [Input('trace-line-color','value'),
     Input('trace-showlines', 'values')])
def enableCustomLineColor(color,show_line):
    if (color=='custom' and len(show_line)!=0):
        return False
    else:
        return True

@app.callback(
    Output('trace-pane', 'dummy-line-color'),
    [Input('trace-line-color', 'value'),
     Input('trace-selector','value'),
     Input('custom-line-color-input', 'value'),])
def updateTraceLineColor(color, trace, custom_color):
    try:
        try:
            if(color=='custom'):
                if(custom_color[0]=='#' and len(custom_color)==7):
                    traces_dict[graph_name[0]][trace.replace('-','_')]['line']['color']=custom_color
                else:
                    pass
            else:
                traces_dict[graph_name[0]][trace.replace('-','_')]['line']['color']=color
        except:
            if(color=='custom'):
                if(custom_color[0]=='#' and len(custom_color)==7):
                    traces_dict[graph_name[0]][trace.replace('-','_')]['line']={'color':custom_color}
                else:
                    pass
            else:
                traces_dict[graph_name[0]][trace.replace('-','_')]['line']={'color':color}
    except:
        pass
    return 1

@app.callback(
    Output('trace-line-color', 'value'),
    [Input('trace-selector','value')])
def updateLineColor(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['line']['color']
    except:
        return None

# 1.2 LINE DASH TYPE #

# 1.2.1 Enable/Disable Custom Dash Area
@app.callback(
    Output('custom-line-dash-input', 'disabled'),
    [Input('trace-line-dash','value'),
     Input('trace-showlines', 'values')])
def enableCustomLineColor(dash_type,show_line):
    if (dash_type=='custom' and len(show_line)!=0):
        return False
    else:
        return True

# 1.2.2 Refresh traces_dict
@app.callback(
    Output('trace-pane', 'dummy-line-dash'),
    [Input('trace-line-dash', 'value'),
     Input('trace-selector','value'),
     Input('custom-line-dash-input', 'value'),])
def updateTraceLineDashType(dash_type, trace, custom_dash):
    try:
        try:
            if(dash_type=='custom'):
                traces_dict[graph_name[0]][trace.replace('-','_')]['line']['dash']=custom_dash
            else:
                traces_dict[graph_name[0]][trace.replace('-','_')]['line']['dash']=dash_type
        except:
            if(dash_type=='custom'):
                traces_dict[graph_name[0]][trace.replace('-','_')]['line']={'dash':custom_dash}
            else:
                traces_dict[graph_name[0]][trace.replace('-','_')]['line']={'dash':dash_type}
    except:
        pass
    return 1

# 1.2.3 Remember Dash Types
@app.callback(
    Output('trace-line-dash', 'value'),
    [Input('trace-selector','value')])
def updateLineDashType(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['line']['dash']
    except:
        return None

# 1.3 LINE SHAPE #

# 1.3.1 Refresh traces_dict
@app.callback(
    Output('trace-pane', 'dummy-line-shape'),
    [Input('trace-line-shape', 'value'),
     Input('trace-selector','value')])
def updateTraceLineShape(shape, trace):
    try:
        try:
            traces_dict[graph_name[0]][trace.replace('-','_')]['line']['shape']=shape
        except:
            traces_dict[graph_name[0]][trace.replace('-','_')]['line']={'shape':shape}
    except:
        pass
    return 1

# 1.3.2 Remember Shape
@app.callback(
    Output('trace-line-shape', 'value'),
    [Input('trace-selector','value')])
def updateLineShape(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['line']['shape']
    except:
        return None

# 1.4 LINE WIDTH #

# 1.4.1 Refresh traces_dict
@app.callback(
    Output('trace-pane', 'dummy-line-width'),
    [Input('trace-line-width', 'value'),
     Input('trace-selector','value')])
def updateTraceLineWidth(width, trace):
    try:
        try:
            traces_dict[graph_name[0]][trace.replace('-','_')]['line']['width']=width
        except:
            traces_dict[graph_name[0]][trace.replace('-','_')]['line']={'width':width}
    except:
        pass
    return 1

# 1.3.2 Remember Width
@app.callback(
    Output('trace-line-width','value'),
    [Input('trace-selector','value')])
def updateLineWidth(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['line']['width']
    except:
        return None

# 1.5 LINE SMOOTHING #

# 1.5.1 Refresh traces_dict
@app.callback(
    Output('trace-pane', 'dummy-line-smoothing'),
    [Input('trace-line-smoothing', 'value'),
     Input('trace-selector','value')])
def updateTraceLineWidth(smoothing, trace):
    try:
        try:
            traces_dict[graph_name[0]][trace.replace('-','_')]['line']['smoothing']=smoothing
        except:
            traces_dict[graph_name[0]][trace.replace('-','_')]['line']={'smoothing':smoothing}
    except:
        pass
    return 1

# 1.5.2 Remember Smoothing
@app.callback(
    Output('trace-line-smoothing','value'),
    [Input('trace-selector','value')])
def updateLineWidth(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['line']['smoothing']
    except:
        return None

# 1.5.3 Enable/Disable Smoother
@app.callback(
    Output('trace-line-smoothing', 'disabled'),
    [Input('trace-line-shape','value'),
     Input('trace-showlines', 'values')])
def enableCustomLineColor(shape,show_line):
    try:
        if (shape=='spline' and len(show_line)!=0):
            return False
        else:
            return True
    except:
        return True

# 2.1 MARKER SIZE #

# 2.1.1 Enable/Disable Marker Size Input
@app.callback(
    Output('trace-marker-size', 'disabled'),
    [Input('trace-showmarkers', 'values')])
def enableCustomLineColor(show_marker):
    if (len(show_marker)!=0):
        return False
    else:
        return True
# 2.1.2 Enable/Disable Marker Color Dropdown
@app.callback(
    Output('trace-marker-color', 'disabled'),
    [Input('trace-showmarkers', 'values')])
def enableLineColor(show_line):
    try:
        if(len(show_line)==0):
            return True
        else:
            return False
    except:
         return False

# 2.1.3 Enable/Disable Marker Symbol Dropdown
@app.callback(
    Output('trace-marker-symbol', 'disabled'),
    [Input('trace-showmarkers', 'values')])
def enableLineColor(show_line):
    try:
        if(len(show_line)==0):
            return True
        else:
            return False
    except:
         return False

# 2.1.4 Enable/Disable Marker Symbol Property Radiobutton
@app.callback(
    Output('trace-marker-symbol-property', 'disabled'),
    [Input('trace-showmarkers', 'values')])
def enableLineColor(show_line):
    try:
        if(len(show_line)==0):
            return True
        else:
            return False
    except:
         return False

# 2.1.5 Enable/Disable Marker Border Button
@app.callback(
    Output('show-marker-border-properties-button', 'disabled'),
    [Input('trace-showmarkers', 'values')])
def enableLineColor(show_line):
    try:
        if(len(show_line)==0):
            return True
        else:
            return False
    except:
         return False


# 2.1.6 Enable/Disable Marker Border Width Input
@app.callback(
    Output('trace-marker-border-width', 'disabled'),
    [Input('trace-showmarkers', 'values')])
def enableLineColor(show_line):
    try:
        if(len(show_line)==0):
            return True
        else:
            return False
    except:
         return False

 # 2.1.6 Enable/Disable Marker Border Color Dropdown
@app.callback(
    Output('trace-marker-border-color', 'disabled'),
    [Input('trace-showmarkers', 'values')])
def enableLineColor(show_line):
    try:
        if(len(show_line)==0):
            return True
        else:
            return False
    except:
         return False

# 2.1.2 Refresh trace_dict
@app.callback(
    Output('trace-pane', 'dummy-marker-size'),
    [Input('trace-marker-size', 'value'),
     Input('trace-selector','value')])
def updateTraceLineWidth(size, trace):
    try:
        try:
            traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['size']=size
        except:
            traces_dict[graph_name[0]][trace.replace('-','_')]['marker']={'size':size}
    except:
        pass
    return 1

# 2.1.3 Remember Marker Size
@app.callback(
    Output('trace-marker-size','value'),
    [Input('trace-selector','value')])
def updateLineWidth(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['size']
    except:
        pass

# 2.2 MARKER COLOR #

@app.callback(
    Output('custom-marker-color-input', 'disabled'),
    [Input('trace-marker-color','value'),
     Input('trace-showlines', 'values')])
def enableCustomLineColor(color,show_marker):
    if (color=='custom' and len(show_marker)!=0):
        return False
    else:
        return True

@app.callback(
    Output('trace-pane', 'dummy-marker-color'),
    [Input('trace-marker-color', 'value'),
     Input('trace-selector','value'),
     Input('custom-marker-color-input', 'value'),])
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
    Output('trace-marker-color', 'value'),
    [Input('trace-selector','value')])
def updateLineColor(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['color']
    except:
        return None

# 2.3 MARKER SYMBOL #

# 2.3.1 Refresh traces_dict
@app.callback(
    Output('trace-pane', 'dummy-marker-symbol'),
    [Input('trace-marker-symbol', 'value'),
     Input('trace-marker-symbol-property', 'value'),
     Input('trace-selector','value')])
def updateTraceLineShape(symbol, prop, trace):
    try:
        try:
            traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['symbol']=symbol+prop
        except:
            traces_dict[graph_name[0]][trace.replace('-','_')]['marker']={'symbol':symbol+prop}
    except:
        pass
    return 1


# 2.3.2 Remember Symbol
@app.callback(
    Output('trace-marker-symbol', 'value'),
    [Input('trace-selector','value')])
def updateLineShape(trace):
    try:
        a = traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['symbol']
        if len(str(a))==1:
            return a
        elif len(str(a))==3:
            return int(str(a)[0])
    except:
        return 0

# 2.3.3 Remember Symbol Property
@app.callback(
    Output('trace-marker-symbol-property', 'value'),
    [Input('trace-selector','value')])
def updateLineShape(trace):
    try:
        a = traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['symbol']
        if len(str(a))==1:
            return 0
        elif len(str(a))==3:
            return int(a/100)*100
    except:
        return 0


# 2.5 MARKER BORDER LINE WIDTH #

# 2.5.1 Refresh traces_dict
@app.callback(
    Output('trace-pane', 'dummy-marker-border-width'),
    [Input('trace-marker-border-width', 'value'),
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

# 2.5.2 Remember Width
@app.callback(
    Output('trace-marker-border-width','value'),
    [Input('trace-selector','value')])
def updateLineWidth(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']['width']
    except:
        return None

# 1.1 MARKER BORDER COLOR #

@app.callback(
    Output('custom-marker-border-color-input', 'disabled'),
    [Input('trace-marker-border-color','value'),
     Input('trace-showmarkers', 'values')])
def enableCustomLineColor(color,show_line):
    if (color=='custom' and len(show_line)!=0):
        return False
    else:
        return True

@app.callback(
    Output('trace-pane', 'dummy-marker-border-color'),
    [Input('trace-marker-border-color', 'value'),
     Input('trace-selector','value'),
     Input('custom-marker-border-color-input', 'value'),])
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
    Output('trace-marker-border-color', 'value'),
    [Input('trace-selector','value')])
def updateLineColor(trace):
    try:
        return traces_dict[graph_name[0]][trace.replace('-','_')]['marker']['line']['color']
    except:
        return None
