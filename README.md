# Job Opportunities using [Twitter](https://twitter.com/Vinit_Shahdeo)
## Twitter Sentiment Analysis using Python

[![Generic badge](https://img.shields.io/badge/Sentiment-Analysis-teal.svg?style=for-the-badge)](https://github.com/vinitshahdeo/jobtweets) 
[![Generic badge](https://img.shields.io/badge/Twitter-API-orange.svg?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Vinit_Shahdeo) [![Generic badge](https://img.shields.io/badge/Job-Opportunities-blue.svg?style=for-the-badge)](https://github.com/vinitshahdeo/jobtweets/raw/master/report/REPORT.pdf) 

#### The project is about searching the twitter for job opportunities using popular [#hashtags](https://twitter.com/search?q=%23jobs&src=typd) and applying sentiment analysis on this.

[![GitHub repo size](https://img.shields.io/github/repo-size/vinitshahdeo/jobtweets.svg?logo=github&style=social)](https://github.com/vinitshahdeo/) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/vinitshahdeo/jobtweets.svg?logo=git&style=social)](https://github.com/vinitshahdeo/) [![GitHub top language](https://img.shields.io/github/languages/top/vinitshahdeo/jobtweets.svg?logo=python&style=social)](https://github.com/vinitshahdeo/)

#### Few popular [#hashtags](https://twitter.com/Vinit_Shahdeo)

[![jobs](https://badgen.net/badge/%23/jobs?&scale=1.3)](https://vinitshahdeo.github.io/jobtweets/) [![Careers](https://badgen.net/badge/%23/careers?&scale=1.3)](https://vinitshahdeo.github.io/jobtweets/) [![JobOpening](https://badgen.net/badge/%23/JobOpening?&scale=1.3)](https://vinitshahdeo.github.io/jobtweets/) 

[![FreshHiring](https://badgen.net/badge/%23/FreshHiring?&scale=1.3)](https://vinitshahdeo.github.io/jobtweets/) [![Recruitments](https://badgen.net/badge/%23/Recruitments?&scale=1.3)](https://vinitshahdeo.github.io/jobtweets/) [![JobOpportunities](https://badgen.net/badge/%23/JobOpportunities?&scale=1.3)](https://vinitshahdeo.github.io/jobtweets/) 


### Motivation

Twitter is all about enabling users to send out brief messages to large audiences. If you haven’t been taking advantage of Twitter as a job search tool, it’s time to jump in. When used intelligently, Twitter can have a profound impact on your job search success – or lack thereof. Small steps can help you turn Twitter into your own personal job search platform. Try them today and see what a difference they make in your overall job search success.

### About the Project

#### What is Sentiment Analysis?

Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker.

#### Steps involved in this project

3 major steps in `jobtweets.py` code :

1. Authorize twitter API client.
2. Make a GET request to Twitter API to fetch tweets for a particular query.
3. Parse the tweets. Classify each tweet as positive, negative or neutral.

[![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/vinitshahdeo/jobtweets) [![Made with love](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/vinitshahdeo) [![Makes people smile](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/vinitshahdeo)
#### Explanation

- First of all, I've created a **TwitterClient** class. This class contains all the methods to interact with Twitter API and parsing tweets. We use `__init__` function to handle the authentication of API client.

- In **get_tweets** function, I have used `fetched_tweets = self.api.search_tweets(q = query, count = count)` to call the Twitter API to fetch tweets. 'query' is basically, the hashtags.

- In **get_tweet_sentiment** I've used textblob module. 
`analysis = TextBlob(self.clean_tweet(tweet))`

- **clean_tweet** method to remove links, special characters, etc. from the tweet using some simple regex.

- I have used **sentiment.polarity** method of **TextBlob** class to get the polarity of tweet between -1 to 1.

```python
if analysis.sentiment.polarity > 0:
       return 'positive'
elif analysis.sentiment.polarity == 0:
       return 'neutral'
else:
       return 'negative'
```
- Finally, I've printing the percentage of positive, negative and neutral tweets about a **#hashtag**(query).

**Note** - You can change the hashtags by changing `query = 'WRITE YOUR OWN HASHTAG'`

```python
tweets = api.get_tweets(query = 'Job Opportunities', count = 500)
```

### Libraries Used

[![tweepy](https://img.shields.io/badge/Python-Tweepy-blue.svg?style=flat&logo=python&logoColor=white)](http://docs.tweepy.org/en/v3.5.0/) [![textblob](https://img.shields.io/badge/Python-TextBlob-blue.svg?style=flat&logo=python&logoColor=white)](https://textblob.readthedocs.io/en/dev/)

- [Tweepy](http://docs.tweepy.org/en/v3.5.0/) - **tweepy** is the python client for the official [Twitter API](https://developer.twitter.com/en/docs).
- [TextBlob](https://textblob.readthedocs.io/en/dev/) - **textblob** is the python library for processing textual data.

### Installation

- Install **Tweepy** using pip command: `pip install tweepy`
- Install **TextBlob** using pip command: `pip install textblob`

- or run `pip install -r requirements.txt` in project directory.

### How to run?

[![python](https://img.shields.io/badge/python-jobtweets.py-lightgrey.svg?logo=python&style=social)](https://github.com/vinitshahdeo/jobtweets/)

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

### Project Reports

[![PPT](https://img.shields.io/static/v1.svg?label=Project&message=PPT&logo=microsoft-powerpoint&style=social)](https://github.com/vinitshahdeo/jobtweets/raw/master/report/presentation.pptx) [![report](https://img.shields.io/static/v1.svg?label=Project&message=Report&logo=microsoft-word&style=social)](https://github.com/vinitshahdeo/jobtweets/raw/master/report/REPORT.pdf)

- [Download](https://github.com/vinitshahdeo/jobtweets/raw/master/report/presentation.pptx) the presentation.
- [Download](https://github.com/vinitshahdeo/jobtweets/raw/master/report/REPORT.pdf) project report.

### Useful Links

 - [Getting started with Twitter Developer Platform](https://developer.twitter.com/en/docs/basics/getting-started)
 - [How to Install PIP for Python on Windows, Mac and Linux](https://www.makeuseof.com/tag/install-pip-for-python/)
 
### Related Work

[![Sentiment Analysis](https://img.shields.io/static/v1.svg?label=Sentiment&message=Analysis&color=lightgray&logo=twitter&style=social&colorA=critical)](https://github.com/vinitshahdeo/TwitterSentimentAnalysis/) [![GitHub top language](https://img.shields.io/github/languages/top/vinitshahdeo/TwitterSentimentAnalysis.svg?logo=php&style=social)](https://github.com/vinitshahdeo/)

[Twitter Sentiment Analyzer](https://vinitshahdeo.github.io/TwitterSentimentAnalysis/) - A web app to search the keywords(Hashtags) on Twitter and analyze the sentiments of it. The source code is written in **PHP** and it performs Sentiment Analysis on Tweets by using the Datumbox API.


### Contributing

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?logo=github)](https://github.com/vinitshahdeo/jobtweets/pulls) [![GitHub issues](https://img.shields.io/github/issues/vinitshahdeo/jobtweets?logo=github)](https://github.com/vinitshahdeo/jobtweets/issues) ![GitHub pull requests](https://img.shields.io/github/issues-pr/vinitshahdeo/jobtweets?color=blue&logo=github) 
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/vinitshahdeo/jobtweets?logo=github)](https://github.com/vinitshahdeo/jobtweets/)

- Clone [this](https://github.com/vinitshahdeo/jobtweets/) repository: 

```bash
git clone https://github.com/vinitshahdeo/jobtweets.git
```

- Check out any issue from [here](https://github.com/vinitshahdeo/jobtweets/issues).

- Make changes and send [Pull Request](https://github.com/vinitshahdeo/jobtweets/pull).
 
### Need help?

[![Facebook](https://img.shields.io/static/v1.svg?label=follow&message=@vinit.shahdeo&color=9cf&logo=facebook&style=flat&logoColor=white&colorA=informational)](https://www.facebook.com/vinit.shahdeo)  [![Instagram](https://img.shields.io/static/v1.svg?label=follow&message=@vinitshahdeo&color=grey&logo=instagram&style=flat&logoColor=white&colorA=critical)](https://www.instagram.com/vinitshahdeo/) [![LinkedIn](https://img.shields.io/static/v1.svg?label=connect&message=@vinitshahdeo&color=success&logo=linkedin&style=flat&logoColor=white&colorA=blue)](https://www.linkedin.com/in/vinitshahdeo/)

:email: Feel free to contact me @ [vinitshahdeo@gmail.com](https://mail.google.com/mail/)

[![GMAIL](https://img.shields.io/static/v1.svg?label=send&message=vinitshahdeo@gmail.com&color=red&logo=gmail&style=social)](https://www.github.com/vinitshahdeo) [![Twitter Follow](https://img.shields.io/twitter/follow/Vinit_Shahdeo?style=social)](https://twitter.com/Vinit_Shahdeo)


### License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fvinitshahdeo%2Fjobtweets.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fvinitshahdeo%2Fjobtweets?ref=badge_large)

MIT &copy; [Vinit Shahdeo](https://github.com/vinitshahdeo/jobtweets/blob/master/LICENSE)

### Author

|                                                                                         <a href="https://www.eatmy.news/2020/06/code-like-you-eat-i-mean-code-daily-as.html"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/vinit-shahdeo.jpg" width="150px " height="150px" /></a>                                                                                         |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                        **[Vinit Shahdeo](https://fayz.in/stories/s/1522/0/?ckt_id=ZGL1ZGVk&title=story_of_vinit_shahdeo)**                                                                                                                                        |
| <a href="https://twitter.com/Vinit_Shahdeo"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/twitter.png" width="32px" height="32px"></a> <a href="https://www.facebook.com/vinit.shahdeo"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/facebook.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/vinitshahdeo/"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/linkedin.png" width="32px" height="32px"></a> |


[![GitHub license](https://img.shields.io/github/license/vinitshahdeo/jobtweets.svg?style=social&logo=github)](https://github.com/vinitshahdeo/jobtweets/blob/master/LICENSE) 
[![GitHub forks](https://img.shields.io/github/forks/vinitshahdeo/jobtweets.svg?style=social)](https://github.com/vinitshahdeo/jobtweets/network) [![GitHub stars](https://img.shields.io/github/stars/vinitshahdeo/jobtweets.svg?style=social)](https://github.com/vinitshahdeo/jobtweets/stargazers) [![GitHub followers](https://img.shields.io/github/followers/vinitshahdeo.svg?label=Follow&style=social)](https://github.com/vinitshahdeo/)

------

<p align="center"><strong><sup>:hugs: <br>Check out my other projects <a href="./PROJECTS.md">here</a>!</sup></strong></p>

------

