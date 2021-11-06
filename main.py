from helper_function import *

st.set_page_config(
    page_title='Innomate',
    initial_sidebar_state="expanded",
    layout = "wide"
)

st.sidebar.image(
    "image/Innomate_Logo.png",
    width=300,
)
st.image("image/digital-futuristic-analytics-hologram-working-character-vector-design-illustration_41742-66.jpg", width=450)
menu = ["Home", "Log In", "Sign Up"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    original_title = '<p style="color:#3A5E80; font-size: 50px; font-weight: bold;">Advanced Digital Marketing Platform</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.caption('Developed by Innomate.')
    st.subheader('Digital advertisement spending in Thailand is expected to reach 22,800 million Baht in 2021 with 8% growth rate')
    st.subheader('While the old media spending was dwindled by -18%.....')
    st.subheader('“ Digital is now a frontline and competition is fiercer than ever before”')

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Problem Identification</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image1 = Image.open('image/innomate_aws-03cut.jpg')
    st.image(image1, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">The Future is digital, Transformation is now</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image2 = Image.open('image/innomate_aws-05cut.jpg')
    st.image(image2, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Meet Innomate</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image3 = Image.open('image/innomate_aws-04cut.jpg')
    st.image(image3, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Target customer</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image4 = Image.open('image/innomate_aws-06cut.jpg')
    st.image(image4, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Marketing Plan</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image5 = Image.open('image/innomate_aws-07cut.jpg')
    st.image(image5, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Competitive Advantages & Core Values</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image6 = Image.open('image/innomate_aws-13cut.jpg')
    st.image(image6, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Revenue Stream</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image6 = Image.open('image/innomate_aws-08cut.jpg')
    st.image(image6, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Developing Timeline</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image7 = Image.open('image/innomate_aws-09cut.jpg')
    st.image(image7, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Our services and Potential Expansion</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image8 = Image.open('image/innomate_aws-10cut.jpg')
    st.image(image8, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">System Landscape</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image9 = Image.open('image/innomate_aws-11cut.jpg')
    st.image(image9, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Vision Statement</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image10 = Image.open('image/innomate_aws-14cut.jpg')
    st.image(image10, width=850)

    original_title = '<p style="color:#3A5E80; font-size: 35px; font-weight: bold;">Executive Level</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    image10 = Image.open('image/innomate_aws-15cut.jpg')
    st.image(image10, width=850)



elif choice == "Sign Up":


    st.sidebar.subheader("Create New Account")
    new_user = st.sidebar.text_input("Username")
    new_password = st.sidebar.text_input("Password", type="password")
    confirm_password = st.sidebar.text_input("Confirm Password", type="password")
    if st.sidebar.button("Signup"):
        create_usertable()
        if new_password == confirm_password:
            add_userdata(
                new_user, make_hashes(new_password)
            )
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
        else:
            st.warning("Please make sure your password is match")




elif choice == "Log In":

    st.sidebar.subheader("""Login Section""")

    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.checkbox("Login"):
        # create_usertable()
        hashed_pswd = make_hashes(password)

        result = login_user(username, check_hashes(password, hashed_pswd))
        if result:



            choice1 = st.radio(
                "What's page do you want to go?",
                ('Page 1', 'Page 2', 'Page 3', 'Page 4'))
            if choice1 == 'Page 1':
                title = 'Main Source for News'
                labels = ['Television', 'Newspaper', 'Internet', 'Radio']
                colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)']

                mode_size = [8, 8, 12, 8]
                line_size = [2, 2, 4, 2]

                x_data = np.vstack((np.arange(2001, 2014),) * 4)

                y_data = np.array([
                    [74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 69],
                    [45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28],
                    [13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
                    [18, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 23],
                ])

                fig = go.Figure()

                for i in range(0, 4):
                    fig.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
                                             name=labels[i],
                                             line=dict(color=colors[i], width=line_size[i]),
                                             connectgaps=True,
                                             ))

                    # endpoints
                    fig.add_trace(go.Scatter(
                        x=[x_data[i][0], x_data[i][-1]],
                        y=[y_data[i][0], y_data[i][-1]],
                        mode='markers',
                        marker=dict(color=colors[i], size=mode_size[i])
                    ))

                fig.update_layout(
                    xaxis=dict(
                        showline=True,
                        showgrid=False,
                        showticklabels=True,
                        linecolor='rgb(204, 204, 204)',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                            family='Arial',
                            size=12,
                            color='rgb(82, 82, 82)',
                        ),
                    ),
                    yaxis=dict(
                        showgrid=False,
                        zeroline=False,
                        showline=False,
                        showticklabels=False,
                    ),
                    autosize=False,
                    margin=dict(
                        autoexpand=False,
                        l=100,
                        r=20,
                        t=110,
                    ),
                    showlegend=False,
                    plot_bgcolor='white'
                )

                annotations = []

                # Adding labels
                for y_trace, label, color in zip(y_data, labels, colors):
                    # labeling the left_side of the plot
                    annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                            xanchor='right', yanchor='middle',
                                            text=label + ' {}%'.format(y_trace[0]),
                                            font=dict(family='Arial',
                                                      size=16),
                                            showarrow=False))
                    # labeling the right_side of the plot
                    annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
                                            xanchor='left', yanchor='middle',
                                            text='{}%'.format(y_trace[11]),
                                            font=dict(family='Arial',
                                                      size=16),
                                            showarrow=False))
                # Title
                annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                        xanchor='left', yanchor='bottom',
                                        text='Main Source for News',
                                        font=dict(family='Arial',
                                                  size=30,
                                                  color='rgb(37,37,37)'),
                                        showarrow=False))
                # Source
                annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                                        xanchor='center', yanchor='top',
                                        text='Source: PewResearch Center & ' +
                                             'Storytelling with data',
                                        font=dict(family='Arial',
                                                  size=12,
                                                  color='rgb(150,150,150)'),
                                        showarrow=False))

                fig.update_layout(annotations=annotations)

                st.plotly_chart(fig)
            elif choice1 == 'Page 2':

                x1 = np.random.randn(200) - 2
                x2 = np.random.randn(200)
                x3 = np.random.randn(200) + 2

                fig = go.Figure(data=[go.Table(
                    header=dict(values=[ 'A Source', 'B Source', 'C Source'],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                    cells=dict(values=[ x1, x2,x3],
                               line_color='darkslategray',
                               fill_color='lightcyan',
                               align='left'))
                ])

                fig.update_layout(width=1200, height=500)
                st.plotly_chart(fig)
                with st.expander("See explanation"):
                    hist_data = [x1, x2, x3]
                    group_labels = ['A Source', 'B Source', 'C Source']
                    fig1 = ff.create_distplot(
                        hist_data, group_labels, bin_size=[.1, .25, .5])
                    fig1.update_layout(width=1200, height=500)
                    st.plotly_chart(fig1, use_container_width=True)

                col4, col5 = st.columns([6, 6])
                with col4:
                    df2 = px.data.tips()
                    fig2 = px.sunburst(df2, path=['sex', 'day', 'time'], values='total_bill', color='time',
                                       color_discrete_map={'(?)': 'black', 'Lunch': 'gold', 'Dinner': 'darkblue'})
                    st.plotly_chart(fig2)
                with col5:
                    df = px.data.tips()
                    fig = px.sunburst(df, path=['day', 'time', 'sex'], values='total_bill')
                    st.plotly_chart(fig)



            elif choice1 == 'Page 3':
                df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/sales_success.csv')
                print(df.head())

                levels = ['salesperson', 'county', 'region']  # levels used for the hierarchical chart
                color_columns = ['sales', 'calls']
                value_column = 'calls'


                def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
                    """
                    Build a hierarchy of levels for Sunburst or Treemap charts.

                    Levels are given starting from the bottom to the top of the hierarchy,
                    ie the last level corresponds to the root.
                    """
                    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
                    for i, level in enumerate(levels):
                        df_tree = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
                        dfg = df.groupby(levels[i:]).sum()
                        dfg = dfg.reset_index()
                        df_tree['id'] = dfg[level].copy()
                        if i < len(levels) - 1:
                            df_tree['parent'] = dfg[levels[i + 1]].copy()
                        else:
                            df_tree['parent'] = 'total'
                        df_tree['value'] = dfg[value_column]
                        df_tree['color'] = dfg[color_columns[0]] / dfg[color_columns[1]]
                        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
                    total = pd.Series(dict(id='total', parent='',
                                           value=df[value_column].sum(),
                                           color=df[color_columns[0]].sum() / df[color_columns[1]].sum()))
                    df_all_trees = df_all_trees.append(total, ignore_index=True)
                    return df_all_trees


                df_all_trees = build_hierarchical_dataframe(df, levels, value_column, color_columns)
                average_score = df['sales'].sum() / df['calls'].sum()

                fig = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]], )

                fig.add_trace(go.Sunburst(
                    labels=df_all_trees['id'],
                    parents=df_all_trees['parent'],
                    values=df_all_trees['value'],
                    branchvalues='total',
                    marker=dict(
                        colors=df_all_trees['color'],
                        colorscale='RdBu',
                        cmid=average_score),
                    hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
                    name=''
                ), 1, 1)

                fig.add_trace(go.Sunburst(
                    labels=df_all_trees['id'],
                    parents=df_all_trees['parent'],
                    values=df_all_trees['value'],
                    branchvalues='total',
                    marker=dict(
                        colors=df_all_trees['color'],
                        colorscale='RdBu',
                        cmid=average_score),
                    hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
                    maxdepth=2
                ), 1, 2)

                fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))
                st.plotly_chart(fig)



            else:

                col1, col2, col3 = st.columns([4, 4, 4])

                with col1:
                    st.header("Random Graph1")
                    chart_data = pd.DataFrame(
                    np.random.randn(20, 3),
                    columns=['a', 'b', 'c'])
                    st.line_chart(chart_data)
                with col2:
                    st.header("Random Graph2")
                    chart_data = pd.DataFrame(
                    np.random.randn(20, 3),
                    columns=['a', 'b', 'c'])
                    st.area_chart(chart_data)

                with col3:
                    st.header("Random Graph3")
                    chart_data = pd.DataFrame(
                        np.random.randn(50, 3),
                        columns = ["a", "b", "c"])
                    st.bar_chart(chart_data)







        else:
            st.warning("Incorrect Username/Password")






sentence = st.text_input('Interested in us, please insert your email:')

if st.button('Submit'):
   st.write("Done")
   my_file = open("email_log.txt")
   file_content = my_file.read()
   my_file.seek(0)

   my_file = open("email_log.txt", "w")
   my_file.write(file_content+"\n"+sentence)
   my_file.seek(0)

   my_file.close()