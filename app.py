import streamlit as st
import requests
from bs4 import BeautifulSoup


def download_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("downloaded_content.txt", "wb") as file:
            file.write(response.content)
        st.success("Content downloaded successfully!")
    else:
        st.error("Failed to download content. Please check the URL.")

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

    comment = d["metadata"]["items"][0]["description"] + f' \n{url_article}'

    title = d["metadata"]["items"][0]["subtitle"]
    filename = title + ".m4a"

    url = d["audioUrl"]
    url
    # Spara ljudet till en fil
    r = requests.get(url)
    # with open(file, "wb") as f:
    #     f.write(r.content)

    with open(filename, "wb") as f:
        f.write(r.content)

    with open(filename, 'rb') as f:
        st.download_button('Ladda ned ljudet', r.content, mime="audio/mpeg", file_name= filename)


if __name__ == "__main__":
    main()
