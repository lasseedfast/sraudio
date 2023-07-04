import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    url_article = st.text_input('Adress till artikeln').strip()
    if url_article == '':
        st.stop()
    else:
        url_article
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
    url
    # Spara ljudet till en fil
    r = requests.get(url)

    with open(filename, 'rb') as f:
        st.download_button('Ladda ned ljudet', r.content, mime="audio/mpeg", file_name= filename)


if __name__ == "__main__":
    main()
