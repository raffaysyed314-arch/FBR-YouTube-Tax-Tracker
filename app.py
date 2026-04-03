import streamlit as st
import pandas as pd
import plotly.express as px
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# 1. Setup API
load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')
MY_CHANNEL_ID = "UCa2k8KIWi2avL6EHA4X_djg"

# Using a Cache to save your API quota (The Professional Way)
@st.cache_data(ttl=3600)
def get_youtube_data(channel_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.channels().list(part='statistics,snippet', id=channel_id)
    response = request.execute()
    item = response['items'][0]
    return {
        "name": item['snippet']['title'],
        "views": int(item['statistics']['viewCount']),
        "subs": int(item['statistics']['subscriberCount'])
    }

# 2. UI Layout
st.set_page_config(page_title="Margin Brief: Tax Intel", layout="wide")
st.title("📈 Margin Brief: YouTube FBR Compliance")

with st.spinner("Fetching latest data from YouTube..."):
    data = get_youtube_data(MY_CHANNEL_ID)

if data:
    # 3. FBR Math (April 2026 Rules)
    assessed_rev = (data['views'] / 1000) * 195
    taxable_inc = assessed_rev * 0.70 

    # Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Current Views", f"{data['views']:,}")
    m2.metric("Assessed Revenue", f"PKR {assessed_rev:,.0f}")
    m3.metric("Taxable Income", f"PKR {taxable_inc:,.0f}")

    # 4. Growth Prediction Chart
    st.subheader("Future Tax Projection")
    # Using a container to prevent layout shifts
    with st.container():
        growth_rate = st.slider("Select Monthly View Growth (%)", 1, 100, 15) / 100

        months = list(range(13))
        projected_views = [data['views'] * (1 + growth_rate)**m for m in months]
        projected_taxable = [(v / 1000) * 195 * 0.70 for v in projected_views]

        df = pd.DataFrame({"Month": months, "Taxable Income": projected_taxable})

        fig = px.line(df, x="Month", y="Taxable Income", title="Growth Simulation")
        fig.add_hline(y=600000, line_dash="dash", line_color="red", annotation_text="Taxable Limit (600k)")
        st.plotly_chart(fig, use_container_width=True) # Fixed Warning

    # 5. Final Verdict
    if taxable_inc < 600000:
        st.success(f"Channel: {data['name']} is currently below the 600k threshold.")
    else:
        tax_due = (taxable_inc - 600000) * 0.01
        st.error(f"Estimated Annual Tax: PKR {tax_due:,.0f}")
