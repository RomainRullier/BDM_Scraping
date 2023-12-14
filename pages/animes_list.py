import streamlit as st
import requests

# Remplacez cette URL par l'URL de votre API
API_URL = "http://localhost:8000"

def get_animes():
    response = requests.get(f"{API_URL}/animes")
    if response.status_code == 200:
        return response.json()
    return []

def get_animes_by_letter(letter):
    response = requests.get(f"{API_URL}/animes/{letter}")
    if response.status_code == 200:
        return response.json()
    return []

def display_animes(animes):
    # Créer des lignes avec deux animes chacune
    for i in range(0, len(animes), 2):
        cols = st.columns(2)
        for j in range(2):
            index = i + j
            if index < len(animes):
                anime = animes[index]
                with cols[j]:
                    # Utilisation de Markdown pour afficher l'image et le titre, et la description en dessous
                    st.markdown(f"![{anime['title']}]({anime['img']})")
                    st.markdown(f"**{anime['title']}**")
                    st.write(anime['desc'])

# Widget pour le filtrage par lettre
letter = st .selectbox('Filtrer par Lettre:', ['Toutes'] + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
if letter != 'Toutes':
    filtered_animes = get_animes_by_letter(letter)
    st.write(f'Animes commençant par {letter}:')
    display_animes(filtered_animes)
else:
    # Afficher tous les animes
    animes = get_animes()
    st.write('Tous les Animes:')
    display_animes(animes)

# Initialiser Streamlit
st.title('Liste des Animes')
