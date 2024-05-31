import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Hello, Dirham rev! 👋')
st.title('This is my first streamlit app')
uploaded_file = st.file_uploader("Choose a file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Preview dataset", data.head())

    chart_type = st.selectbox("Select Chart Type", ["Histogram", "Scatter", "Line"])

    column_names = data.columns.tolist()

    x_axis = st.selectbox("X Axis", column_names)
    y_axis = None

    if chart_type != "Histogram":
        y_axis = st.selectbox("Y Axis", column_names)

    if chart_type == "Histogram":
        plt.figure()
        plt.hist(data[x_axis].dropna(), bins=10)
        plt.title(f"Histogram of {x_axis}")
        plt.xlabel(x_axis)
        plt.ylabel("Frequency")
        st.pyplot(plt.gcf())

    elif chart_type == "Scatter":
        plt.figure()
        plt.scatter(data[x_axis].dropna(), data[y_axis].dropna())
        plt.title(f"Scatter plot of {x_axis} vs {y_axis}")
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        st.pyplot(plt.gcf())
    
    elif chart_type == "Line":
        plt.figure()
        plt.plot(data[x_axis].dropna(), data[y_axis].dropna())
        plt.title(f"Line plot of {x_axis} vs {y_axis}")
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        st.pyplot(plt.gcf())

else:
    st.write("No file uploaded")