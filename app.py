import streamlit as st
import time

# --- Konfiguracja strony ---
st.set_page_config(page_title="Pytanie...", page_icon="💜")

# --- CSS: Wygląd aplikacji ---
st.markdown("""
<style>
    /* Tło aplikacji - jasny fiolet */
    .stApp {
        background-color: #F3E5F5;
    }
    
    /* WYMUSZENIE CIEMNEGO KOLORU CZCIONKI */
    h1, h2, h3, p, div, span, label {
        color: #4A148C !important; /* Ciemny, głęboki fiolet */
    }
    
    /* Styl przycisków */
    .stButton button {
        background-color: #8E24AA;
        color: white !important; /* Tekst na przycisku musi być biały */
        border-radius: 10px;
        font-weight: bold;
        border: 2px solid #6A1B9A;
    }
    .stButton button:hover {
        background-color: #6A1B9A;
        border-color: #4A148C;
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

# Teksty na przycisk "Nie"
no_texts = [
    "Nie... 😢",
    "Jesteś pewna? 🤔",
    "Ale na pewno? 🥺",
    "Przemyśl to! 💜",
    "Ranisz moje serce! 💔"
]

# --- Logika aplikacji ---

if st.session_state.accepted:
    # --- EKRAN SUKCESU (Po kliknięciu TAK) ---
    rain_purple_hearts()
    st.balloons()
    
    st.title("Jeeej! Wiedziałem, że się zgodzisz! 💜💜💜")
    st.header("Kocham Cię! Jesteś moją Walentynką!")
    st.write("---")
    
    # --- MIEJSCE NA TWOJE ZDJĘCIA ---
    st.subheader("To my! 🥰")
    
    col_foto1, col_foto2 = st.columns(2)
    
    with col_foto1:
        # Tu wpisz nazwę pierwszego pliku, np. "foto1.jpg"
        # Na razie dałem link z internetu, żebyś widział, że działa
        st.image("https://cataas.com/cat", caption="Nasze chwile", use_container_width=True)
        # Jak wgrasz swoje zdjęcie, zmień powyższą linię na:
        # st.image("foto1.jpg", caption="Nasze chwile", use_container_width=True)

    with col_foto2:
        # Tu wpisz nazwę drugiego pliku, np. "foto2.jpg"
        st.image("https://cataas.com/cat/cute", caption="Nasze wspomnienia", use_container_width=True)
        # Jak wgrasz swoje zdjęcie, zmień powyższą linię na:
        # st.image("foto2.jpg", caption="Nasze wspomnienia", use_container_width=True)
    
else:
    # --- EKRAN PYTANIA ---
    st.title("Hej Kochanie! 💜")
    st.subheader("Mam do Ciebie bardzo ważne pytanie...")
    st.write("---")
    st.header("Czy zostaniesz moją Walentynką? 🍇")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("TAK! 😍", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        # Przycisk NIE znika po 5 kliknięciach
        if st.session_state.no_count < 5:
            current_text = no_texts[st.session_state.no_count]
            if st.button(current_text, use_container_width=True):
                st.session_state.no_count += 1
                st.rerun()
