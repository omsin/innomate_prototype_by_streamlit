import streamlit as st
from PIL import Image


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
