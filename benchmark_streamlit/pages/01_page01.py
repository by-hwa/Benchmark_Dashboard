import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events


def initialization():
    st.session_state['year_value'] = dict()
    st.session_state.count = 0
    pass


def row_ui():
    col = st.columns([1, 3, 1.5, 1.5])
    year_value = {'2018': list(), '2019': list()}

    with col[0]:
        st.write('Minute')
        st.subheader('21.2 min')
        st.write('!!!')
        st.subheader('9.0 min')
        st.subheader('Total Downtime')
        st.header('30.2min')

    with col[1]:
        fig = draw_linechart()
        # st.plotly_chart(fig, use_container_width=True)
        selected_data = plotly_events(fig,
                                      select_event=True,
                                      key=f'linechart_key_{st.session_state.count}')

        st.write(selected_data)

        if selected_data:
            st.write(selected_data[0]['x'])
            y, m, d = selected_data[0]['x'].split('-')

            if y in st.session_state.year_value:
                st.session_state.year_value[y].append(selected_data[0]['y'])
            else:
                st.session_state.year_value[y] = [selected_data[0]['y']]

        st.write(st.session_state)

    with col[2]:
        fig = draw_barchart()
        st.plotly_chart(fig, use_container_width=True)
        st.plotly_chart(fig, use_container_width=True)
        st.plotly_chart(fig, use_container_width=True)

    with col[3]:
        fig = draw_barchart()
        fig.update_layout(height=170)
        st.plotly_chart(fig, use_container_width=True)
        st.plotly_chart(fig, use_container_width=True)


def draw_linechart():
    df = px.data.stocks()
    fig = px.line(df, x='date', y='GOOG')
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=False,
        width=500,
        height=420)
    return fig


def draw_barchart():
    # top_labels = ['Strongly<br>agree', 'Agree', 'Neutral', 'Disagree',
    #               'Strongly<br>disagree']

    colors = ['rgba(38, 24, 74, 0.8)', 'rgba(28, 28, 35, 0.8)',
              'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
              'rgba(190, 192, 213, 1)']

    x_data = [[54, 46],
              [78, 22],
              [27, 73],
              [66, 34],]

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
        margin=dict(l=0, r=0, t=0, b=0),
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
        width=30,
        height=100
    )

    return fig


def main():
    row_ui()


if __name__ == '__main__':
    st.set_page_config(page_title="second page", layout='wide', initial_sidebar_state='collapsed')
    initialization()
    main()
