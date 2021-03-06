import streamlit as st
import pandas as pd
import numpy as np

# Page Config ==============
st.set_page_config(
    page_title=None, 
    page_icon=None, 
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     })

# Sidebar section ==============
st.sidebar.title('Vektir Labs')
st.sidebar.header('Pycaret Tutorial Series - Lab #1')
st.sidebar.write('''
                 This series of labs will be based on the Pycaret python 
                 library. We assume you will have at least basic knowledge
                 of Python and have a will to learn!
                 ''')
with st.sidebar.expander('Reference Links'):
    st.markdown(' - [Pycaret Github](https://github.com/pycaret/pycaret)')
    st.markdown('  - [Pycaret Website](https://pycaret.org/)')
    st.markdown('  - [Moez Ali](https://github.com/moezali1?tab=overview&from=2021-11-01&to=2021-11-22)')

# Main image ============
st.image('../assets/PyCaret_Header.png',caption='pycaret.org')

# Main page ============
st.header('Pycaret - Lab #1')

# Intro ============
st.subheader('What is Pycaret')
st.write('''Well, according to the the official Pycaret Gihub account.....''')
st.write('''PyCaret is an open-source, low-code machine learning library in Python that 
         automates machine learning workflows. It is an end-to-end machine learning 
         and model management tool that speeds up the experiment cycle exponentially 
         and makes you more productive.''')
st.write('''Pycaret was created by @Moez Ali''')
st.write('')

# Install Python 3 
st.subheader('''Project Setup''')
st.markdown('''
         I am going to assume that you have not installed the necessary tools install yet, so I will 
         share the tools/processes I use to get up and running as quickly as possible!
         
         **Step 1** - Download and install Python 3, Click here -> [Python.org](https://www.python.org/downloads/)
         ''')
st.image('../assets/pythonorg.png')
st.markdown('''**Note:** Make sure you install the latest stable build of Python''')

# Check Python 3 install 
st.markdown('''
         **Step 2** - Once you've installed Python 3, open a (Mac) termianl window or a (Windows) CMD prompt and
         type 'python3 --version'
         ''')
st.image('../assets/Terminal.png',caption="Python 3.x installed correctly")
st.markdown('''**Note:** If you receive an error message in the terminal or CMD prompt
            when running 'python3 --version' then consult the python install guide 
            [here](https://www.python.org/search/?q=install&submit=)''')


# Install VS Code
st.markdown('''
         **Step 3** - Install VS Code, Click here -> [VS Code](https://code.visualstudio.com/)
         
         Also, make sure you install the required VS Code Python plugin 
         ''')
st.image('../assets/VS Code.png')
st.markdown('''**Note:** You can chose any editor you like/prefer!''')

# Set up Project
st.markdown('''
         **Step 4** - Open VS Code 
         ''')

st.code('pip install pycaret[full]', language="python")

