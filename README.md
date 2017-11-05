# upTODAYte ![logo](https://www.dropbox.com/s/s7zn010rtxg7z84/23269829_1764092683662192_696141440_o.png?raw=1)

Uptodayte is a news aggregation and visualization tool that collects relevant news articles that took place within the last 24 hours.

* Our robust web application continuously scrapes the News API and implements our robust machine algorithm to identify the top headlines of the day
* Hovering over a location marker will reveal a tooltip containing the headline of the corresponding news article
* Clicking on a marker will open the news article about the story or event that took place at that location marker
* If users only need a quick preview of the story, hovering over the marker with a cursor will reveal a tooltip containing the title of the news article
* "What did I miss?!" feature contains a short summary of all the relevant information that occured in the past day

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

What things you need to install the software and how to install them

 * Python 2.7
 * flask
 * geopy 
 * aylien_news_api
 * sumy
 

The requirements.txt file contains all of the modules and versions of those modules to be installed. It can be done like this:

```
pip install -r requirements.txt
```

### Running the Server

The project is built upon a python **flask** server. In order to run the server, run this command

```
python app.py
```

This will create a local server on your machine. Point your web browser to the address displayed in your terminal.


Your browser should something like the following:

![alt text](https://www.dropbox.com/s/yrkqwac9uylegaf/Screen%20Shot%202017-11-05%20at%206.42.56%20AM.png?raw=1)

### Description of Main Files


**app.py**

Contains all of the server code using Flask. 

**retrieve_news_data.py**

Script to retrieve all news articles from the past day. The script also filters out the non-relevant information returned from the NewsAPI and returns the data as JSON. In addition, the script also generates summaries for each news article using **sumy** which uses machine learning techniques to perform automatic summarization on textual documents.

The json output looks like this:

```json
 {
        "category": "Tech",
        "title": "iPhone X Drop Test Proves It's the Most Breakable iPhone Yet?",
        "locations": [
            "China"
        ],
        "summary": [
            "Samuel L. Jackson's Mr. Glass and the new iPhone X have a lot in common.",
            "A man in China has already dropped and destroyed his brand new iPhone X. Apple has been advertising that the new iPhone was made with the most powerful glass yet, but that appears to be quite the exaggeration since the brand new, expensive as hell phone is now destroyed and worthless.",
            "Demand for the new Apple product is off the charts since this is the first real evolutionary change in the iPhone in 3 years as the body and shape of the phone has been the same since the iPhone 6.",
            "The glass backs on Apple's new 2017 iPhones might be really strong.",
            "But the claim that these new phones contain the strongest glass ever to be used on a smartphone is flat-out ridiculous and people are starting to call Apple out."
        ],
        "geo_coordinates": [
            [
                39.913818, 
                116.363625 
            ]
        ],
        "link": "https://movieweb.com/iphone-x-drop-test-video-most-breakable/",
        "img_url": "https://cdn.movieweb.com/img.news.tops/NEkwttq6jwrXnq_1_a/Iphone-X-Drop-Test-Video-Most-Breakable.jpg"
}
```

**utils.py**

Utility script file that contains code to convert textual locations to geo coordinates. 


## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [NewsApi](https://newsapi.aylien.com/) - API to news articles
* [Sumy](https://pypi.python.org/pypi/sumy) - Library to generate summaries for news articles or html documents
* [Geopy](https://github.com/geopy/geopy) - Client for several popular geocoding web services (converting textual locations to coordinates)
* [Mapbox](https://github.com/mapbox/mapbox-gl-js) - a JavaScript library for interactive, customizable vector maps on the web
* [Slick](http://kenwheeler.github.io/slick/) - carousel module for Javascript
* AWS - for deployment of web application

## Authors

* **Aarsh Patel** -https://github.com/aarshpatel
* **Hisham** - https://github.com
* **Varun Sharma** - https://github.com
* **Lynn Samson** - https://github.com/lasamson

See also the list of [contributors](https://github.com/aarshpatel/upTODAYte/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* HackUMass Volunteers
* Participants of HackUMass for helping us out
