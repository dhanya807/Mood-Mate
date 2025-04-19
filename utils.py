
import random

def get_playlist(mood):
    mood_playlists = {
        "joy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "sadness": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "anger": "https://open.spotify.com/playlist/37i9dQZF1DWZq91oLsHZvy",
        "fear": "https://open.spotify.com/playlist/37i9dQZF1DX6xZZEgC9Ubl",
        "surprise": "https://open.spotify.com/playlist/37i9dQZF1DXa2PvUpywmrr",
        "love": "https://open.spotify.com/playlist/37i9dQZF1DXcCnTAt8CfNe"
    }
    return mood_playlists.get(mood, "https://open.spotify.com/")

def get_quote(mood):
    quotes = {
        "joy": ["Happiness is a direction, not a place."],
        "sadness": ["This too shall pass."],
        "anger": ["Keep calm and carry on."],
        "fear": ["Feel the fear and do it anyway."],
        "surprise": ["Life is full of surprises. Embrace them."],
        "love": ["You are loved more than you know."]
    }
    return random.choice(quotes.get(mood, ["Stay strong."]))

def get_image(mood):
    images = {
        "joy": "https://source.unsplash.com/featured/?happy",
        "sadness": "https://source.unsplash.com/featured/?rain",
        "anger": "https://source.unsplash.com/featured/?fire",
        "fear": "https://source.unsplash.com/featured/?dark",
        "surprise": "https://source.unsplash.com/featured/?sky",
        "love": "https://source.unsplash.com/featured/?heart"
    }
    return images.get(mood, "https://source.unsplash.com/featured/?nature")
