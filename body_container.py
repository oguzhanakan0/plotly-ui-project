# body_container
def create_callback(output_element,retfunc):
    """creates a callback function"""
    def callback(*input_values):
        return retfunc(*input_values)
    return callback
def updateXCol(x_col,idn):
    traces_dict[graph_name[0]]['trace_'+str(idn[-1])]['x_column']=x_col
def updateYCol(y_col,idn):
    traces_dict[graph_name[0]]['trace_'+str(idn[-1])]['y_column']=y_col
def updateType(trace_type,idn):
    traces_dict[graph_name[0]]['trace_'+str(idn[-1])]['trace_type']=trace_type
def updateCounter(x_col,y_col,trace_type):
    counter[0]+=1
    return counter[0]

def updateGraph(title='Graph Title', graph_width=640, graph_height=480, trace_1=None, trace_2=None, trace_3=None, trace_4=None, trace_5=None, trace_6=None, trace_7=None, trace_8=None, trace_9=None, trace_10=None, name=None, opacity=None, showlegend=None,showmode=None,line_color=None,line_dash=None,line_shape=None,line_width=None,line_smoothing=None,marker_size=None,marker_color=None,marker_symbol=None,marker_border_color=None,marker_border_width=None,xaxis=None,yaxis=None,bar_color=None,bar_border_width=None,bar_border_color=None,bar_width=None,visibility=None):
    try:counter[0]+=1
    except: pass
    try:layout_dict[graph_name[0]]['title']={'text': title, 'xref': 'paper'}
    except: pass
    try:layout_dict[graph_name[0]]['width']=graph_width
    except: pass
    try:layout_dict[graph_name[0]]['height']=graph_height
    except: pass
    try:
        filled_traces=[]
        for i in traces_dict[graph_name[0]].keys():
            if (traces_dict[graph_name[0]][i]['trace_type']!=None and
                traces_dict[graph_name[0]][i]['x_column']!=None and
                traces_dict[graph_name[0]][i]['y_column']!=None):
                filled_traces.append(i)
        traces_dict_actual={graph_name[0]:{}}
        for j in filled_traces:
            traces_dict_actual[graph_name[0]][j]=traces_dict[graph_name[0]][j]

        myfig=Graph(graph_name[0],traces_dict=traces_dict_actual,layout_dict=layout_dict).draw()
        return dcc.Graph(id='graph-itself',figure=myfig)
    except: return dcc.Graph(id='graph-itself',figure=go.Figure(data=[],layout={'width':1200,'height':600}))

def readData(path):
    ext = path[path.rfind('.')+1:]
    if ext == 'xlsx':
        return pd.read_excel(path)
    elif ext == 'pkl':
        return pd.read_pickle(path)
    elif ext == 'csv':
        return pd.read_csv(path)
    else:
        return None

def refreshXColForTrace(i):
    try:
        a = traces_dict[graph_name[0]]['trace_'+str(i)]['x_column']
        return a
    except:
        return None
def refreshYColForTrace(i):
    try:
        a = traces_dict[graph_name[0]]['trace_'+str(i)]['y_column']
        return a
    except:
        return None
def refreshTypeForTrace(i):
    try:
        a = traces_dict[graph_name[0]]['trace_'+str(i)]['trace_type']
        return a
    except:
        return None

update_x_col = create_callback(Output('a','b'),updateXCol)
update_y_col = create_callback(Output('a','b'),updateYCol)
update_trace_type = create_callback(Output('a','b'),updateType)
update_counter = create_callback(Output('a','b'),updateCounter)
update_graph = create_callback(Output('a','b'),updateGraph)
