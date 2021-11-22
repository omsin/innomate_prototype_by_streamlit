from helper_function import *

def page_one():
    df1 = pd.DataFrame(np.random.normal(30000, 1000, 100),
                       index=pd.date_range(
                           end=datetime.today().strftime("%d/%m/%Y"),
                           periods=100
                       ).tolist())
    df2 = pd.DataFrame(np.random.normal(2, 1, 100),
                       index=pd.date_range(
                           end=datetime.today().strftime("%d/%m/%Y"),
                           periods=100
                       ).tolist())
    df3 = pd.DataFrame(np.random.normal(15000, 5000, 100),
                       index=pd.date_range(
                           end=datetime.today().strftime("%d/%m/%Y"),
                           periods=100
                       ).tolist())

    df = pd.concat([df1, df2, df3], axis=1)
    df.columns = ["Amount Spent", "ROAS", "Revenue"]
    df.index = df.index.strftime("%d/%m/%Y")

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
