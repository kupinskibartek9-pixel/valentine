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

    /* Tło z płynnym luksusowym gradientem */
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

    /* Wycentrowanie i usunięcie zbędnych marginesów */
    .block-container {
        padding-top: 5vh !important;
        max-width: 850px !important;
    }



    /* STYLIZACJA PRZYCISKÓW */
    .stButton > button {
        border-radius: 50px !important;
        padding: 20px 40px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        border: none !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        height: auto !important;
        width: 100% !important;
    }

    /* WYMUSZENIE BIAŁEGO TEKSTU */
    .stButton > button p {
        color: white !important;
        margin-bottom: 0 !important;
    }

    /* TYLKO PRZYCISK TAK PULSUJE */
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

    /* PRZYCISK NIE - STATYCZNY I ELEGANCKI */
    div[data-testid="stHorizontalBlock"] div:nth-of-type(2) .stButton button {
        background: rgba(74, 20, 140, 0.7) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
    }

    /* GALERIA ZDJĘĆ */
    div[data-testid="stImage"] img {
        height: 380px !important;
        object-fit: cover !important;
        border-radius: 35px;
        border: 10px solid white;
        box-shadow: 0 25px 45px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- 3. Logika (Stan) ---
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
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

if not st.session_state.accepted:
    st.markdown('<h1 class="title-text">Hej Kochanie... ✨</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #4A148C; font-size: 1.1rem;">Przygotowałem dla Ciebie coś specjalnego.</p>', unsafe_allow_html=True)
    st.markdown('<hr style="border: 0.5px solid rgba(255,255,255,0.3); margin: 30px 0;">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #311B92; margin-bottom: 45px; font-weight: 600;">Czy zostaniesz moją Walentynką?</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        if st.button("TAK! 😍", key="yes_final"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        current_no_text = no_options[min(st.session_state.step, len(no_options)-1)]
        if st.button(current_no_text, key="no_final"):
            if current_no_text == "Nie masz wyboru 😈":
                st.session_state.show_error = True
            else:
                st.session_state.step += 1
            st.rerun()

    # WYŚWIETLANIE ŚMIESZNEGO BŁĘDU
    if st.session_state.show_error:
        st.markdown("<br>", unsafe_allow_html=True)
        st.error("BŁĄD 404: Wybrana opcja wygasła lub nigdy nie istniała! Proszę natychmiast kliknąć przycisk po lewej stronie. ⚠️😈")
        st.warning("System wykrył próbę oszustwa! Odpowiedź 'TAK' jest jedyną dostępną w Twoim regionie.")

else:
    # --- EKRAN SUKCESU ---
    st.balloons()
    st.markdown('<h1 class="title-text">Jeeej! 💜</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #311B92; margin-bottom: 20px;">Wiedziałem! Najlepsza decyzja w życiu! 🥰</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #4A148C; font-size: 1.3rem; font-weight: 600;">Kocham Cię najbardziej na świecie!</p>', unsafe_allow_html=True)
    st.markdown('<hr style="border: 0.5px solid rgba(255,255,255,0.3); margin: 30px 0;">', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2, gap="medium")
    with col_a:
        # PAMIĘTAJ O foto1.jpg na GitHubie!
        st.image("https://cataas.com/cat/says/Love", use_container_width=True)
    with col_b:
        # PAMIĘTAJ O foto2.jpg na GitHubie!
        st.image("https://cataas.com/cat/cute", use_container_width=True)
    
    st.markdown('<br><h3 style="color: #311B92; font-family: Playfair Display, serif; font-size: 2rem;">Do zobaczenia na naszej randce! 🌹</h3>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
