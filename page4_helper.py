from helper_function import *

def page_four_help():

    with st.form("my_form000"):
        col1, col2, col3, col4 = st.columns([1, 4, 6, 1])
        with col1.container():
            st.image(
                "image/icon-1.jpg",
                width=100
            )
        with col2.container():
            Custom_title = '<p style="color:#3A5E80; font-size: 20px; font-weight: bold;">CUSTOM Campaign Level</p>'
            st.markdown(Custom_title, unsafe_allow_html=True)
            st.caption('Developed by Innomate.')
        with col3.container():
            st.caption('While the old media spending was dwindled by -18%.....')
            st.caption('“ Digital is now a frontline and competition is fiercer than ever before”')
        with col4.container():
            st.form_submit_button('Back')
    col5, col6 = st.columns([1, 4])
    with col5.container():
        st.title('')
        Custom_title = '<p style="text-align: center; color:#3A5E80; font-size: 25px; font-weight: bold;">Select the Task:</p>'
        st.markdown(Custom_title, unsafe_allow_html=True)
    with col6.container():
        option = st.selectbox(
        '',
        ('Increase Campaign Budget', ''))
    Custom_Mad = '<p style="color:#3A5E80; font-size: 15px; font-weight: bold;">Innomate will increase the campaign budget if:</p>'
    st.markdown(Custom_Mad, unsafe_allow_html=True)
    with st.form("my_form001"):
        col7, col8, col9, col10, col11 = st.columns([3, 3, 3, 3, 1])
        with col7.container():
            option0 = st.selectbox(
                '',
                ("Purchase ROAS", "Website Adds to Cart", "Website Purchases", "Cost per Website Purchase", "Hour Since Creation",
                 "Daily Budget", "Number of Ad Sets in Campaign", "Number of Active Ad Sets in Campaign", "Frequency","Spend"))


        with col8.container():
            option0 = st.selectbox(
                '',
                ('Today', 'Yesterday', 'Today and Yesterday', 'Last 3 day(incl.today)', 'Last 3 day(excl.today)',
                 'Last 7 day(incl.today)'))


        with col9.container():
            option0 = st.selectbox(
                '',
                ('=', '>=', '<=', '>', '<'))


        with col10.container():
            number0 = st.number_input('', min_value=0)


        with col11.container():
            st.title('')
            st.form_submit_button('Reset')
    with st.form("my_form002"):
        col7, col8, col9, col10, col11 = st.columns([3, 3, 3, 3, 1])
        with col7.container():
            option0 = st.selectbox(
                '',
                ("Purchase ROAS", "Website Adds to Cart", "Website Purchases", "Cost per Website Purchase", "Hour Since Creation",
                 "Daily Budget", "Number of Ad Sets in Campaign", "Number of Active Ad Sets in Campaign", "Frequency","Spend"))


        with col8.container():
            option0 = st.selectbox(
                '',
                ('Today', 'Yesterday', 'Today and Yesterday', 'Last 3 day(incl.today)', 'Last 3 day(excl.today)',
                 'Last 7 day(incl.today)'))


        with col9.container():
            option0 = st.selectbox(
                '',
                ('=', '>=', '<=', '>', '<'))


        with col10.container():
            number0 = st.number_input('', min_value=0)


        with col11.container():
            st.title('')
            st.form_submit_button('Reset')

    with st.form("my_form003"):
        col7, col8, col9, col10, col11 = st.columns([3, 3, 3, 3, 1])
        with col7.container():
            option0 = st.selectbox(
                '',
                ("Purchase ROAS", "Website Adds to Cart", "Website Purchases", "Cost per Website Purchase", "Hour Since Creation",
                 "Daily Budget", "Number of Ad Sets in Campaign", "Number of Active Ad Sets in Campaign", "Frequency","Spend"))


        with col8.container():
            option0 = st.selectbox(
                '',
                ('Today', 'Yesterday', 'Today and Yesterday', 'Last 3 day(incl.today)', 'Last 3 day(excl.today)',
                 'Last 7 day(incl.today)'))


        with col9.container():
            option0 = st.selectbox(
                '',
                ('=', '>=', '<=', '>', '<'))


        with col10.container():
            number0 = st.number_input('', min_value=0)


        with col11.container():
            st.title('')
            st.form_submit_button('Reset')
    agree = st.checkbox('Finish')
    st.title('')

    col05, col06 = st.columns([1, 4])
    with col05.container():
        st.title('')
        Custom_title = '<p style="text-align: center; color:#3A5E80; font-size: 25px; font-weight: bold;">Select the Task:</p>'
        st.markdown(Custom_title, unsafe_allow_html=True)
    with col06.container():
        option = st.selectbox(
            '',
            ('Decrease Campaign Budget', ''))
    Custom_Mad = '<p style="color:#3A5E80; font-size: 15px; font-weight: bold;">Innomate will decrease the campaign budget if:</p>'
    st.markdown(Custom_Mad, unsafe_allow_html=True)
    with st.form("my_form0001"):
        col7, col8, col9, col10, col11 = st.columns([3, 3, 3, 3, 1])
        with col7.container():
            option0 = st.selectbox(
                '',
                ("Purchase ROAS", "Website Adds to Cart", "Website Purchases", "Cost per Website Purchase",
                 "Hour Since Creation",
                 "Daily Budget", "Number of Ad Sets in Campaign", "Number of Active Ad Sets in Campaign", "Frequency",
                 "Spend"))

        with col8.container():
            option0 = st.selectbox(
                '',
                ('Today', 'Yesterday', 'Today and Yesterday', 'Last 3 day(incl.today)', 'Last 3 day(excl.today)',
                 'Last 7 day(incl.today)'))

        with col9.container():
            option0 = st.selectbox(
                '',
                ('=', '>=', '<=', '>', '<'))

        with col10.container():
            number0 = st.number_input('', min_value=0)

        with col11.container():
            st.title('')
            st.form_submit_button('Reset')

    with st.form("my_form0002"):
        col7, col8, col9, col10, col11 = st.columns([3, 3, 3, 3, 1])
        with col7.container():
            option0 = st.selectbox(
                '',
                ("Purchase ROAS", "Website Adds to Cart", "Website Purchases", "Cost per Website Purchase",
                 "Hour Since Creation",
                 "Daily Budget", "Number of Ad Sets in Campaign", "Number of Active Ad Sets in Campaign", "Frequency",
                 "Spend"))

        with col8.container():
            option0 = st.selectbox(
                '',
                ('Today', 'Yesterday', 'Today and Yesterday', 'Last 3 day(incl.today)', 'Last 3 day(excl.today)',
                 'Last 7 day(incl.today)'))

        with col9.container():
            option0 = st.selectbox(
                '',
                ('=', '>=', '<=', '>', '<'))

        with col10.container():
            number0 = st.number_input('', min_value=0)

        with col11.container():
            st.title('')
            st.form_submit_button('Reset')

    with st.form("my_form0003"):
        col7, col8, col9, col10, col11 = st.columns([3, 3, 3, 3, 1])
        with col7.container():
            option0 = st.selectbox(
                '',
                ("Purchase ROAS", "Website Adds to Cart", "Website Purchases", "Cost per Website Purchase",
                 "Hour Since Creation",
                 "Daily Budget", "Number of Ad Sets in Campaign", "Number of Active Ad Sets in Campaign", "Frequency",
                 "Spend"))

        with col8.container():
            option0 = st.selectbox(
                '',
                ('Today', 'Yesterday', 'Today and Yesterday', 'Last 3 day(incl.today)', 'Last 3 day(excl.today)',
                 'Last 7 day(incl.today)'))

        with col9.container():
            option0 = st.selectbox(
                '',
                ('=', '>=', '<=', '>', '<'))

        with col10.container():
            number0 = st.number_input('', min_value=0)

        with col11.container():
            st.title('')
            st.form_submit_button('Reset')

    agree01 = st.checkbox('Send')
    st.title('')
    st.title('')
    Custom_Due = '<p style="color:#3A5E80; font-size: 30px; font-weight: bold;">Date Schedule:</p>'
    st.markdown(Custom_Due, unsafe_allow_html=True)
    genre = st.radio("Your rule will either run continuously starting today or within a date range that you set.  Timezone: Asia/Bangkok",
                     ('Run Continuously', 'Between Specific Date'))
    if genre == 'Between Specific Date':
        col1, col2, col3, col4 = st.columns([2, 1, 2, 7])
        with col1.container():
            d0 = st.date_input("Select your Start Date")
        with col2.container():
            st.subheader('')
            st.markdown('<p style="text-align: center; color:black; font-size: 40px; font-weight: bold;">-</p>', unsafe_allow_html=True)

        with col3.container():
            d1 = st.date_input("Select your End Date")
        with col4.container():
            st.title('')

    Custom_Rea = '<p style="color:#3A5E80; font-size: 30px; font-weight: bold;">Realtime trigger activation scheduling:</p>'
    st.markdown(Custom_Rea, unsafe_allow_html=True)
    genre = st.radio("Choose whether you want your rule to be applied 24/7 or only on specific days/hours.  Timezone: Asia/Bangkok",
                     ('Run Continuous', 'On Specific Days/Hours'))