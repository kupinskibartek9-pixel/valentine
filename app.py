import streamlit as st

# --- 1. Konfiguracja strony ---
# Ustawiamy layout na "centered", żeby panel był ładnie na środku
st.set_page_config(page_title="Pytanie... 💜", page_icon="✨", layout="centered")

# --- 2. CSS - TOTALNE NADPISANIE STYLÓW ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    /* UKRYCIE ELEMENTÓW SYSTEMOWYCH STREAMLIT - NA AMEN */
    header[data-testid="stHeader"] {visibility: hidden; height: 0;}
    #MainMenu {visibility: hidden; height: 0;}
    footer {visibility: hidden; height: 0;}
    .stDeployButton {display: none;}
    
    /* RESET MARGINESÓW GŁÓWNEGO KONTENERA */
    .block-container {
        padding-top: 2rem !important; /* Mały odstęp od góry okna */
        padding-bottom: 2rem !important;
        max-width: 700px !important; /* Szerokość panelu */
    }

    /* TŁO CAŁEJ STRONY - DELIKATNY FIOLETOWY GRADIENT */
    .stApp {
        background: linear-gradient(135deg, #ECEFF1 0%, #F3E5F5 50%, #E1BEE7 100%);
        font-family: 'Poppins', sans-serif;
    }

    /* GŁÓWNY PANEL (PROSTOKĄT Z CIENIEM) DLA CAŁEJ TREŚCI */
    .main-card {
        background: rgba(255, 255, 255, 0.95); /* Prawie białe tło */
        border-radius: 30px; /* Zaokrąglone rogi */
        box-shadow: 0 20px 60px rgba(0,0,0,0.15), 0 10px 20px rgba(0,0,0,0.1); /* Głęboki cień */
        padding: 40px; /* Wewnętrzny odstęp */
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.5);
    }

    /* TYPOGRAFIA */
    h1 {
        color: #4A148C !important;
        font-weight: 700 !important;
        font-size: 2.8rem !important;
    }
    h2 {
        color: #6A1B9A !important;
        font-weight: 600 !important;
    }
    p {
        color: #7B1FA2 !important;
        font-size: 1.1rem;
    }
    hr {
        border-color: rgba(106, 27, 154, 0.2) !important;
    }

    /* STYLE PRZYCISKÓW - BAZA */
    .stButton > button {
        border-radius: 50px !important;
        padding: 15px 30px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    /* WYMUSZENIE BIAŁEGO TEKSTU NA PRZYCISKACH */
    .stButton > button p {
        color: white !important;
    }

    /* --- SELEKCJA PRZYCISKÓW --- */

    /* PRZYCISK TAK (Pierwsza kolumna) -> PULSUJE */
    div[data-testid="column"]:nth-of-type(1) .stButton button {
        background: linear-gradient(45deg, #7B1FA2, #AB47BC) !important;
        box-shadow: 0 8px 20px rgba(123, 31, 162, 0.3) !important;
        animation: pulseYes 2s infinite;
    }
    @keyframes pulseYes {
        0% { transform: scale(1); box-shadow: 0 8px 20px rgba(123, 31, 162, 0.3); }
        50% { transform: scale(1.05); box-shadow: 0 12px 30px rgba(123, 31, 162, 0.5); }
        100% { transform: scale(1); box-shadow: 0 8px 20px rgba(123, 31, 162, 0.3); }
    }

    /* PRZYCISK NIE (Druga kolumna) -> STATYCZNY, BEZ PULSU */
    div[data-testid="column"]:nth-of-type(2) .stButton button {
        background: rgba(106, 27, 154, 0.7) !important; /* Ciemniejszy, matowy fiolet */
        box-shadow: none !important; /* BRAK CIENIA */
        animation: none !important; /* BRAK ANIMACJI - NA PEWNO */
        transform: none !important; /* BRAK POWIĘKSZANIA */
    }
    /* Delikatny efekt najechania na NIE (zmiana koloru, bez ruchu) */
    div[data-testid="column"]:nth-of-type(2) .stButton button:hover {
        background: rgba(106, 27, 154, 0.9) !important;
    }

    /* STYLE ZDJĘĆ W GALERII */
    div[data-testid="stImage"] img {
        height: 300px !important;
        object-fit: cover !important;
        border-radius: 20px;
        border: 5px solid white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# --- 3. Logika Aplikacji ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False
if 'show_error' not in st.session_state:
    st.session_state.show_error = False

no_options = [
    "Nie... 😢",
    "Pomyśl jeszcze raz... 🧐",
    "Na pewno? 💔",
    "Daj szansę... ✨",
    "Nie masz wyboru 😈"
]

# --- 4. Renderowanie - WSZYSTKO W JEDNYM KONTENERZE ---
# Otwieramy główny panel
st.markdown('<div class="main-card">', unsafe_allow_html=True)

if not st.session_state.accepted:
    # --- EKRAN PYTANIA ---
    st.markdown('<h1>Hej Kochanie... ✨</h1>', unsafe_allow_html=True)
    st.markdown('<p>Mam do Ciebie najważniejsze pytanie...</p>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<h2 style="margin: 40px 0;">Czy zostaniesz moją Walentynką? 💜</h2>', unsafe_allow_html=True)

    # Kolumny z przyciskami
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        if st.button("TAK! 😍", key="yes_final"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        current_no_text = no_options[min(st.session_state.step, len(no_options)-1)]
        if st.button(current_no_text, key="no_final"):
            if current_no_text == "Nie masz wyboru 😈":
                st.session_state.show_error = True # Pokazujemy błąd
            else:
                st.session_state.step += 1 # Następny tekst
            st.rerun()

    # Komunikat o błędzie (wyświetlany WĘWNĄTRZ panelu)
    if st.session_state.show_error:
        st.markdown("<br>", unsafe_allow_html=True)
        st.error("⚠️ BŁĄD SYSTEMU: Ta opcja jest niedostępna! Wybierz jedyną słuszną odpowiedź. 😈")

else:
    # --- EKRAN SUKCESU ---
    st.balloons()
    st.markdown('<h1>Jeeej! 💜</h1>', unsafe_allow_html=True)
    st.markdown('<h2>Wiedziałem, że się zgodzisz! 🥰</h2>', unsafe_allow_html=True)
    st.markdown('<p>Kocham Cię najbardziej na świecie!</p>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    
    # Galeria zdjęć
    st.markdown('<h3 style="color: #6A1B9A; margin-bottom: 20px;">To my:</h3>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2, gap="small")
    with col_a:
        # PAMIĘTAJ: Wgraj foto1.jpg na GitHub i zmień link!
        st.image("https://cataas.com/cat/says/Love", use_container_width=True)
    with col_b:
        # PAMIĘTAJ: Wgraj foto2.jpg na GitHub i zmień link!
        st.image("https://cataas.com/cat/cute", use_container_width=True)
    
    st.markdown('<br><h2 style="margin-top: 30px;">Do zobaczenia na randce! 🌹</h2>', unsafe_allow_html=True)

# Zamykamy główny panel
st.markdown('</div>', unsafe_allow_html=True)
