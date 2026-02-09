import streamlit as st

# --- 1. Konfiguracja strony ---
st.set_page_config(page_title="Special Question 💜", page_icon="✨", layout="wide")

# --- 2. CSS - ULTRA LUXURY & FIXES ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');

/* CAŁKOWITE UKRYCIE GÓRNEGO PASKA STREAMLIT */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display:none;}

/* TŁO */
.stApp {
    background: linear-gradient(-45deg, #f3e5f5, #e1bee7, #d1c4e9, #f3e5f5);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    font-family: 'Poppins', sans-serif;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* KONTENER */
.block-container {
    padding-top: 5vh !important;
    max-width: 850px !important;
}

/* PRZYCISKI – BAZA */
.stButton > button {
    border-radius: 50px !important;
    padding: 20px 40px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    border: none !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    width: 100% !important;
}

/* WYMUSZENIE BIAŁEGO TEKSTU */
.stButton > button p {
    color: white !important;
    margin-bottom: 0 !important;
}

/* PRZYCISK TAK – PULSUJE */
div[data-testid="stHorizontalBlock"] div:nth-of-type(1) .stButton button {
    background: linear-gradient(45deg, #6A1B9A, #9C27B0) !important;
    box-shadow: 0 10px 25px rgba(123, 31, 162, 0.4) !important;
    animation: pulseOnlyYes 2s infinite;
}

@keyframes pulseOnlyYes {
    0% { transform: scale(1); box-shadow: 0 10px 25px rgba(123, 31, 162, 0.4); }
    50% { transform: scale(1.08); box-shadow: 0 15px 35px rgba(123, 31, 162, 0.6); }
    100% { transform: scale(1); box-shadow: 0 10px 25px rgba(123, 31, 162, 0.4); }
}

/* PRZYCISK NIE – STATYCZNY */
div[data-testid="stHorizontalBlock"] div:nth-of-type(2) .stButton button {
    background: rgba(74, 20, 140, 0.7) !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
}

/* 🔒 TWARDY BLOK: NIE NIGDY NIE PULSUJE */
div[data-testid="stHorizontalBlock"] div:nth-of-type(2) .stButton button {
    animation: none !important;
    transform: none !important;
}

/* GALERIA */
div[data-testid="stImage"] img {
    height: 380px !important;
    object-fit: cover !important;
    border-radius: 35px;
    border: 10px solid white;
    box-shadow: 0 25px 45px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# --- 3. Logika ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False
if 'show_error' not in st.session_state:
    st.session_state.show_error = False

no_options = [
    "Nie... 😢",
    "Pomyśl jeszcze raz... 🧐",
    "Jesteś pewna? 💔",
    "Może jednak TAK? ✨",
    "Nie masz wyboru 😈"
]

# --- 4. Render ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

if not st.session_state.accepted:
    st.markdown('<h1>Hej Kochanie... ✨</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#4A148C;">Przygotowałem dla Ciebie coś specjalnego.</p>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<h2 style="color:#311B92;">Czy zostaniesz moją Walentynką?</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        if st.button("TAK! 😍"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        label = no_options[min(st.session_state.step, len(no_options)-1)]
        if st.button(label):
            if label == "Nie masz wyboru 😈":
                st.session_state.show_error = True
            else:
                st.session_state.step += 1
            st.rerun()

    if st.session_state.show_error:
        st.error("BŁĄD 404: Jedyna poprawna odpowiedź to TAK 😈")

else:
    st.balloons()
    st.markdown('<h1>Jeeej! 💜</h1>', unsafe_allow_html=True)
    st.markdown('<h2>Wiedziałem! 🥰</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cataas.com/cat/says/Love", use_container_width=True)
    with col2:
        st.image("https://cataas.com/cat/cute", use_container_width=True)

    st.markdown('<h3>Do zobaczenia na randce 🌹</h3>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
