from flask import Flask, render_template, jsonify, make_response
from utils import *
import pickle
import json

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
	

if __name__ == '__main__':
	app.run(debug=True)
