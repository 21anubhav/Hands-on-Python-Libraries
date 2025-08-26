import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(120deg, #00f2fe, #4facfe, #43e97b, #38f9d7);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: black;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    </style>
    """,
    unsafe_allow_html=True
)


# 1. Charts with Random Numbers

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Line-1', 'Line-2', 'Line-3'])

st.header('1. Charts with Random Numbers')
st.subheader('1.1 Line Chart')
st.line_chart(chart_data)

st.subheader('1.2 Area Chart')
st.area_chart(chart_data)

st.subheader('1.3 Bar Chart')
st.bar_chart(chart_data)


# 2. Visualization with Matplotlib & Seaborn

st.header('2. Visualization with Matplotlib & Seaborn')
st.subheader('2.1 Upload the DataFrame')

uploaded_file = st.file_uploader("Upload your Iris dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    # 2.2 Bar Graph
    st.subheader('2.2 Bar Graph with Matplotlib')
    fig = plt.figure(figsize=(15, 8))
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    # 2.3 Distribution Plot
    st.subheader('2.3 Distribution Plot with Seaborn')
    fig = plt.figure(figsize=(15, 8))
    sns.histplot(df['sepal_length'], kde=True)  
    st.pyplot(fig)


    # 3. Multiple Graphs

    st.header('3. Multiple Graphs in One Column')
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('KDE = False')
        fig1 = plt.figure(figsize=(5, 5))
        sns.histplot(df['sepal_length'], kde=False)
        st.pyplot(fig1)

    with col2:
        st.subheader('Hist = False')
        fig2 = plt.figure(figsize=(5, 5))
        sns.kdeplot(df['sepal_length'])
        st.pyplot(fig2)

 
    # 4. Changing Style

    st.header('4. Changing Style')
    col1, col2 = st.columns(2)

    with col1:
        fig = plt.figure()
        sns.set_style('darkgrid')
        sns.set_context('notebook')
        sns.kdeplot(df['petal_length'])
        st.pyplot(fig)

    with col2:
        fig = plt.figure()
        sns.set_theme(context='poster', style='darkgrid')
        sns.kdeplot(df['petal_length'])
        st.pyplot(fig)


    # 5. Exploring Different Graphs
 
    st.header('5. Exploring Different Graphs')

    st.subheader('5.1 Scatter Plot')
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.scatter(*np.random.random(size=(2, 100)))
    st.pyplot(fig)

    st.subheader('5.2 Count Plot')
    fig = plt.figure(figsize=(15, 8))
    sns.countplot(data=df, x='species')
    st.pyplot(fig)

    st.subheader('5.3 Box Plot')
    fig = plt.figure(figsize=(15, 8))
    sns.boxplot(data=df, x='species', y='petal_length')
    st.pyplot(fig)

    st.subheader('5.4 Violin Plot')
    fig = plt.figure(figsize=(15, 8))
    sns.violinplot(data=df, x='species', y='petal_length')
    st.pyplot(fig)

else:
    st.warning("👆 Please upload the iris.csv file to continue.")
