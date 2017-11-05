import aylien_news_api
from aylien_news_api.rest import ApiException
import time
import pickle
from utils import *
import json

params = {
    'language': ['en'],
    'source_locations_country': ['US'],
    'published_at_start': 'NOW-1DAYS',
    'published_at_end': 'NOW',
    'categories_taxonomy': 'iab-qag',
    'sort_by': 'hotness',
    'categories_id': ['IAB17', 'IAB12', 'IAB11-4'],
    'cursor': '*',
    'per_page': 16
}

id_to_category = {
    'IAB17': 'Sports',
    'IAB12': 'News',
    'IAB11-4': 'Politics'
}


def fetch_stories(params={}):
  fetched_stories = []
  stories = None

  while (stories is None or len(stories) > 0) and (len(fetched_stories) < 100):
    try:
      response = api_instance.list_stories(**params)
    except ApiException as e:
      if (e.status == 429):
        print('Usage limit are exceeded. Wating for 60 seconds...')
        time.sleep(60)
        continue

    stories = response.stories
    params['cursor'] = response.next_page_cursor

    fetched_stories += stories
    print("Fetched %d stories. Total story count so far: %d" %
          (len(stories), len(fetched_stories)))

  return fetched_stories


# Configure API key authorization: app_id, application_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'cfa4787e'
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '4fd1a82e4716ecccfb9ee352139d6ca9'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()


def get_title_and_location_of_stories(stories):
  """ 
  Preprocess the raw stories from the API to only include the title, link, and location 
  TODO:
  Need some way to filter out places that aren't part of the United States or aren't states of the US
  """

  all_story_titles = []
  stories_and_location = []

  for story in stories:
    title = story.title
    if title not in all_story_titles:
      all_story_titles.append(title)

      all_entities = []
      geo_coordinates = []

      for entities in story.entities.body:
        if "Place" in entities.types:
          coords = convert_location_to_lat_lng(entities.text)
          if coords is not None:
            geo_coordinates.append(coords)  # append the geo_coordinates of the place
            all_entities.append(entities.text)  # append the text of the place
            print entities.text, coords

      if len(all_entities) == 0 or len(all_entities) > 2:
        continue
      else:

        # get the category of the story
        all_ids = [cat.id for cat in story.categories]
        for story_id in all_ids:
          if story_id in id_to_category:
            id_category = id_to_category[story_id]
            break

        # get the image of the story            
        url = story.media[0].url

        # get the summary of the story
        summary = story.summary.sentences

        stories_and_location.append((title, all_entities, story.links.permalink, geo_coordinates, id_category, url, summary))
  return stories_and_location


def create_json_from_stories(stories_and_location):
  """ Convert the preprocessed stories into a list of dictionaries. This will help us with making
  the 3d visualizations """
  stories = []
  for story, location, link, geo_coordinates, category, img_url, summary in stories_and_location:
    story_dict = {}
    story_dict["title"] = story
    story_dict["locations"] = location
    story_dict["link"] = link
    story_dict["geo_coordinates"] = geo_coordinates
    story_dict["category"] = category
    story_dict["img_url"] = img_url
    story_dict["summary"] = summary 

    stories.append(story_dict)
  return stories


stories = fetch_stories(params)
stories = get_title_and_location_of_stories(stories)
stories = create_json_from_stories(stories)

with open("stories.json", "w") as f:
  json.dump(stories, f)

print stories[:5]
