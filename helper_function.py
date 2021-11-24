import streamlit as st
import hashlib
import sqlite3
import os
import boto3
import cv2
import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
from plotly.subplots import make_subplots


conn = sqlite3.connect("user_data.db", check_same_thread=False)
c = conn.cursor()
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
def create_usertable():
    c.execute(
        "CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT )"
    )
def add_userdata(username, password):
    c.execute(
        "INSERT INTO userstable(username,password) VALUES (?,?)",
        (username, password),
    )
    conn.commit()
@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def login_user(username, password):
    c.execute(
        "SELECT * FROM userstable WHERE username =? AND password = ?",
        (username, password),
    )
    data = c.fetchall()
    return data
def view_all_users():
    c.execute("SELECT * FROM userstable")
    data = c.fetchall()
    return data

def submit_email():
    sentence = st.text_input('Interested in us, please insert your email:')

    if st.button('Submit'):
        st.write("Done")
        my_file = open("email_log.txt")
        file_content = my_file.read()
        my_file.seek(0)

        my_file = open("email_log.txt", "w")
        my_file.write(file_content + "\n" + sentence)
        my_file.seek(0)

        my_file.close()