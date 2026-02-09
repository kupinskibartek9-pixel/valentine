import streamlit as st
import time

# --- 1. Konfiguracja strony ---
st.set_page_config(page_title="Walentynka 2026", page_icon="💜", layout="centered")

# --- 2. CSS - STYLING "PRO" ---
st.markdown("""
<style>
    /* Import czcionki dla ładniejszego wyglądu */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    /* Tło całej aplikacji - delikatny gradient */
    .stApp {
        background: linear-gradient(135deg, #fdfbfd 0%, #e2d1f0 100%);
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Nagłówki */
    h1, h2, h3 {
        color: #4A148C !important;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    p {
        color: #6A1B9A !important;
        font-size: 1.2rem;
        text-align: center;
    }

    /* STYL PRZYCISKÓW - WYMASTEROWANY */
    .stButton > button {
        background: linear-gradient(to right, #8E24AA, #7B1FA2);
        color: white !important; /* Biały tekst */
        font-weight: bold;
        border: none;
        border-radius: 25px; /* Zaokrąglone rogi */
        padding: 15px 30px;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2); /* Cień pod przyciskiem */
        transition: all 0.3s ease;
        width: 100%;
    }

    /* Efekt najechania myszką na przycisk */
    .stButton > button:hover {
        transform: scale(1.05); /* Lekkie powiększenie */
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        background: linear-gradient(to right, #9C27B0, #8E24AA);
    }
    
    /* --- GALERIA ZDJĘĆ PRO --- */
    /* To wymusza, żeby zdjęcia były tej samej wielkości i przycięte do kwadratu */
    div[data-testid="stImage"] img {
        height: 300px !important; /* Stała wysokość */
        object-fit: cover !important; /* Dopasowanie bez rozciągania */
        border-radius: 15px; /* Zaokrąglone rogi zdjęć */
        box-shadow: 0 8px 16px rgba(0,0,0,0.2); /* Cień pod zdjęciem */
        transition: transform 0.3s ease;
    }
    
    div[data-testid="stImage"] img:hover {
        transform: scale(1.02);
    }

    /* Animacja serc */
    @keyframes falling {
        0% { transform: translateY(-10vh); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(110vh); opacity: 0; }
    }
    .heart {
        position: fixed;
        color: #8E24AA;
        font-size: 2rem;
        animation: falling 3s linear infinite;
        z-index: 9999;
    }
</style>
""", unsafe_allow_html=True)

# Funkcja JS do serc
def rain_purple_hearts():
    script = """
    <script>
        function createHeart() {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.innerHTML = '💜';
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.animationDuration = Math.random() * 2 + 3 + "s";
            document.body.appendChild(heart);
            setTimeout(() => { heart.remove(); }, 5000);
        }
        setInterval(createHeart, 300);
    </script>
    """
    st.components.v1.html(script, height=0)

# --- 3. Logika (Stan aplikacji) ---
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# Teksty na przycisk "Nie"
no_texts = [
    "Nie... 😢",
    "Jesteś pewna? 🤔",
    "Szkoda... 💔",
    "Przemyśl to! 🥺",
    "Nie masz wyboru 😈" # Ostatni tekst
]

# --- 4. Główny widok ---

if st.session_state.accepted:
    # --- EKRAN SUKCESU ---
    rain_purple_hearts()
    st.balloons()
    
    st.title("Jeeej! 💜💜💜")
    st.header("Wiedziałem, że się zgodzisz!")
    st.write("Jesteś moją Walentynką! Kocham Cię!")
    st.write("---")
    
    st.subheader("My 🥰")
    
    # Kolumny na zdjęcia
    col_foto1, col_foto2 = st.columns(2)
    
    with col_foto1:
        # ZMIEŃ LINK/NAZWĘ PLIKU PONIŻEJ
        st.image("https://cataas.com/cat", use_container_width=True) 

    with col_foto2:
        # ZMIEŃ LINK/NAZWĘ PLIKU PONIŻEJ
        st.image("https://cataas.com/cat/cute", use_container_width=True)
    
else:
    # --- EKRAN PYTANIA ---
    st.markdown("<br>", unsafe_allow_html=True) # Odstęp od góry
    st.title("Hej Kochanie! 💜")
    st.write("Mam do Ciebie bardzo ważne pytanie...")
    
    # Opcjonalnie: Główne zdjęcie pytające (możesz dodać jeśli chcesz)
    # st.image("pytanie.jpg", width=300)
    
    st.markdown("---")
    st.header("Czy zostaniesz moją Walentynką? 🍇")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="medium")

    with col1:
        if st.button("TAK! 😍", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        # Pobieramy tekst
        if st.session_state.no_count < len(no_texts):
            current_text = no_texts[st.session_state.no_count]
        else:
            current_text = no_texts[-1] # Zabezpieczenie, zostaje ostatni tekst

        # Rysujemy przycisk "Nie"
        if st.button(current_text, use_container_width=True):
            # Jeśli to był ostatni tekst (Diabełek), to kliknięcie działa jak zgoda!
            if current_text == "Nie masz wyboru 😈":
                st.session_state.accepted = True
                st.rerun()
            else:
                # W innym przypadku po prostu zmieniamy tekst
                st.session_state.no_count += 1
                st.rerun()
