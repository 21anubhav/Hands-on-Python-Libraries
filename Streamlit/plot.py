import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

# -------------------------------
# 1. Altair Scatter Plot
# -------------------------------
st.header('1. Altair Scatter Plot')

chart_data = pd.DataFrame(np.random.randn(500, 5), columns=['a', 'b', 'c', 'd', 'e'])
chart = alt.Chart(chart_data).mark_circle().encode(
    x='a',
    y='b',
    size='c',
    tooltip=['a', 'b', 'c', 'd', 'e']
)
st.altair_chart(chart, use_container_width=True)

# -------------------------------
# 2. Interactive Charts
# -------------------------------
st.header('2. Interactive Charts')

st.subheader('2.1 Line Chart (Upload your lang_data.csv)')
uploaded_lang = st.file_uploader("Upload lang_data.csv", type=["csv"])

if uploaded_lang is not None:
    df_lang = pd.read_csv(uploaded_lang)
    st.dataframe(df_lang.head())

    lang_list = df_lang.columns.tolist()
    lang_choices = st.multiselect('Choose your language', lang_list)

    if lang_choices:
        new_df = df_lang[lang_choices]
        st.line_chart(new_df)
        st.subheader('2.2 Area Chart')
        st.area_chart(new_df)
    else:
        st.info("👆 Please select at least one column to plot.")

# -------------------------------
# 3. Data Visualisation with Plotly
# -------------------------------
st.header('3. Data Visualisation with Plotly')

st.subheader('3.1 Displaying the dataset (Upload tips.csv)')
uploaded_tips = st.file_uploader("Upload tips.csv", type=["csv"])

if uploaded_tips is not None:
    df_tips = pd.read_csv(uploaded_tips)
    st.dataframe(df_tips.head())

    st.subheader('3.2 Pie Chart')
    fig = px.pie(df_tips, values='total_bill', names='day')
    st.plotly_chart(fig)

    st.subheader('3.3 Pie Chart with Multiple Parameters')
    fig = px.pie(df_tips,
                 values='total_bill',
                 names='day',
                 opacity=0.7,
                 color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

    st.subheader('3.4 Histogram (Distribution Plot)')
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    hist_data = [x1, x2, x3]
    group_labels = ['Group - 1', 'Group - 2', 'Group - 3']
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
    st.plotly_chart(fig)

else:
    st.warning("👆 Please upload tips.csv to see Plotly visualizations.")
