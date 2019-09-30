import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import pandas as pd


load_dotenv()
TOKEN = os.getenv("GENIUSTOKEN")

defaults = {
    "request": {
        "token": TOKEN,
        "base_url": "https://api.genius.com"
    },
    "message": {
        "search_fail": "The lyrics for this song were not found!",
        "wrong_input": "Wrong number of arguments.\n"
                       "Use two parameters to perform a custom search "
                       "or none to get the song currently playing on Spotify."
    }
}


def request_song_info(song_title, artist_name):
    base_url = defaults["request"]["base_url"]
    headers = {"Authorization": "Bearer " + defaults["request"]["token"]}
    search_url = base_url + "/search"
    data = {"q": song_title + " " + artist_name}
    response = requests.get(search_url, data=data, headers=headers)

    return response


def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    [h.extract() for h in html("script")]
    lyrics = html.find("div", class_="lyrics").get_text()

    return lyrics


def main():
    df = pd.read_csv("data/top_200_features.csv")
    tracklist = list(zip(df["Track Name"], df["Artist"]))

    f = open("data/lyrics.txt", "a")
    for track in tracklist:
        song_title, artist_name = track[0], track[1]

        print("{} by {}".format(song_title, artist_name))

        # Search for matches in request response
        response = request_song_info(song_title, artist_name)
        json = response.json()
        remote_song_info = None

        for hit in json["response"]["hits"]:
            if artist_name.lower() in hit["result"]["primary_artist"]["name"].lower():
                remote_song_info = hit
                break

        # Extract lyrics from URL if song was found
        if remote_song_info:
            song_url = remote_song_info["result"]["url"]
            lyrics = scrap_song_url(song_url)

            f.write("{} by {}".format(song_title, artist_name))
            f.write(lyrics)

            print(lyrics)
        else:
            print(defaults["message"]["search_fail"])
    f.close()


if __name__ == "__main__":
    main()
