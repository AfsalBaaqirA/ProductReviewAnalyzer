def add(a, b):
    result = a + b
    return result

def analyzeTextSentiment(text):
    from textblob import TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment.polarity

