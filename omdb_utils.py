# omdb_utils.py
import requests

def get_movie_details(title, api_key):

    url = url = "http://www.omdbapi.com/?i=tt3896198&apikey=f2bc851"

    res = requests.get(url).json()
    if res.get("Response") == "True":
        result = res.get("Plot", "N/A"), res.get("Poster", "N/A")
        plot = result[0]
        poster = result[1]
        return plot, poster

    return "N/A", "N/A"
