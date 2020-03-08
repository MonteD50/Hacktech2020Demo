import plotly
import plotly.graph_objs as go
import json 

X_demo_overall_one_day_data = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16]

y_demo_finance_one_day_data = [0, 0.34, 0, 0.5, 0, -0.456, 0.45, -0.4654, 0.645, 0.145, 0.235, 0.675, -0.3, 0.5456, 0.54, 0.6]

y_demo_health_one_day_data = [0.65, 0.43, 0, 0, 0, -0.12, 0.5, -0.65, 0.97, 0.32, 0.56, 0.675, -0.893, 0.54, 0.675, 0.89]

y_demo_productivity_one_day_data = [0.564, 0, 0, 0.5, 0.43, -0.33, 0.455, -0.143, 0.153, 0.76, 0.21, 0.675, -0.344, 0.967, 0.565, 0.766]

y_demo_overall_one_day_data = []
for i in range(len(y_demo_finance_one_day_data)):
    avg = (y_demo_finance_one_day_data[i] + y_demo_health_one_day_data[i] + y_demo_productivity_one_day_data[i]) / 3
    y_demo_overall_one_day_data.append(avg)

def _overall_graph():
    first_data_point = y_demo_overall_one_day_data[0]
    last_data_point = y_demo_overall_one_day_data[-1]

    data = go.Figure().add_trace(go.Scatter(x=X_demo_overall_one_day_data, y=y_demo_overall_one_day_data, name="Overall",
                         line_color='white')).update_layout(title_text='Overall',
                  xaxis_rangeslider_visible=True, autosize=True,width=750, height=650, margin=dict(l=50,r=50,b=100,pad=4), plot_bgcolor='black',xaxis_showgrid=False, yaxis_showgrid=False)
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def _health_graph():
    data = go.Figure().add_trace(go.Scatter(x=X_demo_overall_one_day_data, y=y_demo_health_one_day_data, name="Health",
                         line_color='blue')).update_layout(title_text='Health',
                  xaxis_rangeslider_visible=True, autosize=True,width=500, height=500, margin=dict(l=50,r=50,b=100,pad=4), plot_bgcolor='black',xaxis_showgrid=False, yaxis_showgrid=False)
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def _finance_graph():

    data = go.Figure().add_trace(go.Scatter(x=X_demo_overall_one_day_data, y=y_demo_finance_one_day_data, name="Finance",
                         line_color='red')).update_layout(title_text='Finance',
                  xaxis_rangeslider_visible=True, autosize=True,width=500, height=500, margin=dict(l=50,r=50,b=100,pad=4), plot_bgcolor='black',xaxis_showgrid=False, yaxis_showgrid=False)
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def _productivity_graph():
    data = go.Figure().add_trace(go.Scatter(x=X_demo_overall_one_day_data, y=y_demo_productivity_one_day_data, name="Productivity",
                         line_color='green')).update_layout(title_text='Productivity',
                  xaxis_rangeslider_visible=True, autosize=True,width=500, height=500, margin=dict(l=50,r=50,b=100,pad=4), plot_bgcolor='black',xaxis_showgrid=False, yaxis_showgrid=False)
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def _excersie_graph():
    y_demo_walked_one_day_data = [4.1, 2.3, 4.5, 6.5,3.3,7.8, 4.4, 4.4, 3.4, 6.5, 4.3, 4.9, 4.0, 4.9, 3.97, 4.32]
    data = go.Figure().add_trace(go.Bar(x=X_demo_overall_one_day_data, y=y_demo_walked_one_day_data, name="Miles Walked")).update_layout(title_text='Miles Walked',yaxis_title="Miles",xaxis_rangeslider_visible=True, autosize=True,width=500, height=500, margin=dict(l=50,r=50,b=100,pad=4), plot_bgcolor='black',xaxis_showgrid=False, yaxis_showgrid=False)
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def _calorie_graph():
    y_demo_calorie_one_day_data = [1893, 2432, 1478, 1900,2345,1976, 1673, 2497,3172, 2532, 2531, 2231, 2763, 3521, 2341, 2214]
    data = go.Figure().add_trace(go.Bar(x=X_demo_overall_one_day_data, y=y_demo_calorie_one_day_data, name="Calorie Intake")).update_layout(title_text='Calorie Intake',yaxis_title="Calories",xaxis_rangeslider_visible=True, autosize=True,width=500, height=500, margin=dict(l=50,r=50,b=100,pad=4), plot_bgcolor='black',xaxis_showgrid=False, yaxis_showgrid=False)
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def _revenue_graph():
    y_demo_revenue_one_day_data = [0, 0, 0, 0,0,0, 0, 0,0, 0, 0,0, 0, 0, 0, 0]
    data = go.Figure().add_trace(go.Scatter(x=X_demo_overall_one_day_data, y=y_demo_revenue_one_day_data, name="Profit")).update_layout(title_text='Profit Made From Selling to Advertisers',yaxis_title="$", autosize=True,width=500, height=500, margin=dict(l=50,r=50,b=100,pad=4), plot_bgcolor='black',xaxis_showgrid=False, yaxis_showgrid=False)
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
