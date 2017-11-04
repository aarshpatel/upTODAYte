import aylien_news_api
from aylien_news_api.rest import ApiException
import time

import time
import aylien_news_api
from aylien_news_api.rest import ApiException

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

def fetch_stories(params={}):
    """ Continously fetch stories from the API """
    fetched_stories = []
    stories = None

    while(stories is None or len(stories) > 0) and len(fetched_stories) < 100:
        try:
            response = api_instance.list_stories(**params)
        except ApiException as e:
            if e.status == 429:
                print('Usage limit are exceeded. Waiting for 60 seconds...')
                time.sleep(60)
                continue

    stories = response.stories

    params['cursor'] = response.next_page_cursor
    fetched_stories += stories

  	# fetched_stories += stories
    print("Fetched %d stories. Total story count so far: %d" %
        (len(stories), len(stories_and_location)))

    return fetched_stories

# Configure API key authorization: app_id, application_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'd5889e03'
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '09edcc0645c5c9bfcc6865bfacf511df'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

def get_title_and_location_of_stories(stories):
    """ Preprocess the raw stories from the API to only include the title, link, and location """
    all_story_titles = []
    stories_and_location = []

    for story in stories:
        title = story.title
        if title not in all_story_titles:
            all_story_titles.append(title)

            all_entities = []
            for entities in story.entities.body:
                if "Place" in entities.types:
                    all_entities.append(entities.text)
            if len(all_entities) == 0 or len(all_entities) > 2:
                continue
            else:
                stories_and_location.append((title, all_entities, story.links.permalink))
    return stories_and_location

stories = fetch_stories(params)

stories_and_locations = get_title_and_location_of_stories(stories)

for story, location, link in stories:
    print story, location, link

