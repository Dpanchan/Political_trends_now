from flask import Flask, request, render_template
from collections import defaultdict
import json
import sys

app = Flask(__name__)

hot_topics = defaultdict(int)

@app.route("/event_sink", methods=["POST"])
def handle_feed():
  topic = request.form["topic"]
  hot_topics[topic] += 1
  return '{ "received topic": "%s" }' % topic

@app.route("/hot-topics")
def render_graph():
  items = []
  for (k, v) in hot_topics.items():
    items.append([k, v])

  stats = json.dumps([["Politician", "Trendiness"]] + items)

  with open("/home/Divya5270/trends_now/pie.html") as pie:
    return pie.read() % stats
  return render_template("pie.html")


if __name__ == "__main__":
  app.run(debug=True,
    host=sys.argv[1],
    port=int(sys.argv[2]))
