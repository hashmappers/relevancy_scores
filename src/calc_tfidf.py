from sklearn.feature_extraction.text import TfidfVectorizer

# open processed file
f = open('../data/tweets_geo.json', 'r')

# assign tf-idf scores
vectorizer = TfidfVectorizer()
response = vectorizer.fit_transform(f)

print(str(response))