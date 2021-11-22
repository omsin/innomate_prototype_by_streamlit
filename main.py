from helper_function import *
from page1 import *
from page2 import *
from page3 import *
from page4 import *
from home import *

logo = Image.open('image/AWS_TL.png')
st.set_page_config(
    page_title='Innomate',
    page_icon=logo,
    initial_sidebar_state="expanded",
    layout = "wide"
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 200px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 200px;
        margin-left: -200px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image(
    "image/Innomate_Logo.png",
    width=160,
)

menu = ["Home", "Log In", "Sign Up"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    home_page()



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


            option = st.selectbox(
                "Select the services:",
                ('Dashboard', 'Ads Creation', 'Design Analytics', 'Automation Strategies'))

            if option == 'Dashboard':
                page_one()

            elif option == 'Ads Creation':
                page_two()

            elif option == 'Design Analytics':
                page_three()

            else:
                page_four()


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