import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("Technology_Advancements_India_2019_2024.csv")

st.title(" Technology Advancements in India (2019-2024)")
st.markdown("This dashboard visualizes sector-wise technology implementation, adoption percentage, and investment.")

with st.expander(" Show Dataset"):
    st.dataframe(df)


st.sidebar.header(" Filter Options")
years = st.sidebar.multiselect("Select Year(s):", sorted(df['Year'].unique()), default=sorted(df['Year'].unique()))
sectors = st.sidebar.multiselect("Select Sector(s):", df['Sector'].unique(), default=df['Sector'].unique())


filtered_df = df[(df['Year'].isin(years)) & (df['Sector'].isin(sectors))]


metric = st.sidebar.selectbox(
    " Select Metric to Visualize:",
    ["Estimated_Adoption(%)", "Investment_in_Cr(INR)"]
)


chart_type = st.selectbox(" Select Chart Type:", ["Bar Chart", "Line Chart", "Pie Chart", "Area Chart", "Scatter Plot"])


st.subheader(f"{chart_type} of {metric} by Sector and Year")


if chart_type == "Bar Chart":
    fig = px.bar(filtered_df, x="Sector", y=metric, color="Year", barmode="group", hover_data=["Technology_Implemented"])
elif chart_type == "Line Chart":
    fig = px.line(filtered_df, x="Year", y=metric, color="Sector", markers=True, hover_data=["Technology_Implemented"])
elif chart_type == "Pie Chart":
    pie_df = filtered_df.groupby("Sector")[metric].sum().reset_index()
    fig = px.pie(pie_df, names="Sector", values=metric)
elif chart_type == "Area Chart":
    fig = px.area(filtered_df, x="Year", y=metric, color="Sector")
elif chart_type == "Scatter Plot":
    fig = px.scatter(filtered_df, x="Year", y=metric, color="Sector", size=metric, hover_data=["Technology_Implemented"])


st.plotly_chart(fig, use_container_width=True)
