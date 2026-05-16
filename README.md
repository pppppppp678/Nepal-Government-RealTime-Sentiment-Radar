# Nepal-Government-RealTime-Sentiment-Radar
# 🦅 Nepal Government Real-Time Sentiment Radar

A production-ready data engineering platform that ingests real-time public news indexes and media streams regarding governance in Nepal, processes them through an analytical NLP rules layer, and serves data via an interactive dashboard.


nepal-gov-sentiment-radar/
│
├── .github/workflows/       # (Optional) For future CI/CD automated test runs
├── data/
│   └── nepal_gov_processed_sentiment.csv  # Sample cached dataset batch
│
├── app.py                   # Streamlit interface application layer
├── pipeline.py              # Google News RSS Live collection & ingestion engine
├── requirements.txt         # Package dependency blueprint
└── README.md                # The master project presentation document


## 🛠️ Architecture & Tech Stack
- **Data Ingestion:** Real-time stream parsing via Google News RSS Feed API.
- **Processing Layer:** Vectorized text sorting and classification using Pandas NLP engines.
- **Serving Layer:** High-fidelity monitoring dashboard engineered with Streamlit and Plotly Express.
- **Infrastructure:** Local development tunneled via secure Ngrok proxy architectures.

## 🚀 Deployment Instructions
1. Clone the platform repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/nepal-gov-sentiment-radar.git](https://github.com/YOUR_USERNAME/nepal-gov-sentiment-radar.git)
