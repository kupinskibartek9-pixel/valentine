import streamlit as st
import time

# --- Konfiguracja strony ---
st.set_page_config(page_title="Pytanie...", page_icon="💜")

# --- CSS: Fioletowy styl i animacja serc ---
st.markdown("""
<style>
    /* Tło aplikacji */
    .stApp {
        background-color: #F3E5F5;
    }
    
    /* Styl przycisków */
    .stButton button {
        background-color: #8E24AA;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #6A1B9A;
        border-color: #AB47BC;
    }

    /* Animacja latających serc (HTML/CSS) */
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

# Funkcja generująca deszcz fioletowych serc
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

# --- Zarządzanie stanem (pamięć aplikacji) ---
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# Lista tekstów na przycisk "Nie"
no_texts = [
    "Nie... 😢",
    "Jesteś pewna? 🤔",
    "Ale na pewno? 🥺",
    "Przemyśl to! 💜",
    "Ranisz moje serce! 💔",
    "Dobra, koniec żartów!" # To się już nie wyświetli, bo przycisk zniknie
]

# --- Logika aplikacji ---

if st.session_state.accepted:
    # --- EKRAN SUKCESU ---
    rain_purple_hearts() # Odpalamy fioletowe serca
    st.balloons() # I balony
    
    st.title("Jeeej! Wiedziałem, że się zgodzisz! 💜💜💜")
    st.header("Kocham Cię!")
    
    st.write("---")
    
    # --- MIEJSCE NA ZDJĘCIE ---
    # Opcja 1: Jeśli masz plik zdjęcia w repozytorium (np. 'foto.jpg') odkomentuj linię niżej:
    # st.image("foto.jpg", caption="My 💜", use_column_width=True)
    
    # Opcja 2: Zdjęcie z internetu (dla testu wstawiam słodkiego kota, zmień link na swój!)
    st.image("https://cataas.com/cat/cute", caption="To my! (albo prawie my 😜)", use_container_width=True)
    
else:
    # --- EKRAN PYTANIA ---
    st.title("Hej Kochanie! 💜")
    st.subheader("Mam do Ciebie bardzo ważne pytanie...")
    st.write("---")
    st.header("Czy zostaniesz moją Walentynką? 🍇") # Winogrono bo fioletowe ;)

    col1, col2 = st.columns(2)

    with col1:
        # Przycisk TAK
        if st.button("TAK! 😍", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        # Przycisk NIE (wyświetla się tylko jeśli kliknięto mniej niż 5 razy)
        if st.session_state.no_count < 5:
            # Pobieramy tekst zależnie od licznika
            current_text = no_texts[st.session_state.no_count]
            
            if st.button(current_text, use_container_width=True):
                st.session_state.no_count += 1
                st.rerun()
