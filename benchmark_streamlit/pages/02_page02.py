import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np


def initialization():
    pass


def draw_barchart():
    # top_labels = ['Strongly<br>agree', 'Agree', 'Neutral', 'Disagree',
    #               'Strongly<br>disagree']

    colors = ['rgba(38, 24, 74, 0.8)', 'rgba(28, 28, 35, 0.8)',
              'rgba(38, 24, 74, 0.8)', 'rgba(28, 28, 35, 0.8)',
              'rgba(190, 192, 213, 1)']

    name = ['Auto', 'Manual']

    x_data = [[54, 46, 54, 46]]

    y_data = ['Execution']

    fig = go.Figure()

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig.add_trace(go.Bar(
                x=[xd[i]], y=[yd],
                orientation='h',
                name=name[i % 2],
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

    # for yd, xd in zip(y_data, x_data):
    #     # labeling the y-axis
    #     annotations.append(dict(xref='paper', yref='y',
    #                             x=0, y=yd,
    #                             xanchor='right',
    #                             text=str(yd),
    #                             font=dict(family='Arial', size=14,
    #                                       color='rgb(67, 67, 67)'),
    #                             showarrow=False, align='right'))
    #     # labeling the first percentage of each bar (x_axis)
    #     annotations.append(dict(xref='x', yref='y',
    #                             x=xd[0] / 2, y=yd,
    #                             text=str(xd[0]) + '%',
    #                             font=dict(family='Arial', size=14,
    #                                       color='rgb(248, 248, 255)'),
    #                             showarrow=False))
        # labeling the first Likert scale (on the top)
        # if yd == y_data[-1]:
        #     annotations.append(dict(xref='x', yref='paper',
        #                             x=xd[0] / 2, y=1.1,
        #                             text=top_labels[0],
        #                             font=dict(family='Arial', size=14,
        #                                       color='rgb(67, 67, 67)'),
        #                             showarrow=False))
        # space = xd[0]
        # for i in range(1, len(xd)):
        #     if i != 0:break
        #     # labeling the rest of percentages for each bar (x_axis)
        #     annotations.append(dict(xref='x', yref='y',
        #                             x=space + (xd[i] / 2), y=yd,
        #                             text=str(xd[i]) + '%',
        #                             font=dict(family='Arial', size=14,
        #                                       color='rgb(248, 248, 255)'),
        #                             showarrow=False))
            # labeling the Likert scale
            # if yd == y_data[-1]:
            #     annotations.append(dict(xref='x', yref='paper',
            #                             x=space + (xd[i] / 2), y=1.1,
            #                             text=top_labels[i],
            #                             font=dict(family='Arial', size=14,
            #                                       color='rgb(67, 67, 67)'),
            #                             showarrow=False))
            # space += xd[i]

    fig.update_layout(annotations=annotations)
    fig.update_layout(
        autosize=False,
        width=50,
        height=50
        )
    return fig


def draw_linechart(df: pd.DataFrame):
    fig = px.line(df)
    fig.update_layout(
        autosize=False,
        width=50,
        height=200,
        showlegend=False,
        xaxis = dict(
            visible=True,
            showgrid=False,
            showline=False,
            showticklabels=True,
            zeroline=False,
            # domain=[1, 1]
        ),
        yaxis = dict(
            visible=True,
            showgrid=False,
            showline=True,
            showticklabels=True,
            zeroline=False,
        ),
        margin=dict(l=0, r=0, t=0, b=0),
    )
    return fig


def main():
    st.header('Execution')
    fig = draw_barchart()
    st.plotly_chart(fig, use_container_width=True)

    col = st.columns([9, 1])

    df1 = pd.DataFrame(np.random.randn(10), columns=['aa'])
    df2 = pd.DataFrame(np.random.randn(10), columns=['aa'])
    df3 = pd.DataFrame(np.random.randn(10), columns=['aa'])

    with col[0]:
        fig = draw_linechart(df1)
        st.plotly_chart(fig, use_container_width=True)

        fig = draw_linechart(df2)
        st.plotly_chart(fig, use_container_width=True)

        fig = draw_linechart(df3)
        st.plotly_chart(fig, use_container_width=True)

    with col[1]:
        st.dataframe(df1, height=200)
        st.dataframe(df2, height=200)
        st.dataframe(df3, height=200)


if __name__ == '__main__':
    st.set_page_config(layout='wide')
    initialization()
    main()