import streamlit as st
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

/* TOTALNE USUNIĘCIE UI STREAMLIT */
header, footer, #MainMenu {display:none !important;}
.stDeployButton {display:none !important;}
html, body, [class*="css"] {margin:0; padding:0;}
section.main > div {padding-top:0 !important;}

/* TŁO */
.stApp {
    background: linear-gradient(135deg,
        #2a003f 0%,
        #4a148c 40%,
        #7b1fa2 70%,
        #ab47bc 100%);
    font-family: 'Poppins', sans-serif;
}

/* GŁÓWNA KARTA */
.main-card {
    background: #ffffff;
    border-radius: 32px;
    padding: 50px 40px;
    text-align: center;
    max-width: 720px;
    margin: 40px auto;
    box-shadow: 0 30px 80px rgba(0,0,0,0.35);
}

/* TEKST */
h1 {
    font-size: 3rem;
    font-weight: 700;
    color: #4a148c;
}
h2 {
    font-size: 1.8rem;
    color: #6a1b9a;
}
p {
    font-size: 1.15rem;
    color: #6a1b9a;
}

/* PRZYCISKI – BAZA */
.stButton > button {
    width: 100% !important;
    padding: 22px 0 !important;
    border-radius: 999px !important;
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    border: none !important;
    transition: all 0.25s ease !important;
}

/* WYMUSZENIE BIAŁEJ CZCIONKI */
.stButton > button * {
    color: #ffffff !important;
}

/* TAK – MEGA PRO */
div[data-testid="column"]:nth-of-type(1) .stButton button {
    background: linear-gradient(135deg, #7b1fa2, #ce93d8) !important;
    box-shadow: 0 15px 40px rgba(123,31,162,0.6) !important;
    animation: pulseYes 1.6s infinite;
}

@keyframes pulseYes {
    0% {transform: scale(1);}
    50% {transform: scale(1.08);}
    100% {transform: scale(1);}
}

/* NIE – WYRAŹNE, ALE SŁABSZE */
div[data-testid="column"]:nth-of-type(2) .stButton button {
    background: #9e9e9e !important;
    box-shadow: none !important;
    font-size: 1.05rem !important;
    opacity: 0.8;
}

div[data-testid="column"]:nth-of-type(2) .stButton button:hover {
    opacity: 1;
}

/* OBRAZY */
img {
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)
