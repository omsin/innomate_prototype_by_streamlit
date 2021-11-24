from helper_function import *
from page4_helper import *

def page_four():

    change_page_inner = 0

    st.title("Automation Strategies")

    placeholder = st.empty()

    if change_page_inner == 0:
        with placeholder.container():
            row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3, row0_3, row0_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row0_1:
                with st.form("my_form1"):
                    st.subheader("Long-Term Budget Optimization")
                    image3 = Image.open('image/icon-s.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1
            with row0_2:
                with st.form("my_form2"):
                    st.subheader("Maximize Conversions")
                    image3 = Image.open('image/icon-s.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1
            with row0_3:
                with st.form("my_form3"):
                    st.subheader("Enhanced Cost Per Click")
                    image3 = Image.open('image/icon-s.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1

            row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3, row1_3, row1_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row1_1:
                with st.form("my_form4"):
                    st.subheader("Penalize Low-Performing Campaigns")
                    image3 = Image.open('image/icon-s.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1
            with row1_2:
                with st.form("my_form5"):
                    st.subheader("Target Cost Per Acquisition")
                    image3 = Image.open('image/icon-s.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1
            with row1_3:
                with st.form("my_form6"):
                    st.subheader("Target Return on Ad Spend")
                    image3 = Image.open('image/icon-s.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1

            row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3, row2_3, row2_spacer4 = \
                st.columns((.1, 2, .1, 2, .1, 2, .1))
            with row2_1:
                with st.form("my_form7"):
                    st.subheader("Maximize Conversion Value")
                    image3 = Image.open('image/icon-s.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1
            with row2_2:
                with st.form("my_form8"):
                    st.subheader("Maximize Daily Campaign Profits")
                    image3 = Image.open('image/icon-s.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1
            with row2_3:
                with st.form("my_form9"):
                    st.subheader("Create by your own")
                    image3 = Image.open('image/icon-s.jpg')
                    st.image(image3, width=220)
                    submitted = st.form_submit_button("select")
                    if submitted:
                        change_page_inner = 1



    if change_page_inner == 1:
        with placeholder.empty():
            if st.button('back'):
                change_page_inner = 0
        page_four_help()


