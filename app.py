from flask import Flask, render_template, request, redirect
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from textblob import TextBlob
import webbrowser
count = 0

app = Flask(__name__)

english_bot = ChatBot("ChatterBot", storage_adaptor="chatterbot.storage.SQLStorageAdaptor")
trainer = ChatterBotCorpusTrainer(english_bot)

trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    global count
    userText = request.args.get('msg')
    obj = TextBlob(userText)
    sentiment, subjectivity = obj.sentiment
    print(obj.sentiment)
    if sentiment > 0:
        count = count + 1
    elif sentiment < 0:
        count = count - 1
    else:
        count = count + 0
    print("count", count)

    return str(english_bot.get_response(userText))


@app.route("/forward/", methods=['POST'])
def get_song_playlist():
    global count
    if count > 0:
        return redirect("https://open.spotify.com/playlist/37i9dQZF1DX48TTZL62Yht")
    elif count < 0:
        return redirect("https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT?si=1acb94c12763425f")
    else:
        return redirect("https://open.spotify.com/playlist/3VRgyOBSHasdx1dENlLbir?si=5c7d2c1898e0470d")


if __name__ == '__main__':
    app.run()
