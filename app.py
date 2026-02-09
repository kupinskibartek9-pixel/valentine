import streamlit as st

# --- 1. Konfiguracja strony ---
st.set_page_config(
    page_title="Special Question 💜",
    page_icon="✨",
    layout="wide"
)

# --- 2. CSS - ULTRA LUXURY ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');

header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display:none;}

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

.block-container {
    padding-top: 5vh !important;
    max-width: 850px !important;
}

/* PRZYCISKI */
.stButton > button {
    border-radius: 50px !important;
    padding: 20px 40px !important;
    font-weight: 600 !important;
    letter-spacing: 2px !important;
    border: none !important;
    width: 100% !important;
}

/* TEKST PRZYCISKÓW */
.stButton > button p {
    color: white !important;
}

/* TAK – PULSUJE */
div[data-testid="stHorizontalBlock"] div:nth-of-type(1) .stButton button {
    background: linear-gradient(45deg, #6A1B9A, #9C27B0) !important;
    box-shadow: 0 10px 25px rgba(123, 31, 162, 0.4) !important;
    animation: pulseYes 2s infinite;
}

@keyframes pulseYes {
    0% { transform: scale(1); }
    50% { transform: scale(1.08); }
    100% { transform: scale(1); }
}

/* NIE – STATYCZNY */
div[data-testid="stHorizontalBlock"] div:nth-of-type(2) .stButton button {
    background: rgba(74, 20, 140, 0.7) !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
    animation: none !important;
    transform: none !important;
}
</style>
""", unsafe_allow_html=True)

# --- 3. STAN APLIKACJI ---
if "step" not in st.session_state:
    st.session_state.step = 0

if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "show_error" not in st.session_state:
    st.session_state.show_error = False

# PYTANIA (ZMIENIAJĄ SIĘ)
questions = [
    "Czy zostaniesz moją Walentynką? 💜",
    "Jesteś pewna? 😢",
    "Pomyśl jeszcze raz... 🧐",
    "Może jednak TAK? ✨",
    "Nie masz wyboru hihi 😈"
]

# --- 4. RENDER ---
if not st.session_state.accepted:
    st.markdown('<h1 class="title-text">Hej Kochanie... ✨💜</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #4A148C; font-size: 1.1rem;">Przygotowałem dla Ciebie coś specjalnego.</p>', unsafe_allow_html=True)
    st.markdown('<hr style="border: 0.5px solid rgba(255,255,255,0.3); margin: 30px 0;">', unsafe_allow_html=True)
    current_question = questions[st.session_state.step]
    st.markdown(f'<h2 style="color: #311B92; margin-bottom: 45px; font-weight: 600;">{current_question}</h2>', unsafe_allow_html=True)



    col1, col2 = st.columns(2, gap="large")

    with col1:
        if st.button("TAK 😍"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        if st.button("NIE 😈"):
            if st.session_state.step >= len(questions) - 1:
                st.session_state.show_error = True
            else:
                st.session_state.step += 1
            st.rerun()

    if st.session_state.show_error:
        st.error("BŁĄD MIŁOSCIOWY: Wybrana opcja wygasła lub nigdy nie istniała! Proszę natychmiast kliknąć przycisk po lewej stronie. ⚠️😈")
        st.warning("System wykrył próbę oszustwa! Odpowiedź 'TAK' jest jedyną poprawną w Twoim przypadku")


else:
    # --- SUKCES ---
    st.balloons()
    st.markdown('<h1 style="color:#6A1B9A;">Jeeeej! 💜</h1>', unsafe_allow_html=True)
    st.markdown('<h2>Wiedziałem 🥰</h2>', unsafe_allow_html=True)
    st.markdown('<h3>Kocham Cię najbardziej na świecie 🌹</h3>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://cataas.com/cat/says/Love", use_container_width=True)
    with col_b:
        st.image("https://cataas.com/cat/cute", use_container_width=True)
st.markdown('<br><h3 style="color: #311B92; font-family: Playfair Display, serif; font-size: 2rem;">Do zobaczenia na naszej randce! 🌹</h3>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

