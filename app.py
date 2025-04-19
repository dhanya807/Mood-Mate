
from flask import Flask, render_template, request
from transformers import pipeline
from utils import get_playlist, get_quote, get_image

app = Flask(__name__)
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        emotion_result = emotion_pipeline(user_input)[0][0]  # first item of the first list
        mood = emotion_result['label'].lower()


        playlist = get_playlist(mood)
        quote = get_quote(mood)
        image_url = get_image(mood)

        return render_template('index.html', mood=mood, quote=quote, playlist=playlist, image_url=image_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
