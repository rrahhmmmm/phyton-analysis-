import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("survey_data.csv")

st.title("Audience Preference Survey")
st.markdown("Explore viewer habits from survey data.")


age_min, age_max = int(df['age'].min()), int(df['age'].max())
age_range = st.slider("Filter by Age", age_min, age_max, (age_min, age_max))
filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]


genre_counts = filtered_df['favorite_genre'].value_counts().reset_index()
genre_counts.columns = ['genre', 'count']  # rename agar lebih jelas

fig_genre = px.bar(genre_counts, x='genre', y='count',
                   labels={'genre': 'Genre', 'count': 'Count'},
                   color='count',
                   title="Genre Preference")

st.subheader("📺 Preferred Platforms 📺")
platform_counts = filtered_df['platform'].value_counts().reset_index()
platform_counts.columns = ['platform_name', 'count']
fig_platform = px.pie(platform_counts, values='count', names='platform_name',
                      title='Platform Distribution')
st.plotly_chart(fig_platform)


watch_time_counts = filtered_df['watch_time'].value_counts().reset_index()
watch_time_counts.columns = ['watch_time_range', 'count']
watch_time_counts['count'] = pd.to_numeric(watch_time_counts['count'], errors='coerce')

fig_watch_time = px.bar(watch_time_counts, x='watch_time_range', y='count',
                           labels={'watch_time_range': 'Watch Time Range', 'count': 'Count'},
                           title="Watch Time Distribution")
st.plotly_chart(fig_watch_time)


if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)

# streamlit run app.py
