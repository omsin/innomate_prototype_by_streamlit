from helper_function import *

def page_two_help():
    col1, col2 = st.columns([1, 10])
    with col1.container():
        st.image(
            "image/icon-f.jpg",
            width=100
        )
    with col2.container():
        st.text('')
        Custom_title = '<p style="color:#3A5E80; font-size: 20px; font-weight: bold;">Where to a launch Facebook as sets:</p>'
        st.markdown(Custom_title, unsafe_allow_html=True)
        st.title('')
    gen = st.checkbox('Launch into Innomate Optimized Structure')
    st.caption('it is recommended to launch different core audiences into different campaigns.')

    col01, col02, col03, col04, col05, col06 = st.columns([1, 2, 2, 8, 2, 2])
    with col01.container():
        Custom_01 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">Audiences</p>'
        st.markdown(Custom_01, unsafe_allow_html=True)
        st.subheader('')
        st.subheader('')
        st.text('')
        Custom_02 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">1</p>'
        st.markdown(Custom_02, unsafe_allow_html=True)
    with col02.container():
        Custom_01 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">Funnel stage</p>'
        st.markdown(Custom_01, unsafe_allow_html=True)
        st.subheader('')
        st.subheader('')
        st.text('')
        Custom_02 = '<p style="text-align: center; color:#3A5E80; font-size: 10px; font-weight: bold;">Acqusition Prospecting Lookalike Campain</p>'
        st.markdown(Custom_02, unsafe_allow_html=True)
    with col03.container():
        Custom_01 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">CBO Campaign</p>'
        st.markdown(Custom_01, unsafe_allow_html=True)
        st.subheader('')
        Cus01 = st.selectbox(
            '', ('Open', 'Close'))

    with col04.container():
        Custom_01 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">Name</p>'
        st.markdown(Custom_01, unsafe_allow_html=True)
        st.subheader('')
        title = st.text_input('', 'Innomate-Lookalike Campaign')

    with col05.container():
        Custom_01 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">CBO Campaign Objective</p>'
        st.markdown(Custom_01, unsafe_allow_html=True)
        Cus05 = st.selectbox(
            '', ('Convertion', ''))
    with col06.container():
        Custom_01 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">CBO Campaign Budget</p>'
        st.markdown(Custom_01, unsafe_allow_html=True)
        Cus05 = st.number_input('', min_value=0)
        st.caption('THB')

    gen0 = st.checkbox('Launch all audiences into a campaign of your choice')
    st.caption('Choose this option if you want to have all audiences in one campaign.')
    st.caption('All audiences will be launched into one campaign regardless of the core audience.')
    col001, col002, col003 = st.columns([1, 14, 2])
    with col001.container():
        Custom_01 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">Audiences</p>'
        st.markdown(Custom_01, unsafe_allow_html=True)
        st.subheader('')
        st.subheader('')
        st.text('')
        Custom_02 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">1</p>'
        st.markdown(Custom_02, unsafe_allow_html=True)
    with col002.container():
        Custom_01 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">Name</p>'
        st.markdown(Custom_01, unsafe_allow_html=True)
        st.subheader('')
        title = st.text_input('', 'Select Facebook Campaign')
    with col003.container():
        Custom_01 = '<p style="text-align: center; color:#3A5E80; font-size: 15px; font-weight: bold;">CBO Campaign Budget</p>'
        st.markdown(Custom_01, unsafe_allow_html=True)
        Cus001 = st.number_input(' ', min_value=0)
        st.caption('THB')
