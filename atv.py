from nltk.tokenize import word_tokenize 
from nltk.stem.wordnet import WordNetLemmatizer 
import re, string 
def remove_noise(tweet_tokens, stop_words = ()):
    cleaned_tokens = []
    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\'(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)
        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)
        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


from nltk import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_data) 

custom_tweet = "I ordered just once from TerribleCo, they screwed up gain." 
custom_tokens = remove_noise(word_tokenize(custom_tweet)) 



print(classifier.classify(dict([token, True] for token in custom_tokens)))