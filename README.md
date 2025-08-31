# 🌱 EcoRoute AI

EcoRoute AI is a **smart city mobility project** built during the Gen AI Chakra 4 Hackathon.  
It helps commuters and city planners in **Visakhapatnam** find eco-friendly, low-emission routes.

---

## 🚀 Features
- Compare fastest vs eco-friendly routes.
- Estimate CO₂ footprint of trips.
- Integrate weather conditions for routing.
- City planner dashboard for emissions & mobility trends.
- Built with free APIs (OSRM, OpenWeather).

---

## 🛠 Tech Stack
- **Frontend**: Streamlit (Streamlit Cloud Hosting)
- **Routing**: OSRM (OpenStreetMap)
- **Weather**: OpenWeather API (free tier)
- **AI/NLP**: OpenAI / Hugging Face (for queries & analysis)
- **Database**: Supabase / Neon PostgreSQL
- **Extras**: LangChain for reasoning, Geopy for geocoding

---

## ▶️ Run Locally
```bash
git clone https://github.com/yourusername/ecoroute_ai.git
cd ecoroute_ai
pip install -r requirements.txt
streamlit run app.py
