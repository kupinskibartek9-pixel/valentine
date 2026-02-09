import streamlit as st

# Konfiguracja strony (tytuł w karcie przeglądarki, ikonka)
st.set_page_config(page_title="Pytanie do Ciebie...", page_icon="💌")

# Tytuł i nagłówek
st.title("Hej Kochanie! 💖")
st.header("Mam do Ciebie ważne pytanie...")
st.write("---") # Linia oddzielająca

# Wyświetlenie zdjęcia (opcjonalne - możesz tu wstawić link do waszego zdjęcia)
# st.image("https://twoj-link-do-zdjecia.com/foto.jpg")

st.subheader("Czy zostaniesz moją Walentynką? 🌹")

# Układ kolumn, żeby przyciski były obok siebie (na komputerze)
col1, col2 = st.columns(2)

with col1:
    yes_btn = st.button("TAK! 😍", use_container_width=True)

with col2:
    no_btn = st.button("Nie... 😢", use_container_width=True)

# Logika przycisków
if yes_btn:
    st.balloons() # Animacja balonów
    st.success("Jeeej! Wiedziałem, że się zgodzisz! Kocham Cię! ❤️❤️❤️")
    st.write("Wpadnij do mnie po prezent! 🎁")
    
if no_btn:
    st.error("Błąd systemu! ⚠️ Ta odpowiedź jest niepoprawna. Spróbuj ponownie!")
    st.warning("Podpowiedź: Jedyna słuszna odpowiedź znajduje się po lewej stronie 😉")
