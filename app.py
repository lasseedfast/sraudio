import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    url_article = st.text_input('Adress till artikeln').strip()
    if url_article == '':
        st.stop()

    r = requests.get(url_article).content
    soup = BeautifulSoup(r, "html.parser")
    id = soup.find("button", {
        "class": "details-button"
    }).attrs["data-audio-id"]

    # Hitta länken till ljudet i Isidor
    url = f"https://sverigesradio.se/playerajax/audio?id={id}&type=publication&quality=high"

    d = requests.get(url, headers={'Accept': 'application/json'}).json()

    title = d["metadata"]["items"][0]["subtitle"]
    filename = title + ".m4a"

    url = d["audioUrl"]

    # Spara ljudet till en fil
    r = requests.get(url)

    # Ladda ner ljudet.

    with open(filename, 'wb') as f:
        st.download_button('Ladda ned ljudet', r.content, mime="audio/mpeg", file_name= filename)

st.title('Ladda ner ljud från SR')
if __name__ == "__main__":
    main()
