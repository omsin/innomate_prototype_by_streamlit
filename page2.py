from helper_function import *
from page2_helper import *

def page_two():

    change_page_inner = 0

    st.title("Ads Creation")

    placeholder = st.empty()


    if change_page_inner == 0:
        with placeholder.container():
            row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row0_1:
                with st.form("my_form1"):
                    st.markdown('<p style="text-align: center; color:#3A5E80; font-size: 30px; font-weight: bold;">Acquistion</p>'
                                , unsafe_allow_html=True)
                    image3 = Image.open('image/icon.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1
            with row0_2:
                with st.form("my_form2"):
                    st.markdown(
                        '<p style="text-align: center; color:#3A5E80; font-size: 30px; font-weight: bold;">Retargeting</p>'
                        , unsafe_allow_html=True)
                    image3 = Image.open('image/icon-2.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 2
            with row0_3:
                with st.form("my_form3"):
                    st.markdown(
                        '<p style="text-align: center; color:#3A5E80; font-size: 30px; font-weight: bold;">Retention</p>'
                        , unsafe_allow_html=True)
                    image3 = Image.open('image/icon-3.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 3


    if change_page_inner == 1:
        with placeholder.container():
            st.header("Acquistion")
            st.subheader("Re-engagement")
            if st.button('back'):
                change_page_inner = 0
            row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row0_1:
                with st.form("my_form4"):
                    st.subheader("People who watched your video more than 50%")
                    image3 = Image.open('image/icon-4.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_2:
                with st.form("my_form5"):
                    st.subheader("People who watched your video more than 70%")
                    image3 = Image.open('image/icon-4.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_3:
                with st.form("my_form6"):
                    st.subheader("People who watched your video more than 90%")
                    image3 = Image.open('image/icon-4.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4

            row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row0_1:
                with st.form("my_form7"):
                    st.subheader("People who engaged with your Instagram page")
                    image3 = Image.open('image/icon-i.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_2:
                with st.form("my_form8"):
                    st.subheader("People who engaged with your Facebook page")
                    image3 = Image.open('image/icon-f.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_3:
                with st.form("my_form9"):
                    st.subheader("People who have engaged with your collection ad")
                    image3 = Image.open('image/icon-p.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4

            st.subheader("Lookalike")
            row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row0_1:
                with st.form("my_form10"):
                    st.subheader("From infrequent customers")
                    image3 = Image.open('image/icon-5.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_2:
                with st.form("my_form11"):
                    st.subheader("From occasional customers")
                    image3 = Image.open('image/icon-5.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_3:
                with st.form("my_form12"):
                    st.subheader("From frequent customers")
                    image3 = Image.open('image/icon-5.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4

            row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row0_1:
                with st.form("my_form13"):
                    st.subheader("Lookalike of people who have purchased from specific products")
                    image3 = Image.open('image/icon-p.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_2:
                with st.form("my_form14"):
                    st.subheader("Lookalike of instagram fans")
                    image3 = Image.open('image/icon-i.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_3:
                with st.form("my_form15"):
                    st.subheader("Lookalike of facebook fans")
                    image3 = Image.open('image/icon-f.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4


    if change_page_inner == 2:
        with placeholder.container():
            st.subheader("Retargeting")
            if st.button('back'):
                change_page_inner = 0
            row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row0_1:
                with st.form("my_form16"):
                    st.subheader("Lookalike of people who have purchased from specific products")
                    image3 = Image.open('image/icon-p.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_2:
                with st.form("my_form17"):
                    st.subheader("Lookalike of instagram fans")
                    image3 = Image.open('image/icon-i.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_3:
                with st.form("my_form18"):
                    st.subheader("Lookalike of facebook fans")
                    image3 = Image.open('image/icon-f.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4

            row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row0_1:
                with st.form("my_form19"):
                    st.subheader("All people who visited your website in the last 30-90 days")
                    image3 = Image.open('image/icon-6.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_2:
                with st.form("my_form20"):
                    st.subheader("People who visited the website multiple times")
                    image3 = Image.open('image/icon-6.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_3:
                with st.form("my_form21"):
                    st.subheader("People who visited the website 10+ mins")
                    image3 = Image.open('image/icon-6.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4


    if change_page_inner == 3:
        with placeholder.container():
            st.subheader("Retention")
            if st.button('back'):
                change_page_inner = 0
            row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row0_1:
                with st.form("my_form22"):
                    st.subheader("All people who made a purchase in the last 15 days")
                    image3 = Image.open('image/icon-7.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_2:
                with st.form("my_form23"):
                    st.subheader("All people who made a purchase in the last 90-180 days")
                    image3 = Image.open('image/icon-7.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4
            with row0_3:
                with st.form("my_form24"):
                    st.subheader("People who have purchased specific products")
                    image3 = Image.open('image/icon-7.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    #if submitted:
                    #    change_page_inner = 4

    """
    if change_page_inner == 4:
        with placeholder.container():
            if st.button('back'):
                change_page_inner = 0
            page_two_help()
    """
