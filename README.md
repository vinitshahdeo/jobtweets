# Job Opportunities using Twitter
## Twitter Sentiment Analysis using Python

#### The project is about searching the twitter for job opportunities using popular [#hashtags](https://twitter.com/search?q=%23jobs&src=typd) and applying sentiment analysis on this.

#### Few popular hashtags - 
### `#Jobs` `#Careers` `#JobOpening`
### `#FreshHiring` `#Recruitments` `#JobOpportunities`

### Motivation

Twitter is all about enabling users to send out brief messages to large audiences. If you haven’t been taking advantage of Twitter as a job search tool, it’s time to jump in. When used intelligently, Twitter can have a profound impact on your job search success – or lack thereof. Small steps can help you turn Twitter into your own personal job search platform. Try them today and see what a difference they make in your overall job search success.

### About the Project

#### What is Sentiment Analysis?

Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker.

### Libraries Used

- [Tweepy](http://docs.tweepy.org/en/v3.5.0/) - **tweepy** is the python client for the official [Twitter API](https://developer.twitter.com/en/docs).
- [TextBlob](https://textblob.readthedocs.io/en/dev/) - **textblob** is the python library for processing textual data.

### Installation

- Install **Tweepy** using pip command: `pip install tweepy`
- Install **TextBlob** using pip command: `pip install textblob`

### How to run?

- Get started with **Twitter API** by signing up for [Twitter Developer Account](https://dev.twitter.com/apps).
- In order to fetch tweets through **Twitter API**, you need to register an App through your twitter account. 
- Follow this [link](https://apps.twitter.com/) to register your app.
- Get the API keys. Need help, follow this [link](https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/)
- Open `jobtweets.py` and replace '**XXXXXXXXXXXX**' with your API keys.

```python

        consumer_key = 'XXXXXXXXXXXX'
        consumer_secret = 'XXXXXXXXXXXX'
        access_token = 'XXXXXXXXXXXX'
        access_token_secret = 'XXXXXXXXXXXX'

```
- Run `python jobtweets.py`
- It may take a minute to fetch the results from **Twitter**. Make sure that you've proper internet connection.

### Useful Links

 - [Getting started with Twitter Developer Platform](https://developer.twitter.com/en/docs/basics/getting-started)
 - [How to Install PIP for Python on Windows, Mac and Linux](https://www.makeuseof.com/tag/install-pip-for-python/)