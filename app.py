import streamlit as st

# --- 1. Konfiguracja strony ---
st.set_page_config(page_title="For You 💜", page_icon="✨", layout="wide")

# --- 2. CSS - LUXURY INTERFACE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* Animowany luksusowy gradient w tle */
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

    /* Usunięcie domyślnych marginesów Streamlit */
    .block-container {
        padding-top: 2rem !important;
        max-width: 800px !important;
    }

    /* GŁÓWNY PANEL GLASSMORPHISM - NAPRAWIONY */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 40px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 25px 50px rgba(0,0,0,0.1);
        padding: 50px;
        text-align: center;
        margin: 0 auto;
    }

    /* Nagłówki */
    .title-text {
        font-family: 'Playfair Display', serif;
        color: #311B92 !important;
        font-size: 3.5rem !important;
        margin-bottom: 10px;
        line-height: 1.2;
    }

    .sub-text {
        color: #4A148C !important;
        font-size: 1.2rem;
        font-weight: 300;
        margin-bottom: 30px;
    }

    /* PRZYCISKI - DEFINICJA STYLU */
    .stButton > button {
        border-radius: 50px !important;
        padding: 20px 50px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        border: none !important;
        color: white !important; /* BIAŁY TEKST */
        transition: all 0.4s ease !important;
        height: auto !important;
    }

    /* Przycisk TAK (Fioletowy z pulsem) */
    div[data-testid="stHorizontalBlock"] .stButton:nth-of-type(1) button {
        background: linear-gradient(45deg, #7B1FA2, #9C27B0) !important;
        box-shadow: 0 10px 25px rgba(123, 31, 162, 0.4) !important;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 10px 25px rgba(123, 31, 162, 0.4); }
        50% { transform: scale(1.05); box-shadow: 0 15px 35px rgba(123, 31, 162, 0.6); }
        100% { transform: scale(1); box-shadow: 0 10px 25px rgba(123, 31, 162, 0.4); }
    }

    /* Przycisk NIE (Ciemniejszy fiolet / Szary) */
    div[data-testid="stHorizontalBlock"] .stButton:nth-of-type(2) button {
        background: rgba(74, 20, 140, 0.8) !important;
    }

    /* Wymuszenie białego tekstu niezależnie od stanu */
    .stButton > button p, .stButton > button:hover p, .stButton > button:active p {
        color: white !important;
    }

    /* ZDJĘCIA - LUXURY GALLERY */
    div[data-testid="stImage"] img {
        height: 350px !important;
        object-fit: cover !important;
        border-radius: 30px;
        border: 8px solid white;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }

    /* Animacja fioletowych serc */
    .heart {
        position: fixed;
        bottom: -10vh;
        color: #9C27B0;
        font-size: 1.5rem;
        animation: floating 4s linear infinite;
        z-index: 999;
        pointer-events: none;
    }
    @keyframes floating {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0; }
        20% { opacity: 0.8; }
        100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)

# Funkcja JS do serc (fioletowy deszcz)
def rain_hearts():
    st.components.v1.html("""
    <script>
        function createHeart() {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.innerHTML = '💜';
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.animationDuration = Math.random() * 2 + 3 + "s";
            heart.style.position = 'fixed';
            heart.style.bottom = '-10vh';
            heart.style.zIndex = '999';
            document.body.appendChild(heart);
            setTimeout(() => { heart.remove(); }, 5000);
        }
        setInterval(createHeart, 250);
        
        // CSS dla serc wewnątrz JS, żeby na pewno się wstrzyknął
        const style = document.createElement('style');
        style.innerHTML = `
            @keyframes floating {
                0% { transform: translateY(0px) rotate(0deg); opacity: 0; }
                20% { opacity: 0.8; }
                100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; }
            }
            .heart { animation: floating 4s linear infinite; font-family: sans-serif; }
        `;
        document.head.appendChild(style);
    </script>
    """, height=0)

# --- 3. Logika Aplikacji ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

no_options = [
    "Nie... 😢",
    "Pomyśl jeszcze raz... 🧐",
    "Serio? 💔",
    "Daj szansę... ✨",
    "Ostatnia szansa! 🥺",
    "Nie masz wyboru 😈"
]

# --- 4. Renderowanie ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

if not st.session_state.accepted:
    st.markdown('<h1 class="title-text">Hej Kochanie... ✨</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Czekałem na tę chwilę od dawna.</p>', unsafe_allow_html=True)
    st.markdown('<hr style="border: 0.5px solid rgba(255,255,255,0.3)">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #311B92; margin-bottom: 40px;">Czy zostaniesz moją Walentynką?</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("TAK! 😍", key="yes_btn"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        current_no_text = no_options[min(st.session_state.step, len(no_options)-1)]
        if st.button(current_no_text, key="no_btn"):
            if current_no_text == "Nie masz wyboru 😈":
                st.session_state.accepted = True
                st.rerun()
            else:
                st.session_state.step += 1
                st.rerun()
else:
    # --- EKRAN SUKCESU ---
    rain_hearts()
    st.balloons()
    st.markdown('<h1 class="title-text">Jeeej! 💜</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Wiedziałem, że serce podpowie Ci dobrze.</p>', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #311B92;">Kocham Cię najbardziej na świecie!</h2>', unsafe_allow_html=True)
    st.markdown('<hr style="border: 0.5px solid rgba(255,255,255,0.3)">', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        # ZMIEŃ NA "foto1.jpg" JAK WRZUCISZ NA GITHUB
        st.image("https://cataas.com/cat/says/Love", use_container_width=True)
    with col_b:
        # ZMIEŃ NA "foto2.jpg" JAK WRZUCISZ NA GITHUB
        st.image("https://cataas.com/cat/cute", use_container_width=True)
    
    st.markdown('<br><h3 style="color: #4A148C; font-family: Playfair Display, serif;">Do zobaczenia na naszej randce! 🌹</h3>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
