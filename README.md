# Job Opportunities using Twitter

#### The project is about searching the twitter for job opportunities using popular [#hashtags](https://twitter.com/search?q=%23jobs&src=typd) and applying sentiment analysis on this.

#### Few popular hashtags - 
### `#Jobs` `#Careers` `#JobOpening`
### `#FreshHiring` `#Recruitments` `#JobOpportunities`

### Motivation

Twitter is all about enabling users to send out brief messages to large audiences. If you haven’t been taking advantage of Twitter as a job search tool, it’s time to jump in. When used intelligently, Twitter can have a profound impact on your job search success – or lack thereof. Small steps can help you turn Twitter into your own personal job search platform. Try them today and see what a difference they make in your overall job search success.

### Libraries Used

- Tweepy
- TextBlob

### How to run?

- Get **Twitter API** key for your application by signing up for [Twitter Developer Account](https://dev.twitter.com/apps).
- Open `jobtweets.py` and replace '**XXXXXXXXXXXX**' with your API keys.

```python

        consumer_key = 'XXXXXXXXXXXX'
        consumer_secret = 'XXXXXXXXXXXX'
        access_token = 'XXXXXXXXXXXX'
        access_token_secret = 'XXXXXXXXXXXX'

```
- Open command prompt and run `pip install tweepy` and `pip install textblob`
- Run `python jobtweets.py`
- It may take a minute to fetch the results from **Twitter**. Make sure that you've proper internet connection.

### Useful Links

 - [Getting started with Twitter Developer Platform](https://developer.twitter.com/en/docs/basics/getting-started)
 - [How to Install PIP for Python on Windows, Mac and Linux](https://www.makeuseof.com/tag/install-pip-for-python/)