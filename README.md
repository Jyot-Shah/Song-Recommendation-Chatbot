# Emotion-based Song Recommendation Chatbot 🎵🤖

A Flask-based intelligent chatbot that analyzes user sentiment through conversation and recommends personalized Spotify playlists based on detected mood.

## 📋 Table of Contents
- Overview
- Features
- How It Works
- Technologies Used
- Prerequisites
- Installation
- Running the Project
- Project Structure
- Usage
- Important Notes
- Troubleshooting
- License
- Authors
- Acknowledgments

## 🌟 Overview

This project combines natural language processing and sentiment analysis to create an interactive chatbot that understands your mood and recommends appropriate Spotify playlists. The more you chat, the better it understands your emotional state!

## ✨ Features

- **Interactive Chatbot**: Powered by ChatterBot with English corpus training
- **Real-time Sentiment Analysis**: Uses TextBlob to analyze emotional tone of messages
- **Mood-based Recommendations**: Suggests Spotify playlists based on cumulative sentiment:
  - 😊 Positive mood → Upbeat/Happy playlists
  - 😢 Negative mood → Mellow/Sad playlists
  - 😐 Neutral mood → Balanced playlists

## 🔧 How It Works

1. **Chat Phase**: User engages in conversation with the bot
2. **Sentiment Tracking**: Each message is analyzed for sentiment polarity
   - Positive messages increment the sentiment counter
   - Negative messages decrement the counter
   - Neutral messages don't affect the counter
3. **Recommendation**: When user clicks "Song Recommendations", the system:
   - Evaluates the cumulative sentiment score
   - Redirects to an appropriate Spotify playlist
   - Opens the playlist in the same browser tab

### Sentiment Score Logic
```
count > 0  → Happy Playlist
count < 0  → Sad Playlist
count == 0 → Neutral Playlist
```

## 🛠 Technologies Used

- **Backend**: Flask (Python web framework)
- **Chatbot**: ChatterBot (conversational AI library)
- **NLP**: TextBlob (sentiment analysis)
- **Database**: SQLite (conversation storage)
- **Frontend**: HTML/CSS/JavaScript
- **Music Service**: Spotify Web Player

## 📦 Prerequisites

- **Python 3.7+**
- **pip**
- **Internet connection** (for Spotify)
- **Modern web browser**

## 🚀 Installation

```bash
git clone https://github.com/Jyot-Shah/Song-Recommendation-Chatbot.git
cd Song-Recommendation-Chatbot

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # on Windows

# Install dependencies
pip install flask chatterbot chatterbot-corpus textblob pytz

# Download TextBlob corpora (first time only)
python -m textblob.download_corpora
```

## ▶️ Running the Project

```bash
python app.py
# or
set FLASK_APP=app.py
flask run
```

Open `http://127.0.0.1:5000/` in your browser. Stop with `Ctrl + C`.

## 📁 Project Structure
```
Song-Recommendation-Chatbot/
├── app.py
├── db.sqlite3            # auto-created after you run the 'app.py' file
├── templates/
│   └── index.html
├── static/
│   ├── styles.css
│   └── headphone.jpg
├── LICENSE
├── .gitignore
└── README.md
```

## 💡 Usage

1. Chat with the bot; sentiment is tracked automatically.
2. Click **Song Recommendations** to be redirected (same tab) to a Spotify playlist matching your mood.

## ⚠️ Important Notes

- Global `count` resets on server restart; single-user oriented.
- Initial ChatterBot training can take 30–60 seconds.
- Ensure port 5000 is free; change via `app.run(port=5001)` if needed.
- Internet is required for Spotify access.

### Customizing Playlists
Edit the URLs in `app.py` under `get_song_playlist()` to use your own happy/sad/neutral playlists.

## 🐛 Troubleshooting

- **ChatterBot install fails**: `pip install chatterbot==1.0.4 SQLAlchemy==1.3.24 pytz`
- **Port in use**: run Flask on another port.
- **Bot silent**: let training finish; check terminal logs; delete `db.sqlite3` and restart.
- **Playlist not opening**: check internet and playlist URLs.

## 📄 License

MIT License (see `LICENSE`).

## 👥 Authors

- [Jyot Shah](https://www.linkedin.com/in/jyotshah1/)

## 🙏 Acknowledgments

- Inspired by [yogsgehlot/Chatbot-Song-Recommender-System](https://github.com/yogsgehlot/Chatbot-Song-Recommender-System)
- ChatterBot, TextBlob, Flask, and Spotify

---

**Note**: This is an educational project and not intended for production use without significant modifications for scalability and security.

For questions or issues, please open an issue on GitHub or mail to **jyotshah1595@gmail.com**

**Happy Chatting! 🎵**
