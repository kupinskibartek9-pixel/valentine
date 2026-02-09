import streamlit as st

# --- 1. Konfiguracja strony ---
st.set_page_config(page_title="For My One and Only 💜", page_icon="✨", layout="centered")

# --- 2. CSS - ULTRA PRO VISUALS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap');

    /* Dynamiczne, luksusowe tło */
    .stApp {
        background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 50%, #ce93d8 100%);
        font-family: 'Poppins', sans-serif;
    }

    /* Szklany panel (Glassmorphism) */
    .main-container {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        text-align: center;
    }

    /* Główne napisy - Ciemny, elegancki fiolet */
    h1, h2, h3 {
        color: #311B92 !important;
        font-weight: 700 !important;
        letter-spacing: -1px;
    }
    
    p {
        color: #4A148C !important;
        font-weight: 400;
    }

    /* PRZYCISKI - FULL WHITE TEXT + GLOW */
    .stButton > button {
        background: linear-gradient(45deg, #6A1B9A, #AB47BC);
        border: none !important;
        border-radius: 50px !important;
        padding: 15px 40px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 10px 20px rgba(106, 27, 154, 0.3) !important;
    }

    /* WYMUSZENIE BIAŁEGO KOLORU TEKSTU W PRZYCISKU */
    .stButton > button div p, .stButton > button p, .stButton > button {
        color: white !important;
        font-size: 18px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton > button:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 30px rgba(106, 27, 154, 0.5) !important;
        background: linear-gradient(45deg, #7B1FA2, #BA68C8);
    }

    /* GALERIA ZDJĘĆ - IDENTYCZNA WIELKOŚĆ I EFEKT LUSTRA */
    div[data-testid="stImage"] img {
        height: 350px !important;
        width: 100% !important;
        object-fit: cover !important;
        border-radius: 20px;
        border: 4px solid white;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }

    /* Animacja serc */
    @keyframes floating {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0; }
        50% { opacity: 0.8; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }
    .heart {
        position: fixed;
        bottom: -10vh;
        color: #9C27B0;
        font-size: 1.5rem;
        animation: floating 4s linear infinite;
        z-index: 999;
    }
</style>
""", unsafe_allow_html=True)

def rain_hearts():
    script = """
    <script>
        function createHeart() {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.innerHTML = '💜';
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.animationDuration = Math.random() * 2 + 3 + "s";
            document.body.appendChild(heart);
            setTimeout(() => { heart.remove(); }, 4000);
        }
        setInterval(createHeart, 200);
    </script>
    """
    st.components.v1.html(script, height=0)

# --- 3. Logika Aplikacji ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

no_options = [
    "Nie... 😢",
    "Pomyśl jeszcze raz... 🧐",
    "Na pewno tego chcesz? 🥺",
    "Może jednak TAK? ✨",
    "Ostatnia szansa... 💔",
    "Nie masz wyboru 😈"
]

# --- 4. Renderowanie ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    if not st.session_state.accepted:
        st.title("Hej Kochanie... ✨")
        st.write("Jest coś, co od dawna chciałem Ci powiedzieć.")
        st.markdown("---")
        st.header("Czy zostaniesz moją Walentynką? 💜")
        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("TAK! 😍"):
                st.session_state.accepted = True
                st.rerun()

        with col2:
            current_no_text = no_options[min(st.session_state.step, len(no_options)-1)]
            if st.button(current_no_text):
                if current_no_text == "Nie masz wyboru 😈":
                    st.session_state.accepted = True
                    st.rerun()
                else:
                    st.session_state.step += 1
                    st.rerun()
    else:
        # EKRAN SUKCESU
        rain_hearts()
        st.balloons()
        st.title("Jeeej! Wiedziałem! 💜")
        st.header("Najlepsza decyzja w życiu! 🥰")
        st.write("Kocham Cię najbardziej na świecie!")
        st.markdown("---")
        
        col_a, col_b = st.columns(2)
        with col_a:
            # WGRAJ foto1.jpg na GitHub!
            st.image("https://cataas.com/cat/says/Love", use_container_width=True)
        with col_b:
            # WGRAJ foto2.jpg na GitHub!
            st.image("https://cataas.com/cat/cute", use_container_width=True)
        
        st.markdown("<br><h3>Do zobaczenia na randce! 🌹</h3>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
