import streamlit as st

# --- 1. Konfiguracja strony ---
st.set_page_config(page_title="Special Question 💜", page_icon="✨", layout="wide")

# --- 2. CSS - ULTRA LUXURY & FIXES ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');

/* UKRYCIE STREAMLIT UI */
header, footer, #MainMenu {display:none;}
.stDeployButton {display:none;}

/* 🌌 TŁO – PRO, GŁĘBOKIE, PREMIUM */
.stApp {
    background:
        radial-gradient(circle at top left, #b388ff 0%, transparent 40%),
        radial-gradient(circle at bottom right, #7b1fa2 0%, transparent 45%),
        linear-gradient(135deg, #2a003f 0%, #4a148c 45%, #6a1b9a 100%);
    font-family: 'Poppins', sans-serif;
}

/* WYŚRODKOWANIE */
.block-container {
    padding-top: 8vh !important;
    max-width: 900px !important;
}

/* 🟣 GŁÓWNA KARTA – SERCE APPKI */
.pro-card {
    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.95),
        rgba(245,235,255,0.95)
    );
    border-radius: 36px;
    padding: 60px 50px;
    box-shadow:
        0 40px 90px rgba(42,0,63,0.55),
        inset 0 0 0 1px rgba(255,255,255,0.6);
    text-align: center;
}

/* TEKST */
h1 {
    font-size: 3rem;
    font-weight: 700;
    color: #4a148c;
}
h2 {
    font-size: 1.9rem;
    color: #311B92;
}
p {
    font-size: 1.15rem;
    color: #4A148C;
}

/* PRZYCISKI – BAZA */
.stButton > button {
    width: 100% !important;
    padding: 22px 0 !important;
    border-radius: 999px !important;
    font-size: 1.25rem !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    border: none !important;
    transition: all 0.3s ease !important;
}

/* WYMUSZENIE BIAŁEGO TEKSTU */
.stButton > button * {
    color: white !important;
}

/* 💜 TAK – PREMIUM CTA */
div[data-testid="stHorizontalBlock"] div:nth-of-type(1) .stButton button {
    background: linear-gradient(135deg, #7b1fa2, #ce93d8) !important;
    box-shadow: 0 18px 45px rgba(123,31,162,0.6) !important;
    animation: pulseYes 1.6s infinite;
}

@keyframes pulseYes {
    0% {transform: scale(1);}
    50% {transform: scale(1.09);}
    100% {transform: scale(1);}
}

/* 😈 NIE – STONOWANE */
div[data-testid="stHorizontalBlock"] div:nth-of-type(2) .stButton button {
    background: rgba(90, 40, 120, 0.6) !important;
    animation: none !important;
    transform: none !important;
    opacity: 0.8;
}

/* ZDJĘCIA */
div[data-testid="stImage"] img {
    height: 380px !important;
    object-fit: cover !important;
    border-radius: 28px;
    box-shadow: 0 25px 45px rgba(0,0,0,0.25);
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
    "Nie masz wyboru hihi 😈"
]

# --- 4. Render ---
st.markdown('<div class="pro-card">', unsafe_allow_html=True)


if not st.session_state.accepted:
    st.markdown('<h1>Hej Kochanie... ✨💜</h1>', unsafe_allow_html=True)
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
    st.markdown('<h2>Wiedziałem, że się zgodzisz!! 🥰</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cataas.com/cat/says/Love", use_container_width=True)
    with col2:
        st.image("https://cataas.com/cat/cute", use_container_width=True)

    st.markdown('<h3>Do zobaczenia na randeczce 🌹</h3>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
