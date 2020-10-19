# init, graph
# coding: utf-8

# In[2]:


import pandas as pd
import plotly as plt
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot
init_notebook_mode()


# In[7]:


''' Processes data according to it's chart type and creates trace code.
    x_column: x axis
    y_column: y axis
    trace_type: Chart type
'''

class trace():

    def __init__(self, t_dict):
        self.x = t_dict["data_frame"][t_dict["x_column"]]
        self.y = t_dict["data_frame"][t_dict["y_column"]]
        self.t_type = t_dict["trace_type"]
        self.param_dict = t_dict.copy()
        self.param_dict.pop('data_frame')
        self.param_dict.pop('trace_type')
        self.param_dict.pop('x_column')
        self.param_dict.pop('y_column')

        self.param_dict['x']=list(self.x)
        self.param_dict['y']=list(self.y)

    def create_trace(self):
        if self.t_type == "bar": return self.create_bar()
        elif self.t_type == "scatter": return self.create_scatter()

    def create_bar(self):
        self.param_dict_bar = self.param_dict.copy()
        try: del self.param_dict_bar['mode']
        except: pass
        try: del self.param_dict_bar['line']
        except: pass
        try: del self.param_dict_bar['marker']['symbol']
        except: pass
        try: del self.param_dict_bar['marker']['size']
        except: pass
        t = go.Bar(**self.param_dict_bar)
        return t

    def create_scatter(self):
        self.param_dict_scatter = self.param_dict.copy()
        try: del self.param_dict_scatter['width']
        except: pass
        t = go.Scatter(**self.param_dict_scatter)
        return t



# In[13]:


class layout():
    def __init__(self, l_dict):
        self.layout = {}
        try: self.layout["title"] = l_dict["title"]
        except: pass
        try: self.layout["autosize"] = l_dict["autosize"]
        except: pass
        try: self.layout["width"] = l_dict["width"]
        except: pass
        try: self.layout["height"] = l_dict["height"]
        except: pass
        try: self.layout["barmode"] = l_dict["barmode"]
        except: pass
        try: self.layout["legend"] = l_dict["legend"]
        except: pass
        try: self.layout["text"] = l_dict["text"]
        except: pass

    def create_layout(self):
        return self.layout


# In[32]:


''' Processes trace code dictionary, evaluates every trace code individually and draws graphs.
    Input: Graph_name
    Output: Plotly figure
'''

class Graph():

    def __init__(self, graph_name,traces_dict,layout_dict):
        self.name = graph_name
        self.trace_dictionary = traces_dict[graph_name].copy()
        self.traces = []
        for i in self.trace_dictionary:
            self.traces.append(trace(self.trace_dictionary[i]).create_trace())
        self.layout = layout(layout_dict[graph_name]).create_layout()

    def draw(self):
        # su anki ekrana cizdirmek icin: iplot(go.Figure(data=self.traces, layout=self.layout))
        return go.Figure(data=self.traces, layout=self.layout)
    def getData(self):
        return self.traces
    def getLayout(self):
        return self.layout


# In[34]:


## test area
#df = pd.DataFrame([[8,2,3],[9,5,6],[10,8,9]], columns = ["c1","c2","c3"], index = ["r1","r2","r3"])
#
#traces_dict = {'graph_1':
#                         {
#                         "trace_1" : {"data_frame" : df,
#                                     "trace_type" : "scatter",
#                                     "x_column" : "c1",
#                                     "y_column" : "c2" },
#                         "trace_2" : {"data_frame" : df,
#                                     "trace_type" : "bar",
#                                     "x_column" : "c1",
#                                     "y_column" : "c3" },
#                         "trace_3" : {"data_frame" : df,
#                                     "trace_type" : "bar",
#                                     "x_column" : "c1",
#                                     "y_column" : "c3" }
#                        }
#                   }
#
#layout_dict = {'graph_1':
#                         {"title" : "Banu",
#                          "width" : 640,
#                          "height": 480}
#                    }
#
#myfigure = Graph('graph_1')
#iplot(myfigure.draw())

