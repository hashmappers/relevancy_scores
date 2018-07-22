import scipy.sparse
import itertools
from sklearn.feature_extraction.text import TfidfVectorizer

# open processed file
f = open('../data_aquaman/tweets_geo.json', 'r')

# assign tf-idf scores
vectorizer = TfidfVectorizer()
m = vectorizer.fit_transform(f)

# create dictionary of unique int_id, weight pairs
# TODO: don't need following?
# uniqueScores = {}
# cm = scipy.sparse.coo_matrix(m)
# for i,j,v in zip(cm.row, cm.col, cm.data):
#     uniqueScores[j] = v

# get list of words by id
vocab = vectorizer.get_feature_names()

# test tweet analysis
tweet = "something something test sentence stuff aquaman"
a = vectorizer.build_analyzer()
aTweet = a(tweet)

score = 0
for tWord in aTweet:
    for i, vWord in enumerate(vocab):
        if(tWord == vWord):
            score += 1
print("Tweet score:", score)
