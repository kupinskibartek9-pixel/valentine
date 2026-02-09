import streamlit as st

st.set_page_config(
    page_title="Najważniejsze pytanie 💜",
    page_icon="💜",
    layout="centered"
)

# ====================== CSS ======================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

/* USUNIĘCIE STREAMLIT UI */
header, footer, #MainMenu {display:none;}
.block-container {padding-top:4rem; max-width:720px;}
.stDeployButton {display:none;}

body {
    font-family: 'Poppins', sans-serif;
}

/* TŁO */
.stApp {
    background: radial-gradient(circle at top,
        #f3e5f5 0%,
        #e1bee7 35%,
        #ba68c8 70%,
        #6a1b9a 100%);
}

/* KARTA */
.card {
    background: rgba(255,255,255,0.18);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    border-radius: 32px;
    padding: 48px 40px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.25);
    box-shadow:
        0 30px 80px rgba(74,20,140,0.35),
        inset 0 0 40px rgba(255,255,255,0.08);
    animation: fadeIn 1s ease;
}

@keyframes fadeIn {
    from {opacity:0; transform: translateY(20px);}
    to {opacity:1; transform: translateY(0);}
}

/* TEKST */
h1 {
    font-size: 3rem;
    font-weight: 700;
    color: #4a148c;
}
h2 {
    font-weight: 600;
    color: #6a1b9a;
}
p {
    color: #4a148c;
    opacity: 0.9;
    font-size: 1.1rem;
}

/* PRZYCISKI */
.stButton > button {
    border-radius: 999px;
    padding: 16px 32px;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    width: 100%;
    transition: all 0.3s ease;
}

/* TAK */
div[data-testid="column"]:nth-of-type(1) button {
    background: linear-gradient(135deg, #7b1fa2, #ce93d8);
    color: white;
    box-shadow: 0 10px 30px rgba(123,31,162,0.45);
    animation: glow 2s infinite;
}

@keyframes glow {
    0% {box-shadow: 0 10px 30px rgba(123,31,162,0.4);}
    50% {box-shadow: 0 15px 45px rgba(186,104,200,0.7);}
    100% {box-shadow: 0 10px 30px rgba(123,31,162,0.4);}
}

/* NIE */
div[data-testid="column"]:nth-of-type(2) button {
    background: rgba(255,255,255,0.25);
    color: #6a1b9a;
    box-shadow: none;
}

div[data-testid="column"]:nth-of-type(2) button:hover {
    background: rgba(255,255,255,0.35);
}

/* OBRAZY */
img {
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)

# ====================== LOGIKA ======================
if "step" not in st.session_state:
    st.session_state.step = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False
if "error" not in st.session_state:
    st.session_state.error = False

no_texts = [
    "Nie… 😢",
    "Zastanów się 💔",
    "Na pewno? 🥺",
    "Jeszcze raz ✨",
    "Nie masz wyboru 😈"
]

# ====================== UI ======================
st.markdown('<div class="card">', unsafe_allow_html=True)

if not st.session_state.accepted:
    st.markdown("<h1>Hej Ty… 💜</h1>", unsafe_allow_html=True)
    st.markdown("<p>Mam jedno, bardzo ważne pytanie</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin:40px 0;'>Czy zostaniesz moją Walentynką?</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("TAK 😍"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        label = no_texts[min(st.session_state.step, len(no_texts)-1)]
        if st.button(label):
            if label == "Nie masz wyboru 😈":
                st.session_state.error = True
            else:
                st.session_state.step += 1
            st.rerun()

    if st.session_state.error:
        st.error("❌ Błąd systemu. Ta opcja nie istnieje 😈")

else:
    st.balloons()
    st.markdown("<h1>Wiedziałem 💜</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Jesteś moją Walentynką 🥰</h2>", unsafe_allow_html=True)
    st.markdown("<p>To będzie najpiękniejszy dzień 💫</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cataas.com/cat/cute")
    with col2:
        st.image("https://cataas.com/cat/says/Love")

    st.markdown("<h2 style='margin-top:30px;'>Do zobaczenia 🌹</h2>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
