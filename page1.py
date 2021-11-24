from helper_function import *

def page_one():
    df1 = pd.read_csv("csv/df1.csv", index_col=0)
    df2 = pd.read_csv("csv/df2.csv", index_col=0)
    df3 = pd.read_csv("csv/df3.csv", index_col=0)


    df = pd.concat([df1, df2, df3], axis=1)
    df.columns = ["Amount Spent", "ROAS", "Revenue"]
    #df.index = df.index.strftime("%d/%m/%Y")
    st.title("Dashboard")
    st.write('### Full Dataset', df)
    selected_indices = st.multiselect('Select rows:', df.index)
    selected_rows = df.loc[selected_indices]
    st.write('### Selected Rows', selected_rows)
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
        st.columns((.1, 2, .1, 2, .1, 2, .1))
    with row0_1:
        df1.columns = ['earth']
        row0_1 = go.Figure()
        row0_1.add_trace(
            go.Scatter(x=list(df1.index), y=list(df1['earth'])))
        row0_1.update_layout(width=420, height=400)
        row0_1.update_layout(title_text="Amount Spent")
        row0_1.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward",

                             ),

                        dict(count=3,
                             label="3m",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6m",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="YTD",
                             step="year",
                             stepmode="todate"),
                        dict(step="all")

                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type="date", range=[df1.index[0], df1.index[31]]
            )
        )

        st.plotly_chart(row0_1)

    with row0_2:
        df2.columns = ['earth']
        row0_2 = go.Figure()
        row0_2.add_trace(
            go.Scatter(x=list(df2.index), y=list(df2['earth'])))
        row0_2.update_layout(width=420, height=400)
        row0_2.update_layout(title_text="ROAS")

        row0_2.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward"),
                        dict(count=3,
                             label="3m",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6m",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="YTD",
                             step="year",
                             stepmode="todate"),
                        dict(step="all")

                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type="date", range=[df1.index[0], df1.index[31]]
            )
        )
        st.plotly_chart(row0_2)
    with row0_3:
        df3.columns = ['earth']
        row0_3 = go.Figure()
        row0_3.add_trace(
            go.Scatter(x=list(df3.index), y=list(df3['earth'])))
        row0_3.update_layout(width=420, height=400)
        row0_3.update_layout(title_text="Revenue")

        row0_3.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward"),
                        dict(count=3,
                             label="3m",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6m",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="YTD",
                             step="year",
                             stepmode="todate"),
                        dict(step="all")

                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type="date", range=[df1.index[0], df1.index[31]]
            )
        )
        st.plotly_chart(row0_3)


    """

    df = pd.concat([df1, df2, df3], axis=1)
    df.columns = ["Amount Spent", "ROAS", "Revenue"]

    st.title("Dashboard")
    st.write('### Full Dataset', df)
    selected_indices = st.multiselect('Select rows:', df.index)
    selected_rows = df.loc[selected_indices]
    st.write('### Selected Rows', selected_rows)

    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
        st.columns((.1, 2, .1, 2, .1, 2, .1))
    with row0_1:
        row0_1.subheader("Amount Spent")
        row0_1.line_chart(df1.iloc[df1.shape[0] - 10:df1.shape[0]], width=250, height=200)
    with row0_2:
        row0_2.subheader("ROAS")
        row0_2.line_chart(df2.iloc[df2.shape[0] - 10:df2.shape[0]], width=250, height=200)
    with row0_3:
        row0_3.subheader("Revenue")
        row0_3.line_chart(df3.iloc[df3.shape[0] - 10:df3.shape[0]], width=250, height=200)
    """
