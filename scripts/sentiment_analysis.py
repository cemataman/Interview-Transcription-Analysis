from data_cleaning import read_transcript
from textblob import TextBlob

# read the document
doc = read_transcript()

# join all the paragraphs into a single string
doc_text = ' '.join(doc)

# create a TextBlob object
blob = TextBlob(doc_text)

# get the sentiment polarity score
sentiment_score = blob.sentiment.polarity

# print the sentiment score
print('Sentiment Score:', sentiment_score)
