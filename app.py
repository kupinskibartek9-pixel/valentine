import streamlit as st

# --- 1. Konfiguracja strony ---
st.set_page_config(page_title="Dla mojej Walentynki 💜", page_icon="✨", layout="centered")

# --- 2. CSS - FULL PRO LOOK & FIXES ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    /* 1. USUNIĘCIE BIAŁEGO PASKA I ELEMENTÓW SYSTEMOWYCH */
    [data-testid="stHeader"] {display: none;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* TŁO CAŁEJ APKI */
    .stApp {
        background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
        font-family: 'Poppins', sans-serif;
    }

    /* 2. GŁÓWNY PROSTOKĄT (KARTA) Z CIENIEM */
    .main-card {
        background: white;
        padding: 60px;
        border-radius: 40px;
        box-shadow: 0 30px 60px rgba(0,0,0,0.15);
        text-align: center;
        border: 2px solid rgba(255, 255, 255, 0.5);
        margin-top: 50px;
    }

    /* NAGŁÓWKI */
    h1 {
        color: #4A148C !important;
        font-weight: 800 !important;
        font-size: 3.5rem !important;
        margin-bottom: 10px !important;
    }
    h2 {
        color: #6A1B9A !important;
        font-weight: 600 !important;
        margin-bottom: 40px !important;
    }

    /* 3. PRZYCISKI - DUŻE, FIOLETOWE, BIAŁA CZCIONKA */
    .stButton > button {
        height: 85px !important;
        border-radius: 25px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }

    /* WYMUSZENIE BIAŁEGO TEKSTU W ŚRODKU PRZYCISKU */
    .stButton > button p {
        color: white !important;
        font-size: 24px !important;
        font-weight: 800 !important;
    }

    /* PRZYCISK TAK - PULSUJĄCY GRADIENT */
    div[data-testid="column"]:nth-of-type(1) .stButton button {
        background: linear-gradient(45deg, #7B1FA2, #9C27B0) !important;
        box-shadow: 0 15px 30px rgba(123, 31, 162, 0.4) !important;
        animation: pulseYes 1.8s infinite !important;
    }

    @keyframes pulseYes {
        0% { transform: scale(1); box-shadow: 0 15px 30px rgba(123, 31, 162, 0.4); }
        50% { transform: scale(1.08); box-shadow: 0 20px 40px rgba(123, 31, 162, 0.6); }
        100% { transform: scale(1); box-shadow: 0 15px 30px rgba(123, 31, 162, 0.4); }
    }

    /* PRZYCISK NIE - STATYCZNY, CIEMNIEJSZY */
    div[data-testid="column"]:nth-of-type(2) .stButton button {
        background: #4A148C !important;
        animation: none !important;
        transform: none !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
    }

    /* ZDJĘCIA - PRO LOOK */
    div[data-testid="stImage"] img {
        height: 350px !important;
        object-fit: cover !important;
        border-radius: 30px;
        border: 8px solid white;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- 3. Logika (State) ---
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

# --- 4. Renderowanie ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)

if not st.session_state.accepted:
    # EKRAN PYTANIA
    st.markdown('<h1>Hej Kochanie... ✨💜</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#7B1FA2; font-size: 1.2rem;">Mam do Ciebie bardzo ważne pytanie.</p>', unsafe_allow_html=True)
    st.markdown('<hr style="border: 0.5px solid #eee; margin: 30px 0;">', unsafe_allow_html=True)
    st.markdown('<h2>Czy zostaniesz moją Walentynką?</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        if st.button("TAK! 😍", key="yes"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        label = no_options[min(st.session_state.step, len(no_options)-1)]
        if st.button(label, key="no"):
            if label == "Nie masz wyboru 😈":
                st.session_state.show_error = True
            else:
                st.session_state.step += 1
            st.rerun()

    if st.session_state.show_error:
        st.markdown("<br>", unsafe_allow_html=True)
        st.error("⚠️ BŁĄD SYSTEMU: Ta odpowiedź jest zablokowana. Musisz wybrać TAK! 😈")

else:
    # EKRAN SUKCESU (ZDJĘCIA)
    st.balloons()
    st.markdown('<h1>Jeeej! 💜</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="margin-bottom: 10px;">Wiedziałem, że się zgodzisz!! 🥰</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#4A148C; font-weight: 600;">To będzie najpiękniejszy dzień!</p>', unsafe_allow_html=True)
    st.markdown('<hr style="border: 0.5px solid #eee; margin: 30px 0;">', unsafe_allow_html=True)

    col_img1, col_img2 = st.columns(2, gap="medium")
    with col_img1:
        st.image("https://cataas.com/cat/says/Love", use_container_width=True)
    with col_img2:
        st.image("https://cataas.com/cat/cute", use_container_width=True)

    st.markdown('<br><h2 style="color:#311B92; font-size: 2.5rem;">Do zobaczenia na randce! 🌹</h2>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
