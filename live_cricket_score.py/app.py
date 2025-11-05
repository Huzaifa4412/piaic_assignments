from flask import Flask, render_template
import feedparser

app = Flask(__name__)


@app.route("/")
def live_scores():
    feed = feedparser.parse("https://static.cricinfo.com/rss/livescores.xml")
    scores = [entry.title for entry in feed.entries]
    return render_template("index.html", scores=scores)


if __name__ == "__main__":
    app.run(debug=True)
