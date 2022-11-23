import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as make_subplots
from streamlit_plotly_events import plotly_events


def initialization_state():
    pass


def reset_state_callback():
    pass


def row_ui_1():
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([0.5, 0.55, 2, 0.3, 0.3, 0.3, 1, 2])

    with col1:
        st.write('STJDAP OEE')
        st.empty()
        st.header('59%')

    with col2:
        st.write('Performance')
        st.subheader('71%')
        st.write('Availability')
        st.subheader('94%')
        st.write('Quality')
        st.subheader('88%')

    with col3:
        fig = draw_barchart()

        st.write('STJDAP OEE by Shift')
        selected_data = plotly_events(fig,
                                      select_event=True,)
        # st.plotly_chart(fig, use_container_width=True)
        # st.write(selected_data)

    percent_list = [50, 79, 38, 32, 50, 58, 92, 40, 53]

    selected_x = [data['x'] for data in selected_data]

    if selected_x:
        for i, x in enumerate(selected_x):
            percent_list[i] = x

    with col4:
        st.write('  A')

        for percent in percent_list[:3]:
            st.markdown(f'''<div style="background-color : black; color : white; width:50px;
             height:50px; padding : 12px; margin : 3px;">{percent}%<div>''',
                        unsafe_allow_html=True)

        # st.markdown(f'''<div style="background-color : red; color : white; width:50px;
        #          height:50px; padding : 12px; margin : 3px;">60%<div>''',
        #             unsafe_allow_html=True)
        # st.markdown(f'''<div style="background-color : blue; color : white; width:50px;
        #          height:50px; padding : 12px; margin : 3px;">70%<div>''',
        #             unsafe_allow_html=True)

    with col5:
        st.write('  B')
        for percent in percent_list[3:6]:
            st.markdown(f'''<div style="background-color : green; color : white; width:50px;
                     height:50px; padding : 12px; margin : 3px;">{percent}%<div>''',
                        unsafe_allow_html=True)
        # st.markdown(f'''<div style="background-color : coral; color : white; width:50px;
        #                  height:50px; padding : 12px; margin : 3px;">60%<div>''',
        #             unsafe_allow_html=True)
        # st.markdown(f'''<div style="background-color : yellow; color : black; width:50px;
        #                  height:50px; padding : 12px; margin : 3px;">70%<div>''',
        #             unsafe_allow_html=True)

    with col6:
        st.write('  C')
        for percent in percent_list[6:]:
            st.markdown(f'''<div style="background-color : red; color : white; width:50px;
                     height:50px; padding : 12px; margin : 3px;">{percent}%<div>''',
                        unsafe_allow_html=True)
        # st.markdown(f'''<div style="background-color : red; color : white; width:50px;
        #                  height:50px; padding : 12px; margin : 3px;">60%<div>''',
        #             unsafe_allow_html=True)
        # st.markdown(f'''<div style="background-color : blue; color : white; width:50px;
        #                  height:50px; padding : 12px; margin : 3px;">70%<div>''',
        #             unsafe_allow_html=True)

    with col7:
        st.write('time gain/loss')
        st.header('11.3 Hours')
        st.write('Total DoingTime')
        st.header('21.7 Hours')

    with col8:
        circle_fig = draw_circle_chart()
        selected_circle_data = plotly_events(circle_fig,
                                             select_event=True)
        # st.plotly_chart(circle_fig, use_container_width=True)


def draw_barchart():
    # top_labels = ['Strongly<br>agree', 'Agree', 'Neutral', 'Disagree',
    #               'Strongly<br>disagree']

    colors = ['rgba(38, 24, 74, 0.8)', 'rgba(28, 28, 35, 0.8)',
              'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
              'rgba(190, 192, 213, 1)']

    x_data = [[54, 46],
              [78, 22],
              [27, 73],
              [66, 34]]

    y_data = ['54%',
              '78%',
              '27%',
              '66%']

    fig = go.Figure()

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig.add_trace(go.Bar(
                x=[xd[i]], y=[yd],
                orientation='h',
                marker=dict(
                    color=colors[i],
                    line=dict(color='rgb(248, 248, 249)', width=0)
                )
            ))

    fig.update_layout(
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
            # domain=[1, 1]
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        barmode='stack',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(l=0, r=0, t=10, b=0),
        showlegend=False,
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='y',
                                x=0, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False, align='right'))
        # labeling the first percentage of each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=xd[0] / 2, y=yd,
                                text=str(xd[0]) + '%',
                                font=dict(family='Arial', size=14,
                                          color='rgb(248, 248, 255)'),
                                showarrow=False))
        # labeling the first Likert scale (on the top)
        # if yd == y_data[-1]:
        #     annotations.append(dict(xref='x', yref='paper',
        #                             x=xd[0] / 2, y=1.1,
        #                             text=top_labels[0],
        #                             font=dict(family='Arial', size=14,
        #                                       color='rgb(67, 67, 67)'),
        #                             showarrow=False))
        space = xd[0]
        for i in range(1, len(xd)):
            if i != 0:break
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i] / 2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            # if yd == y_data[-1]:
            #     annotations.append(dict(xref='x', yref='paper',
            #                             x=space + (xd[i] / 2), y=1.1,
            #                             text=top_labels[i],
            #                             font=dict(family='Arial', size=14,
            #                                       color='rgb(67, 67, 67)'),
            #                             showarrow=False))
            space += xd[i]

    fig.update_layout(annotations=annotations)
    fig.update_layout(
        autosize=False,
        width=400,
        height=200,
        )

    return fig


def draw_circle_chart():
    labels = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
              "Rest of World"]

    fig = go.Figure()

    # fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=[16, 15, 12, 6, 5, 4, 42], name="GHG Emissions"))
    # fig.add_trace(go.Pie(labels=labels, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
    #               1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    # fig.update_layout(
    #     title_text="Global Emissions 1990-2011",
    #     # Add annotations in the center of the donut pies.
    #     annotations=[dict(text='GHG', x=1, y=1, font_size=20, showarrow=False),
    #                  dict(text='CO2', x=0.82, y=0.5, font_size=20, showarrow=False)
    #                  ])

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=False,
        width=300,
        height=250
    )

    return fig


def main():
    row_ui_1()
    # row_ui_1()
    # row_ui_1()


if __name__ == '__main__':
    st.set_page_config(page_title='first_page', layout='wide', initial_sidebar_state="collapsed",)
    initialization_state()
    main()
