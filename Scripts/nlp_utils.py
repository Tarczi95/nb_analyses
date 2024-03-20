from nltk.sentiment import SentimentIntensityAnalyzer


sia = SentimentIntensityAnalyzer()


def analyze_sentiment(review):
    sentiment_score = sia.polarity_scores(review)['compound']
    if sentiment_score >= 0.1:
        return 'Positive'
    elif sentiment_score <= -0.1:
        return 'Negative'
    else:
        return 'Neutral'
