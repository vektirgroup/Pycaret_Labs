import streamlit as st
import pandas as pd
import numpy as np



# Sidebar section ==============
st.sidebar.title('-------- Vektir Labs --------')
st.sidebar.header('Pycaret tutorial series')
st.sidebar.write('''
                 This series of labs will be based on the Pycaret python 
                 library. We assume you will have at least basic knowledge
                 of Python and have a will to learn!
                 ''')
# TODO: expander not working
with st.expander('Reference Info'):
    st.write('''test''')
    st.sidebar.markdown(' - [Pycaret Github](https://github.com/pycaret/pycaret)')
    st.sidebar.markdown('  - [Pycaret Website](https://pycaret.org/)')
    st.sidebar.markdown('  - [Moez Ali](https://github.com/moezali1?tab=overview&from=2021-11-01&to=2021-11-22)')

st.expander()
# Main image ============
st.image('../assets/PyCaret_Header.png',caption='pycaret.org')

# Main page section ============
st.header('Pycaret - Lab #1')
st.subheader('What is Pycaret')

st.write('''Well, according to the the official Pycaret Gihub account.....''')

st.write('''PyCaret is an open-source, low-code machine learning library in Python that 
         automates machine learning workflows. It is an end-to-end machine learning 
         and model management tool that speeds up the experiment cycle exponentially 
         and makes you more productive.''')

st.write('''Pycaret was created by @Moez Ali''')

# st.write('''''')
st.subheader('''Project Setup''')

# Install Python 3 
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

