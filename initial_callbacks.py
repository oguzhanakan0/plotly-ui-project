# initial_callbacks
# coding: utf-8
# In[ ]:
# BUTTON STATES START #
@app.callback(
    Output('create-graph-button', 'value'),
    [Input('create-graph-button', 'n_clicks')],
    [State('graph-text-area', 'value')])
def createGraphButtonStates(n_clicks,value):
    if n_clicks==None:
        return 0
    elif(value!=None):
        return 2
    else:
        return 1

@app.callback(
    Output('submit-path-button', 'value'),
    [Input('submit-path-button', 'n_clicks')],
    [State('path-input-area', 'value')])
def submitPathButtonStates(n_clicks,value):
    if n_clicks==None:
        return 0
    elif(value!=None):
        return 2
    else:
        return 1
# BUTTON STATES END #

# CONTAINER HIDDEN = TRUE FALSE START #
@app.callback(
    Output('graph-text-area-container', 'hidden'),
    [Input('create-graph-button', 'value')])
def createGraphTextArea(value):
    if (value==1 or value==2):
        return False
    else:
        return True

@app.callback(
    Output('graph-main-container', 'hidden'),
    [Input('create-graph-button', 'value')])
def submitPathTextArea(value):
    if value==2:
        return False
    else:
        return True


@app.callback(
    Output('graph-initials-container', 'hidden'),
    [Input('submit-path-button', 'value')])
def submitPathTextArea(value):
    if value==2:
        return False
    else:
        return True

# CONTAINER HIDDEN = TRUE FALSE END #

# AREAS & BUTTONS ABLE DISABLE START #
@app.callback(
    Output('graph-text-area', 'disabled'),
    [Input('create-graph-button', 'value'),
     Input('graph-text-area', 'value')])
def createGraphTextAreaDisabled(value,gn):
    if value==2:
        try:
            graph_name.append(gn)
            layout_dict[gn]={}
            traces_dict[gn]={}
        except:
            pass
        return True

@app.callback(
    Output('create-graph-button', 'disabled'),
    [Input('create-graph-button', 'value')])
def createGraphButtonDisabled(value):
    if value==2:
        return True

@app.callback(
    Output('path-input-area', 'disabled'),
    [Input('submit-path-button', 'value'),
     Input('path-input-area', 'value')])
def createGraphTextAreaDisabled(value,path):
    if value==2:
        data_path.append(path)
        return True

@app.callback(
    Output('submit-path-button', 'disabled'),
    [Input('submit-path-button', 'value')])
def createGraphButtonDisabled(value):
    if value==2:
        return True
# AREAS & BUTTONS ABLE DISABLE END #


# BUTTON TEXT START #
@app.callback(
    Output('create-graph-button', 'children'),
    [Input('create-graph-button', 'value')])
def createGraphButtonText(value):
    if value==1:
        return 'submit'
    if value==2:
        return 'created'
    else:
        return 'create graph'

@app.callback(
    Output('submit-path-button', 'children'),
    [Input('submit-path-button', 'value')])
def createGraphButtonText(value):
    if value==1:
        return 'submit path'
    if value==2:
        return 'path submitted'
    else:
        return 'submit path'
# BUTTON TEXT END #

# ADD TRACE BUTTON CALLBACKS #
@app.callback(
    Output('traces-container', 'children'),
    [Input('add-trace-button', 'n_clicks')])
def addTrace(n_clicks):
    if n_clicks!=None:
        chldrn=[]
        i = n_clicks
        n_traces.append(n_clicks)
        df = readData(data_path[0])
        traces_dict[graph_name[0]]['trace_'+str(i)]={}
        traces_dict[graph_name[0]]['trace_'+str(i)]['data_frame']=df
        for i in range(1,n_clicks+1):
            chldrn.append(html.H3('trace:'+str(i)))
            chldrn.append(dcc.Dropdown(id='x-col-'+str(i),options=[{'label':a, 'value':a} for a in df.columns],value=refreshXColForTrace(i)))
            chldrn.append(dcc.Dropdown(id='y-col-'+str(i),options=[{'label':a, 'value':a} for a in df.columns],value=refreshYColForTrace(i)))
            chldrn.append(dcc.Dropdown(id='trace-type-'+str(i),options=[{'label': 'scatter', 'value': 'scatter'},
                                                                        {'label': 'bar', 'value': 'bar'}],value=refreshTypeForTrace(i)))

        return chldrn

for i in range(1,10):
    try:
        app.callback(output=Output('traces-container','x-col-'+str(i)),
                             inputs=[Input('x-col-'+str(i),'value'),
                                     Input('x-col-'+str(i),'id')])(update_x_col)
        app.callback(output=Output('traces-container','y-col-'+str(i)),
                             inputs=[Input('y-col-'+str(i),'value'),
                                     Input('x-col-'+str(i),'id')])(update_y_col)
        app.callback(output=Output('traces-container','type'+str(i)),
                             inputs=[Input('trace-type-'+str(i),'value'),
                                     Input('x-col-'+str(i),'id')])(update_trace_type)

        app.callback(output=Output('body-container','trace-'+str(i)),
                             inputs=[Input('x-col-'+str(i),'value'),
                                     Input('y-col-'+str(i),'value'),
                                     Input('trace-type-'+str(i),'value')])(update_counter)
    except:
        pass
