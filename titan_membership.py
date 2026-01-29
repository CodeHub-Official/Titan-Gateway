import streamlit as st

# إعدادات الصفحة العالمية
st.set_page_config(page_title="TITAN SYSTEM | CODE HUB", page_icon="🐜", layout="wide")

# حقن CSS "الروح والحركة" (قصير ومحير)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .main {
        background: radial-gradient(circle at center, #1a1a2e 0%, #0f0f1a 100%);
        color: #e0e0e0;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* تأثير النبض في الخلفية */
    @keyframes pulse {
        0% { box-shadow: 0 0 10px #ff0055; }
        50% { box-shadow: 0 0 30px #00ffcc; }
        100% { box-shadow: 0 0 10px #ff0055; }
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #ff0055, #00ffcc);
        color: white;
        border: none;
        border-radius: 5px;
        transition: 0.3s;
        animation: pulse 3s infinite;
    }
    
    .stButton>button:hover {
        transform: scale(1.1);
        color: #000;
    }
    
    .title-text {
        text-align: center;
        background: -webkit-linear-gradient(#00ffcc, #ff0055);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# نظام اللغات (اللغة اللي تحير)
lang = st.sidebar.selectbox("🌐 Select Language / اختر اللغة", ["English", "العربية", "Français", "中文"])

translations = {
    "English": {"welcome": "TITAN CORE ACTIVATED", "ants": "Ant Army Pulse", "status": "Global Connection: Secured"},
    "العربية": {"welcome": "تم تفعيل قلب تايتان", "ants": "نبض جيوش النمل", "status": "الاتصال العالمي: مؤمن"},
    "Français": {"welcome": "CŒUR TITAN ACTIVÉ", "ants": "Pouls des Fourmis", "status": "Connexion Mondiale: Sécurisée"},
    "中文": {"welcome": "泰坦核心已激活", "ants": "蚁群脉冲", "status": "全球连接：已确认"}
}

t = translations[lang]

# محتوى الصفحة "المبهر"
st.markdown(f'<p class="title-text">{t["welcome"]}</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label=t["ants"], value="7,432 RPM", delta="+124")
with col2:
    st.metric(label="Global Keys", value="1.2M", delta="Active")
with col3:
    st.metric(label="System Security", value="99.9%", delta="Solid")

st.markdown("---")

# منطقة "الحركة والروح"
st.write(f"### {t['status']}")
if st.button("Activate Deep Scan | تفعيل الفحص العميق"):
    st.balloons()
    st.success("Scanning the grid... Your Empire is expanding.")

st.info("Titan System is now running in 'Global Mode'. Every pixel is a soldier.")
