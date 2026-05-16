import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Executive Layout Configuration
st.set_page_config(
    page_title="Nepal Gov Analytics Platform", 
    page_icon="🦅", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling Sheets
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .main-title { font-size:38px !important; font-weight: 800 !important; color: #1E3A8A; letter-spacing: -0.5px; margin-bottom: 2px; }
    .sub-title { font-size:15px !important; color: #4B5563; margin-bottom: 25px; }
    
    .kpi-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        text-align: left;
    }
    .kpi-label { font-size: 13px; font-weight: 600; color: #6B7280; text-transform: uppercase; letter-spacing: 0.5px; }
    .kpi-value { font-size: 28px; font-weight: 700; color: #111827; margin-top: 5px; }
    
    .status-badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 600;
        background-color: #E0F2FE;
        color: #0369A1;
        margin-bottom: 15px;
    }
    .status-dot { width: 8px; height: 8px; background-color: #0EA5E9; border-radius: 50%; margin-right: 6px; display: inline-block; }
    </style>
""", unsafe_allow_html=True)

# 2. Header
st.markdown('<div class="status-badge"><span class="status-dot"></span>DATA VOLUME SCALE: 5K BIG-DATA LEVEL</div>', unsafe_allow_html=True)
st.markdown('<p class="main-title">🦅 NEPAL GOVERNMENT SENTIMENT RADAR</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">High-Volume NLP Feed Ledger Tracking Aggregated Public Opinion & News Indexes</p>', unsafe_allow_html=True)
st.divider()

# 3. Load Dataset
df = pd.read_csv("nepal_gov_processed_sentiment.csv")

# 4. Control Sidebar Panel
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/2/23/Emblem_of_Nepal.svg", width=85)

st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%); padding: 20px; border-radius: 14px; border: 1px solid #E2E8F0; margin-top: 15px; margin-bottom: 25px;">
        <span style="font-size: 10px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: 2px;">Lead Architect</span>
        <h2 style="font-size: 21px; font-weight: 800; color: #0F172A; margin: 0 0 4px 0; letter-spacing: -0.5px;">Prem Narayan Bashyal</h2>
        <p style="font-size: 12px; color: #64748B; margin: 0; font-weight: 500;">💼 Data Platform Engineering</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ Control Panel")
platform_filter = st.sidebar.multiselect("Filter Social Channels:", options=df["Platform"].unique(), default=df["Platform"].unique())
sentiment_filter = st.sidebar.multiselect("Filter Sentiment Metrics:", options=df["Sentiment"].unique(), default=df["Sentiment"].unique())

filtered_df = df[(df["Platform"].isin(platform_filter)) & (df["Sentiment"].isin(sentiment_filter))]

# 5. Core KPI Metrics Scoreboard
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
total_count = len(filtered_df)
pos_count = len(filtered_df[filtered_df["Sentiment"] == "POSITIVE"])
neg_count = len(filtered_df[filtered_df["Sentiment"] == "NEGATIVE"])
neu_count = len(filtered_df[filtered_df["Sentiment"] == "NEUTRAL"])

with m_col1:
    st.markdown(f'<div class="kpi-card"><div class="kpi-label">Audited Volume</div><div class="kpi-value">{total_count:,}</div></div>', unsafe_allow_html=True)
with m_col2:
    st.markdown(f'<div class="kpi-card" style="border-left: 4px solid #10B981;"><div class="kpi-label" style="color: #10B981;">Positive Feedback</div><div class="kpi-value">{pos_count:,}</div></div>', unsafe_allow_html=True)
with m_col3:
    st.markdown(f'<div class="kpi-card" style="border-left: 4px solid #EF4444;"><div class="kpi-label" style="color: #EF4444;">Negative Outcry</div><div class="kpi-value">{neg_count:,}</div></div>', unsafe_allow_html=True)
with m_col4:
    st.markdown(f'<div class="kpi-card" style="border-left: 4px solid #F59E0B;"><div class="kpi-label" style="color: #F59E0B;">Neutral Stance</div><div class="kpi-value">{neu_count:,}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Analytics Suite Charts
chart_col1, chart_col2 = st.columns([4, 6])
color_palette = {"POSITIVE": "#10B981", "NEGATIVE": "#EF4444", "NEUTRAL": "#F59E0B"}

with chart_col1:
    st.markdown("#### 📊 Metric Share Allocations")
    sentiment_summary = filtered_df["Sentiment"].value_counts().reset_index()
    sentiment_summary.columns = ["Sentiment", "Count"]
    fig_donut = go.Figure(data=[go.Pie(labels=sentiment_summary["Sentiment"], values=sentiment_summary["Count"], hole=.5, marker=dict(colors=[color_palette[x] for x in sentiment_summary["Sentiment"]]))])
    fig_donut.update_layout(margin=dict(t=20, b=20, l=10, r=10), showlegend=True, height=320, legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5))
    st.plotly_chart(fig_donut, use_container_width=True)

with chart_col2:
    st.markdown("#### 📱 Channel Stance Densities")
    fig_bar = px.histogram(filtered_df, x="Platform", color="Sentiment", color_discrete_map=color_palette, barmode="group")
    fig_bar.update_layout(margin=dict(t=20, b=20, l=10, r=10), height=320, xaxis_title="", yaxis_title="Record Count", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# 7. High-Volume Data Ledger Table
st.markdown("#### 📋 Real-time Audited Feed Ledger (Showing Latest Channels First)")
st.dataframe(
    filtered_df[["Timestamp", "Platform", "User", "Post_Text", "Sentiment"]].sort_values(by="Timestamp", ascending=False),
    use_container_width=True,
    hide_index=True
)
