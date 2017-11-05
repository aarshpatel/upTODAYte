from flask import Flask, render_template, jsonify, make_response
from utils import *
import pickle
import json
import random

app = Flask(__name__)

def get_stories():
    new_stories = {}
    with open("stories.json", "r") as f:
        stories = json.load(f)
    new_stories["data"] = stories
    return new_stories

@app.route('/')
def main():
    stories = get_stories()
    return render_template('index.html', data=json.dumps(stories))

@app.route('/recap_me')
def recap_me():
	stories = get_stories()
	all_summaries = []

	cats = {
			"Sports":  2,
			"Tech":  2,
			"Politics": 2,
			"Celebrity Fan/Gossip": 2,
			"Business": 2
	}

	for story in stories["data"]:
		summary = story["summary"]
		if len(summary) == 0:
			continue

		random_summary = ""
		for story_summary in summary:
			if len(story_summary.split()) < 50 and len(story_summary.split()) > 10:
				random_summary = story_summary
		
		if cats[story["category"]] != 0:	
			all_summaries.append((story["title"], story["img_url"], random_summary, story["link"]))
			cats[story["category"]] -= 1


		if sum(cats.values()) == 0:
			break

	random.shuffle(all_summaries)

	return render_template("recap_me.html", summaries=all_summaries)


if __name__ == '__main__':
    app.run(debug=True)
